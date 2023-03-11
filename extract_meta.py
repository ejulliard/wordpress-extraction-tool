import xml.etree.ElementTree as ET
from datetime import datetime
import regex as re

# YOUR URL
url = ""

# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}

print("Loading for meta extraction")

tree = ET.parse('data.xml')
root = tree.getroot()


# POST EXTRACTION
meta_file = open("out/meta.json", "a")
meta_file.write('{\n"meta":\n[\n')
for item in root.iter('item'):
    meta_file.write('{\n')
    itemId = item.find("wp:post_id", NS_MAP).text
    if itemId :
        meta_file.write('"id": "' + itemId + '",\n')
    itemType = item.find("wp:post_type", NS_MAP).text
    if itemType:
        meta_file.write('"type": "' + itemType + '",\n')
    name = item.find("wp:post_name", NS_MAP).text
    if name:
        meta_file.write('"name": "' + name + '",\n')
    title = item.find("title").text
    if title:
        meta_file.write('"title": "' + title + '",\n')
    slug = item.find("link").text.replace(url, "")
    if slug:
        meta_file.write('"slug": "' + slug + '",\n')
    pubDate = item.find('pubDate').text
    if pubDate:
        meta_file.write('"pubDate": "' + pubDate + '",\n')
    categories = []
    category = item.findall("category")
    for cat in category:
        categories.append(cat.text)
    image = item.find("guid").text
    imageUrls = re.search('(?<=' + url + '/wp-content/uploads/\d*/\d*)(/.*)', image)
    if imageUrls:
        imageUrl = imageUrls.group(0)
        meta_file.write('"image": "/assets' + imageUrl + '",\n')
    
    meta_file.write('"categories": "' + str(categories) + '",\n')

    # IF YOU USED RANKMATH
    metas = item.findall("wp:postmeta", NS_MAP)
    for meta in metas:
        key = meta.findall("wp:meta_key", NS_MAP)
        value = meta.findall("wp:meta_value", NS_MAP)
        for i in range(len(key)):
            if key[i].text == "_thumbnail_id":
                imageId = value[i].text
                meta_file.write('"imageId": "' + imageId + '",\n')
            if key[i].text == "rank_math_title":
                seoTitle = value[i].text
                meta_file.write('"seoTitle": "' + seoTitle + '",\n')
            elif key[i].text == "rank_math_description":
                seoDescription = value[i].text
                meta_file.write('"seoDescription": "' + seoDescription + '",\n')
            elif key[i].text == "rank_math_schema_BlogPosting":
                seoKeywords = re.search('(?<="keywords";s:\d.:")(.*?)(?=\s*")', value[i].text)
                if seoKeywords and seoKeywords.group(0) != '%keywords%':
                    seoKeyword = seoKeywords.group(0)
                    meta_file.write('"seoKeyword": "' + seoKeyword + '",\n')

    meta_file.write('},\n')
meta_file.write(']\n}')
meta_file.close()



# CATEGORY EXTRACTION
category_file = open("out/categories.json", "a")
category_file.write('{\n"categories":\n[\n')
for channel in root.iter('channel'):
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
                    category_file.write('"keywords": "'+ seoKeyword + '"\n,')
        category_file.write('},\n')
category_file.write('\n]\n}')
category_file.close()

# TAG EXTRACTION
for channel in root.iter('channel'):
    tags = channel.findall("wp:tag", NS_MAP)
    tag_file = open("out/tags.json", "a")
    tag_file.write('{\n"tags":\n[\n')
    for tag in tags:
        tagId = tag.find("wp:term_id", NS_MAP).text
        slug = tag.find("wp:tag_slug", NS_MAP).text
        name = tag.find("wp:tag_name", NS_MAP).text
        if tagId:
            tag_file.write('{"id": "'+ tagId +'",\n')
        if name:
            tag_file.write('"name": "'+ name +'",\n')
        if slug:
            tag_file.write('"slug": "'+ slug +'",\n,')
        tag_file.write('},')
tag_file.write('\n]\n}')
tag_file.close()


# IF YOU USE POLYLANG
for channel in root.iter('channel'):
    terms = channel.findall("wp:term", NS_MAP)
    trans_file = open("out/translations.json", "a")
    trans_file.write('{\n"translations":\n[\n')
    for translation in terms:
        tType  = translation.find("wp:term_taxonomy", NS_MAP).text
        if tType == "term_translations":
            transId = translation.find("wp:term_id", NS_MAP).text
            if transId:
                trans_file.write('{"id": "' + transId + '",\n')
            name = translation.find("wp:term_name", NS_MAP).text
            if name:
                trans_file.write('"name": "' + name + '",\n')
            lang = translation.find("wp:term_description", NS_MAP).text
            if lang:
                trans_file.write('"lang": [\n')
                languages = re.search('(?<=s:\d:")\w+(?=")', lang)
                values = re.search("(?<=i:)\d+(?=;s)", lang)
                if languages and values:
                    languages = languages.group(0)
                    values = values.group(0)
                    trans_file.write('{"' + languages + '": "' + values + '"},')
                trans_file.write('],\n')
            trans_file.write('},\n')
trans_file.write(']\n}')

print("Done!")
