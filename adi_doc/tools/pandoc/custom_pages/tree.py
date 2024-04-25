import os
# import networkx as nx
import shutil
import logging

tree_logger = logging.getLogger("tree")

def parse_file(filename, kernel_root):
    print("Parsing file:", filename)
    """Parse a file."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, "r") as f:
        text = f.read()

    # Get list of headers and other dts, dtsi files
    headers = []
    dt_files = []
    for line in text.split("\n"):
        if line.startswith("#include"):
            is_global = "<" in line and ">" in line
            file_path = (
                line.split("#include")[1].strip().strip('"').strip("<").strip(">")
            )
            if not is_global:
                file_path = os.path.join(os.path.dirname(filename), file_path)
            else:
                file_path = os.path.join(kernel_root, "include", file_path)
            if ".h" in file_path:
                headers.append(file_path)
            else:
                dt_files.append(file_path)

    tree_logger.info(f"Parsed headers: {headers}")
    tree_logger.info(f"Parsed dt_files: {dt_files}")
    tree_logger.info("-" * 80)

    return headers, dt_files


def parse_devicetree_dependencies_from_file(filename, kernel_root):
    """Parse devicetree dependencies from a file."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, "r") as f:
        text = f.read()

    headers, dt_files = parse_file(filename, kernel_root)
    # print("Parsed headers:", headers)
    # print("Parsed dt_files:", dt_files)

    # recursively parse all dependencies
    parsed_headers = []
    parsed_dt_files = []
    while True:

        headers_to_parse = []
        dts_to_parse = []

        for header in headers:
            if header in parsed_headers:
                continue
            parsed_headers.append(header)
            headers_i, dt_files_i = parse_file(header, kernel_root)
            headers_to_parse += headers_i
            dts_to_parse += dt_files_i

        for dt_file in dt_files:
            if dt_file in parsed_dt_files:
                continue
            parsed_dt_files.append(dt_file)
            headers_i, dt_files_i = parse_file(dt_file, kernel_root)
            headers_to_parse += headers_i
            dts_to_parse += dt_files_i

        # print("Parsed headers:", parsed_headers)
        # print("Parsed dt_files:", parsed_dt_files)

        if not headers_to_parse and not dts_to_parse:
            break

        headers = headers_to_parse
        dt_files = dts_to_parse

    # Add root node
    if ".h" in filename:
        parsed_headers.append(filename)
    else:
        parsed_dt_files.append(filename)

    return parsed_headers, parsed_dt_files


def determine_relationships(parsed_headers, parsed_dt_files, kernel_root):
    """Determine relationships between the files."""
    # Get all absolute paths
    parsed_headers = [os.path.abspath(header) for header in parsed_headers]
    parsed_dt_files = [os.path.abspath(dt_file) for dt_file in parsed_dt_files]
    # Strip the kernel root from the paths
    # kernel_root = os.path.abspath(kernel_root)
    # parsed_header_names = [header.replace(kernel_root, "") for header in parsed_headers]
    # parsed_dt_file_names = [dt_file.replace(kernel_root, "") for dt_file in parsed_dt_files]
    # Extract filename without paths
    parsed_header_names = [os.path.basename(header) for header in parsed_headers]
    parsed_dt_file_names = [os.path.basename(dt_file) for dt_file in parsed_dt_files]

    all_files = parsed_headers + parsed_dt_files
    all_file_names = parsed_header_names + parsed_dt_file_names

    source_files = {}
    for path, name in zip(all_files, all_file_names):
        f_type = "header" if ".h" in name else "dts"
        source_files[name] = {"type": f_type, "dependencies": []}
        with open(path, "r") as f:
            text = f.read()
        for line in text.split("\n"):
            if line.startswith("#include"):
                file_path = (
                    line.split("#include")[1].strip().strip('"').strip("<").strip(">")
                )
                filename = os.path.basename(file_path)
                source_files[name]["dependencies"].append(filename)
                found = any(file_path in file for file in all_files)
                if not found:
                    raise FileNotFoundError(
                        f"File not found in previous search: {file_path}"
                    )

    return source_files


def generate_web_links(target_files, kernel_root, root_url):
    """Generate web links for all files."""
    if root_url.endswith("/"):
        root_url = root_url[:-1]
    kernel_root = os.path.abspath(kernel_root)
    links = {}
    for file in target_files:
        full_path = os.path.abspath(file)
        # Remove the kernel root
        relative_path = full_path.replace(kernel_root, "")
        if not relative_path.startswith("/"):
            relative_path = "/" + relative_path
        url = f"{root_url}{relative_path}"
        file_short = os.path.basename(file)
        links[file_short] = url
    return links


def generate_d2lang_file(top_node, source_files, output_file, links):
    """Generate a d2lang file."""
    # import py_d2

    # shapes = []
    # connections = []
    # for file in source_files.keys():
    #     shape = py_d2.D2Shape(name=file)
    #     shapes.append(shape)
    #     for dep in source_files[file]["dependencies"]:
    #         connection = py_d2.D2Connection(shape_1=shape, shape_2=dep)
    #         connections.append(connection)

    # diagram = py_d2.D2Diagram(shapes=shapes, connections=connections)

    # with open(output_file, "w", encoding="utf-8") as f:
    #     f.write(str(diagram))

    d2_file = ""
    top_node = os.path.basename(top_node)
    d2_file += f"""title: |md
# Devicetree dependencies: {top_node}
| {{near: top-center}}
"""

    for file in source_files.keys():
        link = links[file]
        is_header = source_files[file]["type"] == "header"
        red = "red"
        green = "green"
        style = red if is_header else green
        d2_file += f"""'{file}' {{
    link: '{link}'
}}\n'{file}'.style.fill: {style}\n"""

    for file in source_files.keys():
        for dep in source_files[file]["dependencies"]:
            d2_file += f"'{file}' -> '{dep}'\n"

    d2_file += """\n
style: {
	fill: transparent
}
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(d2_file)

    # Convert
    os.system(f"D2_LAYOUT=elk d2 {output_file} {output_file}.svg")

    return f"{output_file}.svg"


def generate_page(top_node, svg_filename, output_file):
    """Generate markdown page."""

    if not os.path.exists(svg_filename):
        raise FileNotFoundError(f"File not found: {svg_filename}")

    with open(svg_filename, "r") as f:
        svg = f.read()

    page = f"""({top_node})=
# {top_node} Devicetree Map

```{{eval-rst}}
.. raw:: html
    :file: ./{svg_filename}    
```

"""

#     page = f"""# {top_node} Devicetree Map

# <div style="text-align: center;">
# {svg}
# </div>

# """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(page)


def generate_dt_graph_page(top_node, kernel_root):
    parsed_headers, parsed_dt_files = parse_devicetree_dependencies_from_file(
        top_node, kernel_root
    )

    # Determine relationships between the files
    source_files = determine_relationships(parsed_headers, parsed_dt_files, kernel_root)

    # Generate web links for all files
    links = generate_web_links(
        parsed_headers + parsed_dt_files,
        kernel_root,
        "https://github.com/analogdevicesinc/linux/blob/main/",
    )

    top_node = os.path.basename(top_node)

    # Generate a d2lang file
    d2lang_file = f"{top_node}.d2lang"
    svg_filename = generate_d2lang_file(top_node, source_files, d2lang_file, links)

    # Generate markdown page
    output_file = f"{top_node}.md"
    generate_page(top_node, svg_filename, output_file)

    return {
        "d2lang": d2lang_file,
        "svg_filename": svg_filename,
        "md": output_file,
    }

    # # Create a graph
    # G = nx.DiGraph()

    # # Add nodes
    # for file, data in source_files.items():
    #     G.add_node(file)

    # # Add edges
    # for file, data in source_files.items():
    #     for dep in data["dependencies"]:
    #         G.add_edge(file, dep)

    # # Draw the graph
    # import matplotlib.pyplot as plt
    # nx.draw(G, with_labels=True)
    # plt.show()


def parse_page_for_dt_references(text):
    """Parse a markdown page for devicetree references."""

    import re

    lines = text.split("\n")
    dt_files = []
    for line in lines:
        if ".dts" in line:
            # Find all URLs in the line
            url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
            # Find all matches
            urls = re.findall(url_pattern, line)
            for url in urls:
                if ".dts" in url:
                    tree_logger.info(f"Found DTS URL: {url}")

                    # Check branch
                    #  https://github.com/analogdevicesinc/linux/rpi-4.19.y?arch/arm/boot/dts/overlays/rpi-adxl367-overlay.dts
                    # Branch is before the first "?" so rpi-4.19.y in this case
                    if "?" in url:
                        branch = url.split("?")[0].split("/")[-1].strip()
                        tree_logger.info(f"Branch: {branch}")
                        if branch != "main":
                            tree_logger.warning(f"Branch is not main, skipping")
                            with open("failed.txt", "a") as f:
                                f.write(f"Branch is not main: {url}\n")
                            continue
                    else:
                        tree_logger.warning(f"Failed to find branch in URL: {url}")


                    dt_files.append(url)

    return dt_files


def generate_dt_graph_for_all_dts_files(text, kernel_root, output_folder="dts_graphs"):
    """Generate a devicetree graph for all dts files."""
    # Remove output folder if it exists
    all_files = []
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    dts_files = parse_page_for_dt_references(text)
    for dts_file in dts_files:
        # url to filename
        if "?" not in dts_file:
            continue
        dts_file_path = dts_file.split("?")[1]
        assert dts_file_path, "Failed to extract dts file path: {dts_file}"
        dts_file_path = os.path.join(kernel_root, dts_file_path)
        files = generate_dt_graph_page(dts_file_path, kernel_root)
        all_files.append(files)
        # Move to common folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for file in files.values():
            shutil.move(file, output_folder)

    return output_folder, all_files

def create_reference_blob_to_dt_graphs(folder, dt_graphs_folder):

    try:
        if dt_graphs_folder:
            dt_files = os.listdir(dt_graphs_folder)
            # Move to folder with driver
            if os.path.exists(os.path.join(folder, dt_graphs_folder)):
                shutil.rmtree(os.path.join(folder, dt_graphs_folder))

            shutil.move(dt_graphs_folder, folder)

            # Add links to devicetree map pages
            dt_toc = "\n\n## Devicetree Maps\n\n"

            for dt_file in dt_files:
                if not dt_file.endswith(".md"):
                    continue
                dt_file_full = os.path.join(dt_graphs_folder, dt_file)
                # [reference1](#heading-target)
                dt_toc += f"- [{dt_file}](#{dt_file.replace('.md','')})\n"

            dt_toc += "\n\n"

            # dt_toc += "\n\n```{toctree}\n"
            # dt_toc += ":maxdepth: 1\n\n"
            # dt_toc += ":caption: Example Devicetrees\n\n"
            # for dt_file in dt_files:
            #     if not dt_file.endswith(".md"):
            #         continue
            #     dt_file_full = os.path.join(dt_graphs_folder, dt_file)
            #     dt_toc += f"dt_file <{dt_file_full}>\n"
            # dt_toc += "```\n\n"

    except Exception as e:
        print(f"Failed to generate devicetree map pages: {e}")
        dt_toc = None

    return dt_toc

if __name__ == "__main__":
    # Parse the devicetree dependencies
    kernel_root = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
    dts_loc = os.path.join(kernel_root, "arch", "arm64", "boot", "dts", "xilinx")
    dts_filename = os.path.join(dts_loc, "zynqmp-zcu102-rev10-ad9081.dts")

    files = generate_dt_graph_page(dts_filename, kernel_root)
    print(files)
