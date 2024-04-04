TARGET="https://wiki.analog.com/resources/tools-software/linux-drivers-all"

# wget $TARGET?do=export_raw -O linux-drivers-all.txt

# pandoc -L adi_wiki.lua --verbose -f dokuwiki -t rst -o linux-drivers-all.rst linux-drivers-all.txt
pandoc -L adi_wiki.lua --wrap=preserve --verbose -f dokuwiki -t markdown -o linux-drivers-all.md linux-drivers-all.txt

sed -i 's/\xC2\xA0/ /g' linux-drivers-all.md

# Build list of linked drivers
# Links are of the form: -[ADP5520: Backlight Driver with I/O Expander](linux-drivers//multifunction-device/adp5520)
# We want to extract the driver name and the link

cat linux-drivers-all.md | grep "linux-drivers/" > linux-drivers-all-links.md

## Hand off to python script to extract driver names and links
