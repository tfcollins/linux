"""This module fixes poorly converted formatting"""


import os
import re
import sys
import shutil
import logging

fpl_logger = logging.getLogger("fix_poor_formatting")


def fix_poor_formatting(text):

    # Check if any formatting is broken
    s = r"\[(.*)\]\{\.underline\}"
    for match in re.finditer(s, text):
        fpl_logger.info(f"Found poor formatting G0: {match.group(0)}")
        fpl_logger.info(f"Found poor formatting G1: {match.group(1)}")

        new_block = f"_{match.group(1)}_"
        text = text.replace(match.group(0), new_block)

    return text
