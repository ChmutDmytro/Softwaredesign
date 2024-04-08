import re


class LightNode:
    def __init__(self):
        pass

    def render(self):
        pass


class LightElementNode(LightNode):
    def __init__(self, tag_name, display_type, closing_type, css_classes=None):
        super().__init__()
        self.tag_name = tag_name
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes if css_classes else []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        outer_html = f"<{self.tag_name} class=\"{' '.join(self.css_classes)}\">"
        if self.display_type == "block":
            outer_html += "\n"
        for child in self.children:
            outer_html += child.render()
        if self.closing_type == "dual":
            outer_html += f"</{self.tag_name}>"
        elif self.closing_type == "single":
            outer_html += f"/>"
        if self.display_type == "block":
            outer_html += "\n"
        return outer_html

    def render_inner_html(self):
        inner_html = ""
        for child in self.children:
            inner_html += child.render()
        return inner_html


class LightTextNode(LightNode):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def render(self):
        return self.content


# Створюємо елементи розмітки
header = LightElementNode("header", "block", "dual", ["header"])
h1 = LightElementNode("h1", "block", "dual")
h1.add_child(LightTextNode("Welcome to LightHTML!"))
header.add_child(h1)

nav = LightElementNode("nav", "block", "dual", ["navbar"])
ul = LightElementNode("ul", "block", "dual")
li1 = LightElementNode("li", "block", "dual")
li1.add_child(LightTextNode("Home"))
li2 = LightElementNode("li", "block", "dual")
li2.add_child(LightTextNode("About"))
ul.add_child(li1)
ul.add_child(li2)
nav.add_child(ul)

# Додаємо header та nav до сторінки
page = LightElementNode("div", "block", "dual", ["page"])
page.add_child(header)
page.add_child(nav)

# Виведемо outerHTML та innerHTML
print("OuterHTML:")
print(page.render())
print("\nInnerHTML:")
print(page.render_inner_html())