"""The purpose of this module is to parse markdown files for graphviz tags and 
process them accordingly. The graphviz tags are used to create diagrams in the
documentation."""

import sys
import re
from bs4 import BeautifulSoup


def update_graphviz_blocks(text):
    """Replace all graphviz tags with admonition tags"""

    def replace_first_tag_found(text, retag, is_end_tag):
        wrap_tag_locations = [(m.start(), m.end()) for m in re.finditer(retag, text)]
        # Only handle the first tag found
        if not wrap_tag_locations:
            return text, False
        tag_text = text[wrap_tag_locations[0][0]:wrap_tag_locations[0][1]]
        # print("Tag text: ", tag_text)
        if not is_end_tag:
            # Parse the tag text to determine the type of admonition
            soup = BeautifulSoup(tag_text, "html.parser")
            tag = soup.find()
            # print("Tag name: ", tag.name)
            # print("Tag attrs: ", tag.attrs)
            attrs_as_string = " ".join([f'{key}="{value}"' for key, value in tag.attrs.items()])
            # Replace the tag with the appropriate admonition tag
            if "graphviz" in tag_text:
                replacement = f"<!-- ATTRS: {attrs_as_string} -->\n" + "```{graphviz} "
            else:
                raise Exception("Unknown tag found")
        else:
            replacement = "\n```\n"

        text = text[:wrap_tag_locations[0][0]] + replacement + text[wrap_tag_locations[0][1]:]
        return text, True


    def replace(text, tag, is_end_tag=False):
        while True:
            text, found = replace_first_tag_found(text, tag, is_end_tag)
            if not found:
                break
        return text

    # Replace Tags
    text = replace(text, r"\\<graphviz.*?>")
    text = replace(text, r"\\</graphviz.*?>", True)

    # Remove all backslashes between the graphviz tags
    def replace_backslashes(text):
        while True:
            backslash_locations = [(m.start(), m.end()) for m in re.finditer(r"\\", text)]
            if not backslash_locations:
                break
            text = text[:backslash_locations[0][0]] + text[backslash_locations[0][1]:]
        return text
    
    text = replace_backslashes(text)

    return text
