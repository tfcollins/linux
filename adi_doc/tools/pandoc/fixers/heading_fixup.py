import re


def adjust_heading(text):
    # Find all headings
    headings = re.findall(r"^(#+)(.*)$", text, re.MULTILINE)

    level_1_headings = 0
    first_level_1_heading = None
    for i, heading in enumerate(headings):
        level = len(heading[0])
        title = heading[1].strip()
        if title:
            if not level_1_headings and level == 1:
                first_level_1_heading = i
            if level == 1:
                level_1_headings += 1

    if first_level_1_heading == 0 and level_1_headings == 1:
        # Doc is fine, return as is
        return text

    for i, heading in enumerate(headings):
        level = len(heading[0])
        title = heading[1].strip()
        if title:
            # Adjust heading level
            if i == 0:
                level = 1
            else:
                level = level + 1
            # Adjust heading title
            text = text.replace(heading[0] + heading[1], "#" * level + " " + title)

    return text
