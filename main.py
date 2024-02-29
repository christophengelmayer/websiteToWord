import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def html_to_markdown(element):
    """
    Converts an HTML element to Markdown format, ignoring <div>, <span>, and class attributes.
    """
    if isinstance(element, NavigableString):
        return str(element)
    elif isinstance(element, Tag):
        if element.name == 'p':
            return f"{element.get_text(separator=' ', strip=True)}\n\n"
        elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = element.name[1]
            return f"\n\n{'#' * int(level)} {element.get_text()}\n\n"
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            return f"![{alt}]({src})\n\n"
        elif element.name == 'a':
            href = element.get('href', '')
            return f"[{element.get_text()}]({href})"
        elif element.name in ['div', 'span']:  # Ignore divs and spans, just process their children
            return "".join(html_to_markdown(child) for child in element.children)
        else:
            # For other tags, recursively process their children
            return "".join(html_to_markdown(child) for child in element.children)
    return ""

def fetch_main_content_markdown(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4XX or 5XX errors
        soup = BeautifulSoup(response.text, 'html.parser')
        main_content = soup.find('main')
        if main_content:
            markdown_content = f"---\n\n[{url}]({url})\n\n"
            markdown_content += "".join(html_to_markdown(child) for child in main_content.children)
            return markdown_content
        else:
            return f"# URL: {url}\n\nNo <main> tag found."
    except requests.RequestException as e:
        return f"Error fetching {url}: {str(e)}"

def append_to_markdown(file_path, markdown_content):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(markdown_content + '\n')

def process_urls(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        if url:
            markdown_content = fetch_main_content_markdown(url)
            append_to_markdown(output_file, markdown_content)

# Example usage
input_file = 'urls.txt'  # This should be the path to your text file containing URLs
output_file = 'output/out.md'  # This will be your Markdown file where content is appended
process_urls(input_file, output_file)
