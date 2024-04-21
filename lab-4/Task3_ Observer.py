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
        self.event_listeners = {}

    def add_child(self, child):
        self.children.append(child)

    def add_event_listener(self, event_type, callback):
        if event_type in self.event_listeners:
            self.event_listeners[event_type].append(callback)
        else:
            self.event_listeners[event_type] = [callback]

    def render(self):
        outer_html = f"<{self.tag_name} class=\"{' '.join(self.css_classes)}\""
        for event_type, callbacks in self.event_listeners.items():
            for callback in callbacks:
                outer_html += f" {event_type}=\"{callback}\""
        outer_html += ">"
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


if __name__ == "__main__":
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

    # Додамо EventListener для кліків на елемент "Home"
    def handle_home_click():
        print("Home clicked!")

    li1.add_event_listener("click", handle_home_click)

    # Виведемо outerHTML та innerHTML
    print("OuterHTML:")
    print(page.render())
    print("\nInnerHTML:")
    print(page.render_inner_html())

    # Додаємо кнопку для запуску програми
    print("\nTo simulate click on Home, click the button below:")
    print('<button onclick="handle_home_click()">Click me</button>')