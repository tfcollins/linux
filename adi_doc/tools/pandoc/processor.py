"""Parse and process WRAP/wrap tags from converted dokuwiki files"""
import sys
import re
from bs4 import BeautifulSoup


def handle_wrap_braces(text):
    # Find all tag pairs of form <tag> and </tag> which may be nested
    # and provide the text between the tags to the processor
    # The processor should return the modified text

    # <WRAP> and </WRAP> tag locations
    wrap_tag_locations = [(m.start(), m.end()) for m in re.finditer(r"<WRAP.*?>", text)]
    wrap_tag_locations_start = [start for start, end in wrap_tag_locations]
    wrap_end_tag_locations = [
        (m.start(), m.end()) for m in re.finditer(r"</WRAP>", text)
    ]
    wrap_end_tag_locations_start = [start for start, end in wrap_end_tag_locations]

    soup = BeautifulSoup(text, "html.parser")
    tags = soup.find_all()
    for tag in tags:
        print(tag.name)

    return tags

    return text

    def find_end_tag(start_tag_location):
        for end_start, end_end in wrap_end_tag_locations:
            if end_start > start_tag_location:
                return end_end
        raise Exception(
            "No end tag found for start tag at location {}".format(start_tag_location)
        )

    def find_next_start_tag(end_tag_location):
        for start in wrap_tag_locations_start:
            if start > end_tag_location:
                return start
        return None

    # Find the corresponding end tag for each start tag
    wrap_tag_pairs_locations = []
    for start in wrap_tag_locations_start:
        end = find_end_tag(start)
        # Check if another start tag is present before the end tag
        next_start = find_next_start_tag(start)
        if next_start is not None or next_start > end:
            ...
        else:
            ...
            # Found a nested tag


def run_all_processors(text):
    text = handle_wrap_braces(text)
    return text


if __name__ == "__main__":

    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
    with open(in_filename, "r") as f:
        text = f.read()

    # text = run_all_processors(text)

    # def update_wrap_tag_with_box(text):

    def update_wrap_tag(
        text, start_tag, end_tag_with_braces, replacement_text, require_attrs
    ):

        soup = BeautifulSoup(text, "html.parser")
        tags = soup.find_all(start_tag)

        for tag in tags:
            start_line = tag.sourceline
            start_pos = tag.sourcepos

            # Determine the character position in the string as a whole
            char_count = 0
            for i, l in enumerate(text.split("\n")):
                if i < start_line - 1:
                    char_count += len(l) + 1
                elif i == start_line - 1:
                    char_count += start_pos
                    break

            attrs = list(tag.attrs.keys())
            all_found = True
            for attr in require_attrs:
                if attr not in attrs:
                    all_found = False
                    break

            if len(attrs) == len(require_attrs) and all_found:
                s = tag.text.replace("\n", " ")
                s = s.replace("  ", " ")
                if "This specifies any shell prompt running on the target" in s:

                    print("FOUND")
                    print(f"|{s}|")
                    print("-------------------------")
                    ## Replace the tag block
                    # Find location of next </wrap> tag
                    next_wrap_tag = text.find(end_tag_with_braces, char_count) + len(
                        end_tag_with_braces
                    )

                    print(f"Line: |{text[char_count:next_wrap_tag]}|")

                    text = text[:char_count] + replacement_text + text[next_wrap_tag:]

                    return True, text

        return False, text

    replacement_text = """

.. NOTE::

   This specifies any shell prompt running on the target.

"""
    start_tag = "wrap"
    end_tag_with_braces = "</wrap>"

    found = True
    while found:
        found, text = update_wrap_tag(
            text, start_tag, end_tag_with_braces, replacement_text, ["info"]
        )

    ##############
        
    # Find all instances of <WRAP box bggreen> and </WRAP> and replace with a note
    # indenting the text inside the box
    
    
        
    


    with open(out_filename, "w") as f:
        f.write(text)
