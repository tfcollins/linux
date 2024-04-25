"""The purpose of this module is to parse markdown files for WRAP/wrap tags and 
process them accordingly. These tags are generally used as admonitions"""

import sys
import re
from bs4 import BeautifulSoup


def preprocess(text):
    """First verify that the wrap tags are not nested beyond two levels"""

    # <WRAP> and </WRAP> tag locations
    wrap_tag_locations = [(m.start(), m.end()) for m in re.finditer(r"<WRAP.*?>", text)]
    wrap_lc_tag_locations = [
        (m.start(), m.end()) for m in re.finditer(r"<wrap.*?>", text)
    ]

    wrap_tag_locations_start = [start for start, end in wrap_tag_locations]
    wrap_lc_tag_locations_start = [start for start, end in wrap_lc_tag_locations]

    wrap_end_tag_locations = [
        (m.start(), m.end()) for m in re.finditer(r"</WRAP.*?>", text)
    ]
    wrap_end_lc_tag_locations = [
        (m.start(), m.end()) for m in re.finditer(r"</wrap.*?>", text)
    ]

    wrap_end_tag_locations_start = [start for start, end in wrap_end_tag_locations]
    wrap_end_lc_tag_locations_start = [
        start for start, end in wrap_end_lc_tag_locations
    ]

    def find_next_start_tag(start, wrap_tag_locations_start):
        for next_start in wrap_tag_locations_start:
            if next_start > start:
                return next_start
        return None

    def find_next_end_tag(start, wrap_end_tag_locations):
        for next_end in wrap_end_tag_locations:
            if next_end > start:
                return next_end
        return None

    if wrap_tag_locations_start:
        # Verify WRAP tags are not nested
        for start in wrap_tag_locations_start:
            next_start = find_next_start_tag(start, wrap_tag_locations_start)
            next_end = find_next_end_tag(start, wrap_end_tag_locations_start)
            if next_start is not None and next_start < next_end:
                raise Exception("Nested WRAP tags are not allowed")

    if wrap_lc_tag_locations_start:
        # Verify wrap tags are not nested
        for start in wrap_lc_tag_locations_start:
            next_start = find_next_start_tag(start, wrap_lc_tag_locations_start)
            next_end = find_next_end_tag(start, wrap_end_lc_tag_locations_start)
            if next_start is not None and next_start < next_end:
                raise Exception("Nested wrap tags are not allowed")

    # This is ok now
    # # Verify WRAP and wrap tags are not nested
    # for start in wrap_tag_locations_start:
    #     next_end = find_next_start_tag(start, wrap_end_tag_locations_start)
    #     next_lc_start = find_next_start_tag(start, wrap_lc_tag_locations_start)
    #     if next_end > next_lc_start:
    #         error_text = text[start:next_end+len("</WRAP>")]
    #         print(error_text)
    #         raise Exception("Nested WRAP and wrap tags are not allowed")

    # Verify there are not multiple nested tags


def process(text):
    """Replace all WRAP tags with admonition tags"""

    def replace_first_tag_found(text, retag, is_end_tag):
        wrap_tag_locations = [(m.start(), m.end()) for m in re.finditer(retag, text)]
        # Only handle the first tag found
        if not wrap_tag_locations:
            return text, False
        tag_text = text[wrap_tag_locations[0][0] : wrap_tag_locations[0][1]]
        # print("Tag text: ", tag_text)
        if not is_end_tag:
            # Parse the tag text to determine the type of admonition
            soup = BeautifulSoup(tag_text, "html.parser")
            tag = soup.find()
            # print("Tag name: ", tag.name)
            # print("Tag attrs: ", tag.attrs)
            attrs_as_string = " ".join(
                [f'{key}="{value}"' for key, value in tag.attrs.items()]
            )
            # Replace the tag with the appropriate admonition tag
            if "WRAP" in tag_text:
                replacement = ":::{NOTE} " + f"<!-- ATTRS: {attrs_as_string} -->\n"
            elif "wrap" in tag_text:
                replacement = ":::{HINT} " + f"<!-- ATTRS: {attrs_as_string} -->\n"
            else:
                raise Exception("Unknown tag found")
        else:
            replacement = "\n:::\n"

        text = (
            text[: wrap_tag_locations[0][0]]
            + replacement
            + text[wrap_tag_locations[0][1] :]
        )
        return text, True

    def replace(text, tag, is_end_tag=False):
        while True:
            text, found = replace_first_tag_found(text, tag, is_end_tag)
            if not found:
                break
        return text

    text = replace(text, r"\\<WRAP.*?>")
    text = replace(text, r"\\<wrap.*?>")
    text = replace(text, r"\\</WRAP.*?>", True)
    text = replace(text, r"\\</wrap.*?>", True)

    return text


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        text = f.read()
    print("Preprocessing...")
    preprocess(text)
    print("Preprocessing complete")
    print("Processing...")
    text = process(text)
    print("Processing complete")
    with open(sys.argv[2], "w") as f:
        f.write(text)
