"""This modules fixes included dependent pages or page sections"""

import os
import re
import sys
import shutil
import subprocess
import requests
from urllib.parse import urlparse
import logging

from .fix_all import run_all_fixers

fi_logger = logging.getLogger("fix_includes")

def fix_includes(text, target_dir=None):

    # Page includes are of the form:
    # ![attr](page>page_path#name&of&section)
    # We need to download the page and use include directive to include it

    # Parse the text for includes
    includes = {}
    for match in re.finditer(r"!\[.*\]\((.*)\)", text):
        full = match.group(0)
        include = match.group(1)
        if "page>" in include:
            _, path = include.split("page>")
            if "#" in path:
                path, section = path.split("#")
                # Process section
                sections = section.split("&")
                section = sections[0]
                cmds = sections[1:]
            else:
                section = None
                cmds = []
            includes[include] = {"path": path, "section": section, "cmds": cmds, "full": full}

            fi_logger.info(f"Found include: {include}")

    if not includes:
        fi_logger.info("No includes found")
        return text


    # Download the pages
    for include in includes:
        path = includes[include]["path"]
        section = includes[include]["section"]

        # Check if the file already exists
        if os.path.exists(path):
            fi_logger.info(f"File {path} found. Not downloading")
        else:
            fi_logger.info(f"Downloading {path} to {target_dir}")
            if path[0] == "/":
                path = path[1:]
            url = f"https://wiki.analog.com/{path}?do=export_raw"
            response = requests.get(url)
            if response.status_code != 200:
                fi_logger.error(f"Failed to download {url}: {response.status_code}")
                with open("failed_includes.txt", "a") as f:
                    f.write(f"INCLUDE {path}: {url}\n")
                continue
            # Do download
            filename = path.replace("/", "_")
            if section:
                filename = f"{filename}_SUB_{section.replace(' ', '_')}"
            filename = f"{filename}.dokuwiki"
            full_path = os.path.join(target_dir, filename)
            with open(full_path, "wb") as f:
                f.write(response.content)
            fi_logger.info(f"Downloaded {path} to {full_path}")

            # Do subpage conversion
            subprocess.run(
                [
                    "pandoc",
                    "--wrap=preserve",
                    "--from=dokuwiki",
                    "--to=markdown-pipe_tables-simple_tables-multiline_tables-grid_tables",
                    full_path,
                    "-o",
                    full_path.replace(".dokuwiki", ".md"),
                ]
            )
            # check if file exists
            if not os.path.exists(full_path.replace(".dokuwiki", ".md")):
                fi_logger.error(f"Failed to convert {full_path} to markdown")
                with open("failed_includes.txt", "a") as f:
                    f.write(f"CONVERT {path}: {url}\n")
                continue
            else:
                # Remove the dokuwiki file
                os.remove(full_path)

            # Parse generated markdown file

            # Extract the section
            if section:
                with open(full_path.replace(".dokuwiki", ".md"), "r") as f:
                    include_text = f.read()

                # Extract the section
                section_text = []
                found = False
                level = 0
                noheader = "noheader" in includes[include]["cmds"]
                    
                for line in include_text.splitlines():
                    if not found:
                        section_with_spaces = section.replace("_", " ")
                        if line.startswith(f"# {section}") or line.startswith(f"# {section_with_spaces}"):
                            found = True
                            if not noheader:
                                section_text.append(line)
                            level = line.count("#")
                    else:
                        if "#" in line and line.count("#") <= level:
                            break
                        section_text.append(line)
                    
                include_text = "\n".join(section_text)

                fi_logger.info(f"Extracted section |{section}| from {full_path}")
                fi_logger.info("\nTEXT:\n"+include_text+"\n--------\n")

                if include_text:
                    with open(full_path.replace(".dokuwiki", ".md"), "w") as f:
                        f.write(include_text)
                else:
                    fi_logger.error(f"Failed to extract section |{section}| from {full_path}")
                    continue

            # Post process new file
            with open(full_path.replace(".dokuwiki", ".md"), "r") as f:
                include_text = f.read()

            # Check for nested includes
            if "page>" in include_text:
                raise Exception(f"Nested includes found in {full_path.replace('.dokuwiki', '.md')}")

            # Fixup the include text
            to_skip = ["fix_includes", "adjust_heading"]
            include_text = run_all_fixers(include_text, target_dir, to_skip)

            with open(full_path.replace(".dokuwiki", ".md"), "w") as f:
                f.write(include_text)

        # Replace the include in the text
        replacement = "```{include} "+filename.replace(".dokuwiki", ".md")+"\n```"
        cmds = includes[include]["cmds"]
        if cmds:
            replacement = f"<!-- CMDS: {' '.join(cmds)} -->\n{replacement}"
        text = text.replace(includes[include]["full"], replacement)

    return text

