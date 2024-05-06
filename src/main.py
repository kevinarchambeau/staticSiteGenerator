import os
import shutil

from inline_markdown import extract_title
from block_markdown import markdown_to_html_node


def setup_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")


def generate_page(from_path, template_path, dest_path):
    print(f"generating {from_path}, using {template_path}, to {dest_path}")
    markdown = open(from_path).read()
    destination = open(dest_path, "w")
    title = extract_title(markdown)
    if not title:
        raise ValueError("No title found")
    stripped_title = title.group(0).lstrip("#").strip()
    template = open(template_path).read()
    node = markdown_to_html_node(markdown)
    html_to_insert = node.to_html()
    template_with_title = template.replace("{{ Title }}", stripped_title, 1)
    page = template_with_title.replace("{{ Content }}", html_to_insert, 1)
    destination.write(page)
    destination.close()


def main():
    setup_public()
    print("converting file")
    generate_page("content/index.md", "template.html", "public/index.html")


main()
