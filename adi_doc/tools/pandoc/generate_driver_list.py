# Download the wiki page
import os
import subprocess
import urllib.request

import logging
logging.basicConfig(level=logging.INFO)

from fixers.fixup_wrap_tags import preprocess
from fixers.fix_all import run_all_fixers
from fixers.fix_index import fix_driver_index

# Clear failed files
files_in_dir = os.listdir()
for item in files_in_dir:
    if "failed" in item and ".txt" in item:
        logging.info(f"Removing {item}")
        os.remove(item)

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

# Parse the markdown file to get list of drivers
with open(output, "r") as f:
    text = f.read()

index_page_ref = text

lines = text.split("\n")
drivers = {}
drivers_paths = {}
count = 0
count_max = 30
target = "ADP55"
for i, line in enumerate(lines):
    if "linux-drivers/" in line:
        # if count > count_max:
        #     break
        count += 1
        driver = line.split("](")[0].split("[")[1].strip()
        link = line.split("](")[1].split(")")[0].strip()
        # if target in driver:
        drivers[driver] = link
        drivers_paths[driver] = link

if not os.path.exists("generated"):
    os.makedirs("generated")

# Create index markdown file with links to each driver
with open("generated/drivers.md", "w") as f:
    f.write("## Linux Drivers\n\n")
    for driver, link in drivers.items():
        if link[0] == "/":
            link = link[1:]
        f.write(f"- [{driver}]({link})\n")

with open("generated/drivers_index.md", "w") as f:
    f.write("## Linux Drivers Index\n\n")
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

    # if "ADXL" not in driver:
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
            # "--verbose",
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

    # skips = ["fixup_images"]
    # text = run_all_fixers(text, f"{FOLDER}/{subfolder}", skips)
    text = run_all_fixers(text, f"{FOLDER}/{subfolder}")

    # import sys
    # sys.exit(1)

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

# Make fancy index
print("\nCreating fancy index")
index_page_ref = run_all_fixers(index_page_ref , f"{FOLDER}/{subfolder}")
index_page_ref = fix_driver_index(index_page_ref)

with open("generated/drivers_index.md", "r") as f:
    ref = f.read()

index_page_ref = index_page_ref + ref
with open("generated/drivers_index.md", "w") as f:
    f.write(index_page_ref)



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
# print("\nMoving index files")
# source_folder = os.path.abspath("generated")
# drivers_index = os.path.join(source_folder, "drivers_index.md")
# target_file = os.path.abspath(os.path.join("..", "..", "source", "drivers_index.md"))
# if os.path.exists(target_file):
#     os.remove(target_file)
# shutil.move(drivers_index, target_file)

# # Move images folder
# print("\nMoving images folder")
# source_folder = os.path.abspath(os.path.join("generated", "images"))
# target_folder = os.path.abspath(os.path.join("..", "..", "source", "_static", "images"))
# if os.path.exists(target_folder):
#     shutil.rmtree(target_folder)
# shutil.move(source_folder, target_folder)