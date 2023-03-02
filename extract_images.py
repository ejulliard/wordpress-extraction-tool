import xml.etree.ElementTree as ET
import regex as re
import os
import shutil

# YOUR URL
url = "https://www.treepeo.com"

# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}

print("Loading for images extraction")

tree = ET.parse('data.xml')
root = tree.getroot()
xmlAsString = ET.tostring(root).decode("UTF-8")

images = re.findall('(?<=uploads/\d*/\d*/)(.*png|.*jpg|.*webp|.*svg)(?="|<)',xmlAsString)
images_list = []

for image in images :
    if image not in images_list:
        images_list.append(image)

base = "uploads/"
destination = "out/assets"

for root, dirs, files in os.walk(base):
    path = root.split(os.sep)

    for file in files:
        if not os.path.isdir(file) and file in images_list:
            shutil.move(os.path.join(root,file),os.path.join(destination,file))

print("Done!")