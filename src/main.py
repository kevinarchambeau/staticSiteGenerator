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
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)

    for file in files:
        path = f"{dir_path_content}/{file}"
        if os.path.isfile(path):
            destination = f"{dest_dir_path}/{file.replace(".md", ".html")}"
            print(f"{path}, {template_path}, {destination}")
            generate_page(path, template_path, destination)
        elif os.path.isdir(path):
            destination = f"{dest_dir_path}/{file}"
            generate_pages_recursive(path, template_path, destination)


def main():
    setup_public()
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")


main()
