"""This module fixes the driver index page"""


def fix_driver_index(text):

    text = text.replace("(linux-drivers/", "(drivers/linux-drivers/")
    text = text.replace("(/linux-drivers/", "(drivers/linux-drivers/")
    text = text.replace("maxim>", "https://www.maximintegrated.com/")

    return text