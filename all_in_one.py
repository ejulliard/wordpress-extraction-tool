import xml.etree.ElementTree as ET
from datetime import datetime
import regex as re
import markdownify

# YOUR URL
url = "https://www.treepeo.com"

# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}

print("Loading for all extraction")

tree = ET.parse('data.xml')
root = tree.getroot()

pages_file = open("out/pages.json", "a")
pages_file.write('{\n"pages":\n[\n')

# POST EXTRACTION
for item in root.iter('item'):
    itemId = item.find("wp:post_id", NS_MAP).text
    name = item.find("wp:post_name", NS_MAP).text
    title = item.find("title").text
    slug = item.find("link").text.replace(url, "")
    # pubDate = str(datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S +0000').date())

    pages_file.write('{\n"id": "' + itemId + '",\n"name": "' + name + '",\n"title": "' + title + '",\n"slug": "' + slug + '",\n')

    categories = []
    category = item.findall("category")
    for cat in category:
        categories.append(cat.text)
    pages_file.write('{\n"category": "' + categories + '",\n')
    image = item.find("guid").text
    imageUrls = re.search('(?<=' + url + '/wp-content/uploads/\d*/\d*)(/.*)', image)
    if imageUrls:
        imageUrl = imageUrls.group(0)
        pages_file.write('"image": "/assets/' + imageUrl + '",\n')
    
    # CONTENT EXTRACTION
    content = item.find("content:encoded", NS_MAP).text
    if content:
        # SAVE CONTENT EXTRACTED
        content_file = open("out/posts/" + name + ".md", "w")
        content_file.write(markdownify.markdownify(content))
        content_file.close()
    
    # IF YOU USED RANKMATH
    metas = item.findall("wp:postmeta", NS_MAP)
    for meta in metas:
        key = meta.findall("wp:meta_key", NS_MAP)
        value = meta.findall("wp:meta_value", NS_MAP)
        for i in range(len(key)):
            if key[i].text == "rank_math_title":
                seoTitle = value[i].text
                pages_file.write('{\n"seoTitle": "' + seoTitle + '",\n')
            elif key[i].text == "rank_math_description":
                seoDescription = value[i].text
                pages_file.write('{\n"seoDescription": "' + seoDescription + '",\n')
            elif key[i].text == "rank_math_schema_BlogPosting":
                seoKeywords = re.search('(?<="keywords";s:\d.:")(.*?)(?=\s*")', value[i].text)
                if seoKeywords and seoKeywords.group(0) != '%keywords%':
                    seoKeyword = seoKeywords.group(0)
                    pages_file.write('{\n"seoKeyword": "' + seoKeyword + '"\n},\n')
pages_file.write(']\n}')
pages_file.close()

# CATEGORY EXTRACTION
for channel in root.iter('channel'):
    category_file = open("out/categories.json", "a")
    category_file.write('{\n"categories":\n[\n')

    categories = channel.findall("wp:category", NS_MAP)

    for category in categories:
        categoryId = category.find("wp:term_id", NS_MAP).text
        name = category.find("wp:cat_name", NS_MAP).text
        catSlug = category.find("wp:category_nicename", NS_MAP).text

        category_file.write('{\n"id": "' + categoryId + '",\n"name": "' + name + '",\n"slug": "' + catSlug + '",\n')

        catParents = category.find("wp:category_parent", NS_MAP)
        if catParents:
            catParent = catParents.text
            category_file.write('"parent": "' + catParent + '",\n')
        descriptions = category.find("wp:category_description", NS_MAP)
        if descriptions:
            description = descriptions.text
            category_file.write('"description": "' + description + '",\n')
        # IF YOU USED RANKMATH
        metas = category.findall("wp:termmeta", NS_MAP)
        for meta in metas:
            key = meta.findall("wp:meta_key", NS_MAP)
            value = meta.findall("wp:meta_value", NS_MAP)
            for i in range(len(key)):
                if key[i].text == "rank_math_title":
                    seoTitle = value[i].text
                    category_file.write('"seoTitle": "' + seoTitle + '",\n')
                elif key[i].text == "rank_math_description":
                    seoDescription = value[i].text
                    category_file.write('"seoDescription": "'+ seoDescription +'",\n')
                elif key[i].text == "rank_math_focus_keyword":
                    seoKeyword = value[i].text.replace(" ,",",")
                    category_file.write('"keywords": "'+ seoKeyword + '"\n},')

    category_file.write('\n]\n}')
    category_file.close()

    # TAG EXTRACTION
    tags = channel.findall("wp:tag", NS_MAP)
    tag_file = open("out/tags.json", "a")
    tag_file.write('{\n"tags":\n[\n')
    for tag in tags:
        tagIds = tag.find("wp:term_id", NS_MAP)
        slugs = category.find("wp:tag_slug", NS_MAP)
        names = category.find("wp:tag_name", NS_MAP)
        if tagIds:
            tagId = tagIds.text
            tag_file.write('"id": "'+ tagId +'",\n')
        if names:
            name = name.text
            tag_file.write('"name": "'+ name +'",\n')
        if slugs:
            slug = slugs.name
            tag_file.write('"slug": "'+ slug +'",\n},')

    tag_file.write('\n]\n}')
    tag_file.close()

# IMAGES EXTRACTION

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