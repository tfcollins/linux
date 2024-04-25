"""This module will parse markdownfiles for picture links, download the pictures
 and fix the links to point to the local files."""

import os
import re
import shutil
import sys
import time
import requests
from urllib.parse import urlparse
import logging

fi_logger = logging.getLogger("fixup_images")

here = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(here, "known_bad_images.txt"), "r") as f:
    known_bad_images = f.readlines()
    known_bad_images = [x.strip().replace("\n", "") for x in known_bad_images]


def download_image(url, output):
    """Download an image from a URL to a file."""
    import requests

    if url in known_bad_images:
        fi_logger.warning(f"Skipping known bad image {url}")
        return False

    fi_logger.info(f"Skipping download of {url} to {output}")
    # with open(os.path.join(here, "known_bad_images.txt"), "a") as f:
    #     f.write(f"{url}\n")
    # return False

    assert False, "SHOULD NOT DOWNLOAD IMAGES"

    # Download the image
    try:
        # response = requests.get(url)
        # Get url with timeout
        # response = requests.get(url, timeout=5)
        retries = 3
        for i in range(retries):
            try:
                response = requests.get(url, timeout=5)
                break
            except requests.exceptions.RequestException as e:
                fi_logger.warning(f"Failed to download {url}: {e}")
                time.sleep(5)
                if i == retries - 1:
                    return False
        if response.status_code != 200:
            fi_logger.warning(f"Failed to download {url}: {response.status_code}")
            return False

        # Save the image
        with open(output, "wb") as f:
            f.write(response.content)
    except Exception as e:
        fi_logger.warning(f"Failed to download {url}: {e}")
        return False

    return True


def get_link(url, image, target_dir, text, ref_image):
    filename = os.path.basename(urlparse(url).path)
    output = os.path.join(target_dir, filename)
    if not os.path.exists(output):
        fi_logger.info(f"Downloading {url} to {output}")
        result = download_image(url, output)
        if not result:
            fi_logger.warning(f"Failed to download {url}")
            with open("failed_images.txt", "a") as f:
                f.write(f"{image}: {url}\n")
            return None
    else:
        fi_logger.info(f"Skipping {url} to {output}. File already exists.")

    # Fix the image link
    text = text.replace(ref_image, f"images/{filename}")
    return text


def fixup_images(text, target_dir):

    fi_logger.info("---------------------------------------")

    # Parse the text for image links
    images = []
    descriptions = []
    for match in re.finditer(r"!\[.*\]\((.*)\)", text):
        descriptions.append(match.group(0))
        images.append(match.group(1))

    target_dir = os.path.join(target_dir, "images")

    # Download the images
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for image in images:

        ref_image = image
        # Skip local images
        # print(f"Processing image {image} | {descriptions[images.index(image)]}")
        fi_logger.info(f"Processing image {image}")

        # Check for file extension in URL
        if not image.endswith((".jpg", ".png", ".gif", ".jpeg", ".bmp", ".svg")):
            fi_logger.warning(f"Skipping image {image}. Not a valid image file.")
            continue

        if image.startswith("http"):
            url = image
        else:
            # likely a relative link
            if ">" in image:
                image = image.split(">")[1].strip()
            if "/" == image[0]:
                image = "_media" + image
            # https://wiki.analog.com/_media/software/driver/linux/adp5520_brd.jpg?cache=&w=900&h=683&tok=3ae9ee
            guess = f"https://wiki.analog.com/{image}"
            # See if link is valid
            try:
                response = requests.options(guess)
                if response.ok:
                    url = guess
                else:
                    fi_logger.warning(f"Failed to find image {guess}")
                    with open("failed_images.txt", "a") as f:
                        f.write(f"{image}: {guess}\n")
                    continue
            except Exception as e:
                fi_logger.warning(f"Failed to find image {guess}: {e}")
                with open("failed_images.txt", "a") as f:
                    f.write(f"{image}: {guess}\n")
                continue

        nt = get_link(url, image, target_dir, text, ref_image)
        if nt:
            text = nt

    # Convert image links of form:
    # ![ADP5520 Demo Mother/Daughter Board](images/adp5520_brd.jpg){width="800" query="?800"}
    # to:
    # ```{image} images/adp5520_brd.jpg
    # :alt: ADP5520 Demo Mother/Daughter Board
    # :width: 800
    # :query: ?800
    # ```

    for match in re.finditer(r"!\[.*\]\((.*)\)\{(.*)\}", text):
        alt = match.group(0).split("](")[0].split("[")[1]
        image = match.group(1)
        attributes = match.group(2)
        if not attributes:
            continue

        new_format = f"```{{image}} {image}\n"
        new_format += f":alt: {alt}\n"
        fi_logger.info(f"Attributes: {attributes}")
        fi_logger.info(f"Attributes Split: {attributes.split()}")
        for attribute in attributes.split():
            if "=" not in attribute:
                new_format += f":{attribute}\n"
            else:
                new_format += f":{attribute.split('=')[0]}: {attribute.split('=')[1]}\n"
        new_format += "```"

        fi_logger.info("Old format:")
        fi_logger.info(match.group(0))
        fi_logger.info("New format:")
        fi_logger.info(new_format)

        text = text.replace(match.group(0), new_format)

    return text
