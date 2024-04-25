"""This module fixes short links to the wiki"""
import re
import logging

sl_logger = logging.getLogger("fix_short_links")


def update_link(link, mapping, full, text, link_text):

    if ">" in link:
        # Verify characters after >
        link = link.strip()

        pieces = link.split(">")
        if link.count(">") > 1:
            sl_logger.warning(f"TOO MANY >: {full}")
            with open("failed_unknown_refs.txt", "a") as f:
                f.write(f"TOO MANY >: {full}\n")
            return text

        if len(pieces) == 1:
            ref, short_link = pieces[0], ""
        else:
            ref, short_link = pieces
        if ref not in mapping:
            # raise ValueError(f"Unknown reference: {ref}")
            sl_logger.warning(f"UNKNOWN REF KEY: {ref} | {full}")
            with open("failed_unknown_refs.txt", "a") as f:
                f.write(f"UNKOWN REF KEY: {ref} | {full}\n")
            return text

        sl_logger.info(f"MAPPING: {ref} -> {mapping[ref]}")

        # Create full link
        if short_link:
            if short_link.startswith("/"):
                short_link = short_link[1:]
            short_link = short_link.strip()
        full_link = f"https://{mapping[ref]}/{short_link}"

        text = text.replace(full, f"[{link_text}]({full_link})")
    else:
        sl_logger.info("no > found")
        sl_logger.info(link)

    sl_logger.info("-----------------")

    return text


def fix_short_links(text):

    # Short links are of the form:
    # [link text](ref>short_link)

    mapping = {
        "ez": "ez.analog.com",
        "wiki": "wiki.analog.com",
        "adi": "analog.com",
        "linux.github": "github.com/analogdevicesinc/linux",
        "git.linux.org": "git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree",
        "youtube": "youtube.com",
        "maxim": "maximintegrated.com",
    }

    # Parse the link text, ref, and short_link
    links_parts = {}
    for match in re.finditer(r"\[.*\]\((.*)\)", text):
        sl_logger.info("#" * 10)
        # print(f"Full: {match.group(0)}")
        full = match.group(0)
        link_text = full.split("](")[0].split("[")[1]
        link = match.group(1)

        if "scrape>adi>" in link:
            with open("failed_unknown_refs.txt", "a") as f:
                f.write(f"Scrape link: {full}\n")
            continue

        # Handle multiple links per line
        if full.count(">") > 1:
            sl_logger.info("Multiple > found")
            sl_logger.info("Pre parse RAW full: ", full)
            # Get locations of all ) characters that follow a ] character
            end_of_links = []
            within_the_text_part = False
            for i in range(len(full)):
                if full[i] == "[":
                    within_the_text_part = True
                if full[i] == "]":
                    within_the_text_part = False
                if full[i] == ")":
                    if not within_the_text_part:
                        end_of_links.append(i)

            assert (
                len(end_of_links) > 1
            ), f"Not enough > characters in link, Got: {end_of_links}"

            last_char = full.index("[")
            for end_char_loc in end_of_links:

                full_instance = full[last_char : end_char_loc + 1]
                sl_logger.info(f"Full Instance: {full_instance}")
                try:
                    link_text_instance = full_instance.split("](")[0].split("[")[1]
                    link_instance = full_instance.split("](")[1].split(")")[0]
                except IndexError:
                    sl_logger.warning(f"Likely not a link: {full_instance}")
                    continue
                sl_logger.info(f"Link Instance: {link_instance}")
                sl_logger.info(f"Link Text Instance: {link_text_instance}")

                try:
                    last_char = full.index("[", end_char_loc)
                except ValueError:
                    break  # No more links

                text = update_link(
                    link_instance, mapping, full_instance, text, link_text_instance
                )

        else:
            sl_logger.info("Singleton link found")
            sl_logger.info("Pre parse RAW full: " + str(full))
            text = update_link(link, mapping, full, text, link_text)

    # Fix tables which are raw HTML
    # text = text.replace("linux.github&gt;", mapping["linux.github"]+"/")
    text = text.replace(
        "linux.github&gt;", "https://github.com/analogdevicesinc/linux/"
    )

    # master to main
    text = text.replace("analogdevicesinc/linux/master", "analogdevicesinc/linux/main")

    # Fix old/broken names
    org = "linux/master?"
    new = "linux/main?"
    text = text.replace(org, new)

    return text
