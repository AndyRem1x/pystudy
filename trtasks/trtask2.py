from requests import get
from bs4 import BeautifulSoup


class Node:
    def __init__(self, tag, text=None, children=None):
        self.tag = tag
        self.text = text
        self.children = children or []

    def add_children(self, node):
        self.children.append(node)


class HTMLTree:
    def __init__(self, html_file):
        self.html = html_file
        self.root = None
        self.tree = self.build_dom_tree(self.parse_html())

    def parse_html(self):
        with open(self.html, "r", encoding="UTF-8") as html_file:
            soup = BeautifulSoup(html_file, "html.parser")
            print(soup)
            return soup

    def build_dom_tree(self, element):
        node = Node(element.name, element.string.strip() if element.string else None)

        if self.root is None:
            self.root = node
        for child in element.children:
            if child.name is not None:
                child_node = self.build_dom_tree(child)
                node.add_children(child_node)
        return node

    def find_by_tag(self, tag):
        found_texts = []

        def find_text_recursive(node):
            if node.tag == tag and node.text is not None:
                found_texts.append(node.text)
            for child in node.children:
                find_text_recursive(child)
        find_text_recursive(self.root)
        return found_texts

    def print_tree(self, node=None, level=0):
        node = node or self.root
        print(f"{level * ' '}<{node.tag}> {node.text or ''}")
        for child in node.children:
            self.print_tree(child, level + 2)


URL = "https://github.com/AndyRem1x"
r = get(URL, timeout=200)
HTML = ""
if r.status_code == 200:
    HTML = r.text
with open("trtask2.html", "w", encoding="UTF-8") as file:
    file.write(HTML)
new_tree = HTMLTree("trtask2.html")
new_tree.print_tree()
print(new_tree.find_by_tag("li"))
