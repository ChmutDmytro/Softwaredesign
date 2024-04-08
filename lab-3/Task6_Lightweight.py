class LightHTML:
    def __init__(self, content):
        self.content = content

    def parse_book(self):
        html_elements = []
        lines = self.content.split('\n')
        for i, line in enumerate(lines):
            if i == 0:
                html_elements.append(f"<h1>{line}</h1>")
            elif len(line.strip()) < 20:
                html_elements.append(f"<h2>{line}</h2>")
            elif line.startswith(' '):
                html_elements.append(f"<blockquote>{line}</blockquote>")
            else:
                html_elements.append(f"<p>{line}</p>")
        return html_elements

    def calculate_memory_usage(self, html_elements):
        total_size = sum(map(len, html_elements))
        return total_size

    def lightweight_memory_usage(self, html_elements):
        # Застосовується патерн "Легковаговик" для зменшення споживання пам'яті
        pass

if __name__ == "__main__":
    with open('book.txt', 'r', encoding='utf-8') as file:
        book_content = file.read()

    light_html = LightHTML(book_content)
    html_elements = light_html.parse_book()
    for element in html_elements:
        print(element)

    memory_usage = light_html.calculate_memory_usage(html_elements)
    print("Memory usage:", memory_usage)

    light_html.lightweight_memory_usage(html_elements)