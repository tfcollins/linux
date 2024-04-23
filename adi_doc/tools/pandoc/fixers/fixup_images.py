"""This module will parse markdownfiles for picture links, download the pictures
 and fix the links to point to the local files."""

import os
import re
import shutil
import sys
import time
import requests
from urllib.parse import urlparse


def download_image(url, output):
    """Download an image from a URL to a file."""
    import requests

    # Download the image
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to download {url}: {response.status_code}")
            return False

        # Save the image
        with open(output, "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

    return True


def get_link(url, image, target_dir, text, ref_image):
    filename = os.path.basename(urlparse(url).path)
    output = os.path.join(target_dir, filename)
    if not os.path.exists(output):
        print(f"Downloading {url} to {output}")
        result = download_image(url, output)
        if not result:
            print(f"Failed to download {url}")
            with open("failed_images.txt", "a") as f:
                f.write(f"{image}: {url}\n")
            return None
    else:
        print(f"Skipping {url} to {output}. File already exists.")

    # Fix the image link
    text = text.replace(ref_image, f"images/{filename}")
    return text


def fixup_images(text, target_dir):

    print("---------------------------------------")

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
        print(f"Processing image {image}")

        # Check for file extension in URL
        if not image.endswith((".jpg", ".png", ".gif", ".jpeg", ".bmp", ".svg")):
            print(f"Skipping image {image}. Not a valid image file.")
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
                    print(f"Failed to find image {guess}")
                    with open("failed_images.txt", "a") as f:
                        f.write(f"{image}: {guess}\n")
                    continue
            except Exception as e:
                print(f"Failed to find image {guess}: {e}")
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
        print(f"Attributes: {attributes}")
        print(f"Attributes Split: {attributes.split()}")
        for attribute in attributes.split():
            if "=" not in attribute:
                new_format += f":{attribute}\n"
            else:
                new_format += f":{attribute.split('=')[0]}: {attribute.split('=')[1]}\n"
        new_format += "```"

        print("Old format:")
        print(match.group(0))
        print("New format:")
        print(new_format)

        text = text.replace(match.group(0), new_format)

    return text
