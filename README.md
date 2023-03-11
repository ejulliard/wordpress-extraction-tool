# Wordpress extraction tools (BETA VERSION)

## Introduction

Notre outil de migration de site Wordpress vers un autre framework est la solution idéale pour les propriétaires de sites web qui souhaitent migrer de Wordpress vers un nouveau framework sans perdre leur contenu existant. Grâce à notre outil, la migration de votre site web se fait en quelques clics, sans avoir à réécrire le code source de votre site.

Notre outil est facile à utiliser. Il suffit de suivre les instructions simples et claires pour migrer votre site web vers le framework de votre choix. Que vous choisissiez Angular, React ou Vue.js, notre outil de migration s'adaptera à vos besoins.

Notre outil de migration de site web est également très rapide et efficace. Il permet de migrer votre site web en un temps record, sans aucun compromis sur la qualité et l'intégrité de votre contenu. Vous pouvez ainsi bénéficier des avantages offerts par le nouveau framework sans subir les inconvénients d'une migration manuelle.

En somme, notre outil de migration de site web est une solution simple, efficace et rapide pour migrer votre site web vers un nouveau framework. N'hésitez pas à l'essayer dès maintenant et à découvrir ses nombreux avantages pour votre entreprise ou votre projet en ligne.

## Comment cela fonctionne ?

Afin de faciliter le travail d'intégration dans votre nouveau framework, l'outil vous génère des fichiers de base : JSON pour les data et Markdown pour le contenu. En plus, il est RankMath friendly !

### Pourquoi le JSON ?

L'utilisation d'un fichier JSON pour communiquer présente de nombreux avantages pour les développeurs et les experts SEO. Tout d'abord, le format JSON est très simple à comprendre et à utiliser, ce qui facilite la communication entre les différentes parties prenantes d'un projet. De plus, les fichiers JSON sont facilement interprétables ce qui en fait un choix idéal pour l'optimisation des moteurs de recherche. En utilisant un fichier JSON pour communiquer, les développeurs peuvent également simplifier la gestion des données, réduire les erreurs de communication et accélérer le développement de leur projet.

Par exemple :

1. Votre expert SEO intègre toutes ces méta data (méta-titre, méta-description, H1, Alt d'image, slug...) dans un fichier Excel.
2. Le fichier est converti en JSON
3. Le JSON est intégré dans le site web. Le développeur intègre dynamiquent dans ses layouts toutes les variables avec map()

Toutes vos données SEO sont placées dans un seul fichier.

### Pourquoi le Markdown ?

Même principe pour principe pour le contenu des pages. Premièrement, le fait d'utiliser MD supprime toutes les classes et balises WP inutiles.

De plus, un fichier MD est plus facile à gérer pour un rédacteur web. Plus d'erreur HTML de la part du rédacteur ou un travail de réécriture du texte brut par le développeur.

## Mode d'emploi

1. Extraire toutes les données WP depuis l'Administration :

**OUTILS > EXPORTER > Tout le contenu > Télécharger le fichier d'exportation**

2. Déposer votre fichier à la racine du projet en le renommant en "data.xml".
3. Déposer votre dossier Uploads contenant toutes vos images à la racine du projet.
4. Indiquer votre url dans tous le fichier .py que vous souhaitez utiliser

```
# YOUR URL
url = "https://www.yourwebsite.com"

```

5. Indiquer votre map RSS (disponible au début de votre fichier xml) dans la balise \<rss>

```

# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}

```

6. Lancer le programme désiré :

- extract_content.py : Extraction de tout le contenu de vos page et enregistrement dans le dossier out/content/ sous format .md avec le slug comme titre.
- extract_meta.py : Extraction des méta-données, des catégories et des tags et création des fichiers JSON.
- extract_images.py : Extraction de toutes les images présentes dans les pages html puis migration seulement des images nécessaires dans le dossier out/assets/

  **ATTENTION: LES FICHIERS JSON CONTENUS DANS LE DOSSIER /OUT DOIVENT ÊTRE SUPPRIMÉS AVANT DE RELANCER LE PROGRAMME**

---

ENGLISH VERSION

## Introduction

Our Wordpress to another framework migration tool is the ideal solution for website owners who want to migrate from Wordpress to a new framework without losing their existing content. With our tool, website migration can be done in just a few clicks, without the need to rewrite your site's source code.

Our tool is easy to use. Simply follow the clear and simple instructions to migrate your site to the framework of your choice. Whether you choose Angular, React, or Vue.js, our migration tool will adapt to your needs.

Our website migration tool is also very fast and efficient. It allows you to migrate your website in record time, without compromising the quality and integrity of your content. This way, you can benefit from the advantages offered by the new framework without experiencing the drawbacks of a manual migration.

In summary, our website migration tool is a simple, efficient, and fast solution to migrate your site to a new framework. Don't hesitate to try it now and discover its many benefits for your business or online project.

## How it Works?

To facilitate the integration process into your new framework, our tool generates basic files: JSON for data and Markdown for content.
Plus, it's RankMath friendly!

### Why JSON?

Using a JSON file for communication offers numerous benefits for developers and SEO experts. First, the JSON format is straightforward and easy to use, making communication between different project stakeholders easier. Additionally, JSON files are easily interpretable, making them an ideal choice for search engine optimization. By using a JSON file for communication, developers can simplify data management, reduce communication errors, and speed up project development.

For example:

Your SEO expert integrates all meta data (meta title, meta description, H1, image alt, slug, etc.) into an Excel file.
The file is converted to JSON.
The JSON is integrated into the website. The developer dynamically integrates all variables with map() into their layouts.
All your SEO data is placed in a single file.

### Why Markdown?

The tool generates basic files in JSON for data and Markdown for content to make integration into your new framework easier.

Using Markdown to communicate has many advantages for web developers and content experts. Firstly, the Markdown format is straightforward and easy to understand, making communication between different stakeholders in a project easier. Additionally, Markdown files are easily interpretable, making them an ideal choice for search engine optimization. By using Markdown to communicate, developers can simplify data management, reduce communication errors, and speed up project development.

For content, using Markdown eliminates unnecessary WP classes and tags, making it easier for web writers to manage content without HTML errors or requiring developers to rework raw text.

## Instructions

1. Extract all WP data from the administration panel:

**TOOLS > EXPORT > ALL CONTENT > DOWNLOAD EXPORT FILE**

2. Drop your file at the root of the project, renaming it to "data.xml".
3. Drop your Uploads folder containing all your images at the root of the project.
4. Indicate your URL in all the .py files you want to use

```
# YOUR URL
url = "https://www.yourwebsite.com"
```

5. Indicate your RSS map (available at the beginning of your XML file) in the \<rss> tag

```
# COPY-PASTE YOUR XML'S RSS MAP
NS_MAP = {
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp" : "http://wordpress.org/export/1.2/"
}
```

6. Run the desired program:

- extract_content.py: Extract all your page content and save it in the out/content/ folder in .md format with the slug as title.
- extract_meta.py: Extract metadata, categories, and tags and create JSON files.
- extract_images.py: Extract all images present in the HTML pages and migrate only the necessary images to the out/assets/ folder.

**NOTE: THE JSON FILES CONTAINED IN THE /OUT FOLDER MUST BE DELETED BEFORE RUNNING THE PROGRAM AGAIN**
