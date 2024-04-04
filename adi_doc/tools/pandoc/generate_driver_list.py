# Download the wiki page
import urllib.request
from fixup_wrap_tags import process, preprocess
import os

TARGET = "https://wiki.analog.com/resources/tools-software/linux-drivers-all"

with urllib.request.urlopen(f"{TARGET}?do=export_raw") as f:
    dokuwiki = f.read().decode("utf-8")

input = "linux-drivers-all.dokuwiki"
with open(input, "w") as f:
    f.write(dokuwiki)

# Pass through pandoc to convert to markdown
output = "linux-drivers-all.md"
import subprocess

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
        f.write(f"- [{driver}]({link})\n")

# Download doc pages for each driver
FOLDER = "generated/drivers"
ROOT = "https://wiki.analog.com/resources/tools-software/"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

for driver, link in drivers.items():

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
            "--wrap=preserve",
            # "--verbose",
            "-f",
            "dokuwiki",
            "-t",
            "markdown",
            "-o",
            output,
            input,
        ]
    )

    # Fix up the markdown file
    print(f"Fixing up {output}")
    with open(output, "r") as f:
        text = f.read()

    try:
        preprocess(text)
    except Exception as e:
        print(f"Failed to preprocess {driver}: {e}")
        with open('failed.txt', 'a') as f:
            f.write(f"PP: {driver}: {ROOT}{link}\n")
        os.remove(input)
        continue
    text = process(text)

    with open(output, "w") as f:
        f.write(text)

    # break
    import time
    time.sleep(1)