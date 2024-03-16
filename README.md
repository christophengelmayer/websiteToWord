# Script to convert a website to a single word document

This is a set of tools and scripts designed to simplify the process of converting web pages into a single Microsoft Word document. This utility is especially useful for archiving, content analysis, or offline reading purposes. The process involves generating a sitemap, extracting content, converting it into Markdown format, and then transforming the Markdown file into a Word document with optional embedded resources.

## Features

- **Sitemap Generation**: Automatically generate a sitemap of your target website to map out all the URLs.
- **Content Extraction**: Convert web pages into Markdown format for easy manipulation and conversion.
- **Markdown to Word Conversion**: Utilize Pandoc to convert Markdown files into fully formatted Word documents.
- **Resource Embedding**: Option to embed images directly into the Word document, ensuring content is accessible offline.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm (for sitemap generation)
- Pandoc (for Markdown to Word conversion)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourgithubusername/convert-website-to-word.git
cd convert-website-to-word
```

2. **Set up a Python virtual environment**

```bash
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Generate a Sitemap**

Edit the following command with your target website instead of `https://example.com`.

```bash
npx sitemap-generator-cli -v -r -q https://example.com
```

Modify the generated sitemap so that each line contains only one URL. You may need to sort or filter the URLs as necessary.

### Usage

1. **Activate the Python virtual environment**

```bash
source venv/bin/activate
``` 

2. **Run the script to convert URLs to Markdown**
 
```bash
python main.py
```

Ensure your sitemap or list of URLs is correctly configured in the script.

3. **Convert Markdown to Word with Pandoc**
 
```
bash
pandoc output/out.md -o output/out.docx --embed-resources
```

The `--embed-resources` flag ensures that images are embedded directly into the Word document.
