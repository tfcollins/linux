"""This module fixes short links to the wiki"""
import re


def fix_short_links(text):

    # Short links are of the form:
    # [link text](ref>short_link)

    mapping = {
        "ez": "ez.analog.com",
        "wiki": "wiki.analog.com",
        "adi": "analog.com",
        "linux.github": "github.com/analogdevicesinc/linux",
        "git.linux.org": "git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree",
    }

    # Parse the link text, ref, and short_link
    links_parts = {}
    for match in re.finditer(r"\[.*\]\((.*)\)", text):
        full = match.group(0)
        link_text = full.split("](")[0].split("[")[1]
        link = match.group(1)
        if ">" in link:
            # Verify characters after >
            link = link.strip()

            pieces = link.split(">")
            if link.count(">") > 1:
                with open("failed_unknown_refs.txt", "a") as f:
                    f.write(f"TOO MANY >: {full}\n")
                continue

            if len(pieces) == 1:
                ref, short_link = pieces[0], ""
            else:
                ref, short_link = pieces
            if ref not in mapping:
                raise ValueError(f"Unknown reference: {ref}")
                with open("failed_unknown_refs.txt", "a") as f:
                    f.write(f"UNKOWN REF KEY: {ref} | {full}\n")
                continue
            # Create full link
            if short_link:
                if short_link.startswith("/"):
                    short_link = short_link[1:]
                short_link = short_link.strip()
            full_link = f"https://{mapping[ref]}/{short_link}"

            text = text.replace(full, f"[{link_text}]({full_link})")

    return text
