import xml.etree.ElementTree as ET
import markdownify

# YOUR URL
url = "https://www.treepeo.com"

# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}

print("Loading for contents extraction")

tree = ET.parse('data.xml')
root = tree.getroot()

# POST EXTRACTION
for item in root.iter('item'):

    name = item.find("wp:post_name", NS_MAP).text

    # CONTENT EXTRACTION
    content = item.find("content:encoded", NS_MAP).text
    if content:
        # SAVE CONTENT EXTRACTED
        content_file = open("out/posts/" + name + ".md", "w")
        content_file.write(markdownify.markdownify(content))
        content_file.close()
    
print("Done!")