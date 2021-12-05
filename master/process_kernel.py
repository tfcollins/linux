"""Generate MD pages for DT yaml files"""
import glob
from jinja2 import Environment, FileSystemLoader
import yaml
import os


def test_yaml(filename):
    try:
        with open(filename, "r") as stream:
            data = yaml.safe_load(stream)
        return True
    except:
        return False


def generate_md_files(kernel_root_dir, stop_bad_yaml=False):

    if not os.path.isdir(kernel_root_dir):
        raise Exception(f"{kernel_root_dir} not a directory")

    path = os.path.join(
        kernel_root_dir, "Documentation/devicetree/bindings/iio/**/*.yaml"
    )
    print(path)
    files = glob.glob(path)
    filenames = []

    for file in files:
        if "adi," in file:
            if not test_yaml(file):
                if stop_bad_yaml:
                    raise Exception(f"Invalid yaml file found: {file}")
                print(f"BAD YAML: {file}")
                continue
            filename = file.split("/")[-1]
            filename = filename.replace(",", "_").replace("yaml", "md")
            filename = filename.upper()
            filename = filename.replace(".MD", ".md")
            with open(f"docs/devs/{filename}", "w") as f:
                cmd = f"\n\n::: linux:{file}"
                f.write(cmd)
            filenames.append(filename)

    return filenames


def create_mkdocs_yml(filenames):

    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    template = env.get_template("temp.yml")

    output = template.render(devs=filenames)

    with open("mkdocs.yml", "w") as f:
        f.write(output)


def default():
    fns = generate_md_files("/tmp/linux")
    create_mkdocs_yml(fns)


if __name__ == "__main__":
    default()