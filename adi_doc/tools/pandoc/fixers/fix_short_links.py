"""This module fixes short links to the wiki"""
import re

def update_link(link, mapping, full, text, link_text):

        if ">" in link:
            # Verify characters after >
            link = link.strip()

            pieces = link.split(">")
            if link.count(">") > 1:
                print(f"TOO MANY >: {full}")
                with open("failed_unknown_refs.txt", "a") as f:
                    f.write(f"TOO MANY >: {full}\n")
                return text

            if len(pieces) == 1:
                ref, short_link = pieces[0], ""
            else:
                ref, short_link = pieces
            if ref not in mapping:
                # raise ValueError(f"Unknown reference: {ref}")
                print(f"UNKNOWN REF KEY: {ref} | {full}")
                with open("failed_unknown_refs.txt", "a") as f:
                    f.write(f"UNKOWN REF KEY: {ref} | {full}\n")
                return text

            print(f"MAPPING: {ref} -> {mapping[ref]}")

            # Create full link
            if short_link:
                if short_link.startswith("/"):
                    short_link = short_link[1:]
                short_link = short_link.strip()
            full_link = f"https://{mapping[ref]}/{short_link}"

            text = text.replace(full, f"[{link_text}]({full_link})")
        else:
            print("no > found")
            print(link)

        print('-----------------')

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
        print('#'*10)
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
            print('Multiple > found')
            print("Pre parse RAW full: ", full)
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


            assert len(end_of_links) > 1, f'Not enough > characters in link, Got: {end_of_links}'

            last_char = full.index("[")
            for end_char_loc in end_of_links:

                full_instance = full[last_char:end_char_loc+1]
                print(f"Full Instance: {full_instance}")
                try:
                    link_text_instance = full_instance.split("](")[0].split("[")[1]
                    link_instance = full_instance.split("](")[1].split(")")[0]
                except IndexError:
                    print(f'Likely not a link: {full_instance}')
                    continue
                print(f"Link Instance: {link_instance}")
                print(f"Link Text Instance: {link_text_instance}")

                try:
                    last_char = full.index("[", end_char_loc)
                except ValueError:
                    break # No more links

                text = update_link(link_instance, mapping, full_instance, text, link_text_instance)

        else:
            print("Singleton link found")
            print("Pre parse RAW full: ", full)
            text = update_link(link, mapping, full, text, link_text)



    return text
