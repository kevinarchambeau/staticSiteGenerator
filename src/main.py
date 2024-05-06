import os
import shutil

from textnode import TextNode


def setup_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    setup_public()


main()
