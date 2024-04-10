# Download the wiki page
import os
import subprocess
import urllib.request

from fixers.fixup_wrap_tags import preprocess, process
from fixers.heading_fixup import adjust_heading
from fixers.fixup_term_tags import update_xterm_blocks
from fixers.fixup_graphviz_tags import update_graphviz_blocks

# Check if running on linux
if os.name != "posix":
    print("This script is only supported on Linux")
    exit(1)

TARGET = "https://wiki.analog.com/resources/tools-software/linux-drivers-all"

with urllib.request.urlopen(f"{TARGET}?do=export_raw") as f:
    dokuwiki = f.read().decode("utf-8")

input = "linux-drivers-all.dokuwiki"
with open(input, "w") as f:
    f.write(dokuwiki)

# Pass through pandoc to convert to markdown
output = "linux-drivers-all.md"

subprocess.run(
    [
        "pandoc",
        "-L",
        "adi_wiki.lua",
        "--wrap=preserve",
        "--verbose",
        "-f",
        "dokuwiki",
        "-t",
        "markdown",
        "-o",
        output,
        input,
    ]
)

# Parse the markdown file to get list of drivers
with open(output, "r") as f:
    text = f.read()

lines = text.split("\n")
drivers = {}
drivers_paths = {}
for line in lines:
    if "linux-drivers/" in line:
        driver = line.split("](")[0].split("[")[1].strip()
        link = line.split("](")[1].split(")")[0].strip()
        drivers[driver] = link
        drivers_paths[driver] = link

if not os.path.exists("generated"):
    os.makedirs("generated")

# Create index markdown file with links to each driver
with open("generated/drivers.md", "w") as f:
    f.write("# Linux Drivers\n\n")
    for driver, link in drivers.items():
        if link[0] == "/":
            link = link[1:]
        f.write(f"- [{driver}]({link})\n")

with open("generated/drivers_index.md", "w") as f:
    f.write("# Linux Drivers\n\n")
    f.write("::: {toctree}\n")
    f.write(":maxdepth: 1\n\n")
    written = []
    for driver, link in drivers.items():
        if link[0] == "/":
            link = link[1:]
        if link in written:
            continue
        if "Fan Control IP core" in driver:
            driver = "Fan Control IP"
        else:
            parts = ["AD", "LTC", "HMC", "SSM", "MAX"]
            found = False
            part = None
            for p in parts:
                if p in driver:
                    found = True
                    for sec in driver.split(' '):
                        if p in sec:
                            part = sec
                            part = part.replace(':','')
                            break
            if part:
                driver = part
        f.write(f"{driver} <drivers/{link}>\n")
        written.append(link)
    f.write(":::\n")

# Download doc pages for each driver
FOLDER = "generated/drivers"
ROOT = "https://wiki.analog.com/resources/tools-software/"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

for driver, link in drivers.items():

    # if "ADP5501" not in driver:
    #     continue

    print('---------------------------------------')
    print(f"Downloading {driver} from {ROOT}{link}")

    driver_short_name = link.split("/")[-1]
    input = f"{driver_short_name}.dokuwiki"
    input = f"{FOLDER}/{input}"

    if not os.path.exists(input):
        try:
            with urllib.request.urlopen(f"{ROOT}{link}?do=export_raw") as f:
                dokuwiki = f.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            print(f"Failed to download {driver} from {ROOT}{link}")
            with open('failed.txt', 'a') as f:
                f.write(f"DL: {driver}: {ROOT}{link}\n")
            continue
        with open(input, "w") as f:
            f.write(dokuwiki)
    else:
        print(f"Skipping {driver} download as file already exists")


    # Pass through pandoc to convert to markdown
    output = f"{driver_short_name}.md"
    if link[0] == "/":
        link = link[1:]
    subfolder_from_link = link.split("/")[:-1]
    subfolder = "/".join(subfolder_from_link)
    if not os.path.exists(f"{FOLDER}/{subfolder}"):
        os.makedirs(f"{FOLDER}/{subfolder}")
    output = f"{FOLDER}/{subfolder}/{output}"
    subprocess.run(
        [
            "pandoc",
            "-L",
            "adi_wiki.lua",
            "-L",
            "adi_wiki_drivers.lua",
            "--wrap=preserve",
            "--verbose",
            "-f",
            "dokuwiki",
            "-t",
            # "markdown",
            "markdown-pipe_tables-simple_tables-multiline_tables-grid_tables",
            "-o",
            output,
            input,
        ]
    )

    # Fix up the markdown file
    try:
        print(f"Fixing up {output}")
        with open(output, "r") as f:
            text = f.read()
    except Exception as e:
        print(f"Failed to open {output}: {e}")
        with open('failed.txt', 'a') as f:
            f.write(f"PANDOC: {driver}: {ROOT}{link}\n")
        continue

    try:
        preprocess(text)
    except Exception as e:
        print(f"Failed to preprocess {driver}: {e}")
        with open('failed.txt', 'a') as f:
            f.write(f"PP: {driver}: {ROOT}{link}\n")
        os.remove(input)
        continue
    text = process(text)

    text = adjust_heading(text)

    text = update_xterm_blocks(text)

    text = update_graphviz_blocks(text)

    # Add metadata
    text = f"""---
wiki-source: {ROOT}{link}
title: {driver}
---

""" + text

    with open(output, "w") as f:
        f.write(text)

    # break
    import time

    # time.sleep(0.1)

print("Done, check failed.txt for any failed downloads or processing")

# Move to sphinx source directory
print("\nMoving files to sphinx source directory")
import shutil

source_folder = os.path.abspath("generated")
source_folder = os.path.join(source_folder, "drivers", )
target_folder = os.path.abspath(os.path.join("..", "..", "source", "drivers"))
for folder in os.listdir(source_folder):
    source = os.path.join(source_folder, folder)
    target = os.path.join(target_folder, folder)
    if os.path.isfile(source):
        continue
    if os.path.exists(target):
        print(f"Remove {target}")
        shutil.rmtree(target)
    print(f"Move {source} to {target}")
    shutil.move(source, target)

# Move index files
print("\nMoving index files")
source_folder = os.path.abspath("generated")
drivers_index = os.path.join(source_folder, "drivers_index.md")
target_file = os.path.abspath(os.path.join("..", "..", "source", "drivers_index.md"))
if os.path.exists(target_file):
    os.remove(target_file)
shutil.move(drivers_index, target_file)
