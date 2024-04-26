"""Add metadata to markdown files"""
import os
import logging

meta_logger = logging.getLogger("metadata")


def get_part_name(driver):
    """Get part name from driver name"""
    parts = ["AD", "LTC", "HMC", "SSM", "MAX"]
    found = False
    part = None
    for p in parts:
        if p in driver:
            found = True
            for sec in driver.split(" "):
                if p in sec:
                    part = sec
                    part = part.replace(":", "")
                    break
    if part:
        driver = part
    driver = driver.strip()
    return driver


def parse_compatibles(filename, driver):
    """Parse compatible strings from driver"""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, "r") as f:
        text = f.read()

    compatibles = []
    driver_name = get_part_name(driver)
    driver_name = driver_name.lower()

    for line in text.split("\n"):
        if ".compatible" in line:
            # .compatible = "adi,adar3003",
            line = line.split("=")[1]
            quote = '"' if '"' in line else "'"
            line = line.split(quote)[1]
            line = line.replace('"', "")
            line = line.replace("'", "")
            line = line.strip()

            compatibles.append(line)
        elif ".name" in line and driver_name in line.lower() and line.count('"') == 2:
            # .name = "adar3003",
            print("LINE: ", line)
            print("DRIVER: ", driver_name)
            line = line.split("=")[1]
            quote = '"' if '"' in line else "'"
            line = line.split(quote)[1]
            line = line.replace('"', "")
            line = line.replace("'", "")
            line = line.strip()
            compatibles.append(line)
        elif f'"{driver}"' in line:
            compatibles.append(driver.lower())
        elif f"'{driver}'" in line:
            compatibles.append(driver.lower())
        elif f'"{driver.lower()}"' in line:
            compatibles.append(driver.lower())
        elif f"'{driver.lower()}'" in line:
            compatibles.append(driver.lower())

    return compatibles


def locate_driver(driver, kernel_root):
    """Located associated driver source from driver name"""

    # Determine part name
    if "Fan Control IP core" in driver:
        driver = "Fan Control IP"
    else:
        parts = ["AD", "LTC", "HMC", "SSM", "MAX"]
        found = False
        part = None
        for p in parts:
            if p in driver:
                found = True
                for sec in driver.split(" "):
                    if p in sec:
                        part = sec
                        part = part.replace(":", "")
                        break
        if part:
            driver = part
        driver = driver.strip()

    # print(f"DRIVER {driver}")
    if "adrv9009" not in driver.lower() and "adrv9008" not in driver.lower():
        driver = driver.replace("-", "")

    # OLD with not standard compatible strings
    if driver in ["AD7142"]:
        drivers = ["drivers/input/misc/ad714x.c", "drivers/input/misc/ad714x-i2c.c"]
        drivers = [os.path.join(kernel_root, d) for d in drivers]
        return

    # Known missing
    this_folder = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(this_folder, "known_missing_drivers.txt"), "r") as f:
        known_missing = f.readlines()
        known_missing = [k.strip() for k in known_missing]
    if driver in known_missing:
        meta_logger.error(f"Known driver missing: {driver}")
        return

    # lets use grep to find the driver source since its fast(est)
    cmd = f"grep -l -r {kernel_root} -ie '{driver}'"
    import subprocess

    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        meta_logger.error(f"Error locating driver: {driver}")
        meta_logger.error(f"Error: {e}")
        with open("failed_no_driver_source.log", "w") as f:
            f.write(driver + "\n")
        return None
    output = output.decode("utf-8")
    output = output.split("\n")
    meta_logger.info(f"Output: {output}")

    # Remove duplicates
    output = list(set(output))

    remaining = []
    for fullpath in output:
        filename = fullpath.split("/")[-1]
        if filename in ["Kconfig.adi", "Makefile", "Kconfig", "Kconfig.debug", ""]:
            continue
        if ".h" in filename:
            continue

        remaining.append(fullpath)
    # print(f"Remaining1 : {remaining}")

    # Check if exact match with filename
    filenames = [f.split("/")[-1].lower() for f in remaining]
    for f, r in zip(filenames, remaining):
        if driver.lower() == f.split(".")[0]:
            remaining = [r]
            meta_logger.info(f"Driver found: {remaining}")
            return remaining

    next_remaining = []
    compatibles = {}
    allowed_subfolder = ["iio", "misc", "adi", "video", "i2c", "hwmon"]
    if len(remaining) > 1:
        for fullpath in remaining:
            subfolder_two = fullpath.split("/")[-3]
            subfolder = fullpath.split("/")[-2]
            if subfolder_two in allowed_subfolder or subfolder in allowed_subfolder:
                next_remaining.append(fullpath)
                compatibles[fullpath] = parse_compatibles(fullpath, driver)
        remaining = next_remaining
    # print(f"Remaining2 : {remaining}")

    if len(remaining) > 1:
        # Pick driver file that contains the driver name in compatible string
        next_remaining = []
        # all_compatibles = [v for k, v in compatibles.items()]
        all_compatibles = []
        for k, v in compatibles.items():
            all_compatibles += v

        print(f"Compatibles: {all_compatibles}")
        for fullpath in remaining:
            for compatible in compatibles[fullpath]:
                if driver.lower() in compatible:
                    next_remaining.append(fullpath)
                    # break
        next_remaining = list(set(next_remaining))  # Remove duplicates
        remaining = next_remaining
    # print(f"Remaining3 : {remaining}")

    # Allow special cases
    if len(remaining) == 2:

        if driver in ["AD7476", "AD7091"]:
            meta_logger.info(f"Driver found: {remaining}")
            return

        # Handle cases when driver is ADXXXX and ADXXXX-Y
        filenames = [f.split("/")[-1].lower() for f in remaining]
        for f, r in zip(filenames, remaining):
            if "-" in f and "-" in driver:
                # Match last part
                if f.split("-")[-1] == driver.split("-")[-1]:
                    remaining = [r]
                    meta_logger.info(f"Driver found: {remaining}")
                    return remaining
            elif "-" not in f and "-" not in driver:
                remaining = [r]
                meta_logger.info(f"Driver found: {remaining}")
                return remaining

        # Handle cases where files are PART-spi.c and PART-i2c.c
        filenames = [f.split("/")[-1].lower() for f in remaining]
        i2c = False
        spi = False
        for f, r in zip(filenames, remaining):
            if "i2c" in f:
                i2c = True
                if spi:
                    meta_logger.info(f"Driver found: {remaining}")
                    return remaining
            elif "spi" in f:
                spi = True
                if i2c:
                    meta_logger.info(f"Driver found: {remaining}")
                    return remaining

        # Handle case where driver is driver.c and driver_conv.c
        filenames = [f.split("/")[-1].lower() for f in remaining]
        # Check if _conv in any of the filenames
        if any(["_conv" in f for f in filenames]):
            conv_file = [f for f in filenames if "_conv" in f][0]
            other = [f for f in filenames if "_conv" not in f][0]
            if conv_file.split("_")[0] == other.split(".c")[0]:
                remaining = [remaining[filenames.index(other)]]
                meta_logger.info(f"Driver found: {remaining}")
                return remaining

        # Others
        special_allowed = ["cf_axi_adc_core.c"]
        is_special = False
        for fullpath in remaining:
            if fullpath.split("/")[-1] in special_allowed:
                is_special = True

        if is_special:
            meta_logger.info(f"Driver found: {remaining}")
            return remaining

    if len(remaining) > 2:
        # Check if there are i2c and spi files and only keep those
        i2c = False
        spi = False
        next_remaining = []
        filenames = [f.split("/")[-1].lower() for f in remaining]
        for filename, fullpath in zip(filenames, remaining):
            if "i2c" in filename:
                i2c = True
                next_remaining.append(fullpath)
            elif "spi" in filename:
                spi = True
                next_remaining.append(fullpath)
            if i2c and spi:
                remaining = next_remaining
                meta_logger.info(f"Driver found: {next_remaining}")
                return remaining

    if len(remaining) != 1:
        meta_logger.error(f"Error locating driver: {driver}")
        meta_logger.error(f"To many remaining: {remaining}")
        assert False
        return

    meta_logger.info(f"Remaining4 : {remaining}")
    return remaining

    # assert False, "Should not reach here"


def add_metadata(text, metadata, kernel_root=None):
    """Add metadata to the top of a markdown file"""

    root = f"""---
wiki-source: {metadata['link']}
title: {metadata['driver']}
"""

    if kernel_root:
        source = locate_driver(metadata["driver"], kernel_root)
        if source:
            compatibles = [parse_compatibles(s, metadata["driver"]) for s in source]
            print(f"compatibles: {compatibles}")
            source = ", ".join(source)
            compatibles = [", ".join(c) for c in compatibles]
            compatibles = ", ".join(compatibles)
            root += f"source: {source}\n"
            root += f"compatibles: {compatibles}\n"

    root += "---\n"

    print(f"ROOT: {root}")

    return root + text
