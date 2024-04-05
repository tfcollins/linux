"""This module fixes the xterm tags in the markdown files.
The term tags are generally used to mark code blocks"""

import re

def update_xterm_blocks(text):

    text = text.replace('<xterm>', '```bash')
    text = text.replace('</xterm>', '```')

    return text