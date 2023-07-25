import re
import json

from bs4 import BeautifulSoup

__all__ = (
    "JSONHTML",
)


class JSONHTML:
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError("data must be a dict")

        self._data = data
        self.re_space = re.compile(r"^\s+")

        self._elements = [
            "html", "head", "body", "title",
            "h1", "h2", "h3", "h4", "h5", "h6",
            "div", "span", "p", "a", "img",
            "ul", "ol", "li", "table", "tr"
        ]

        self._attrs = [
            "id", "class", "style", "src", "href", "alt", "content"
        ]

    @classmethod
    def from_file(cls, filename: str) -> "JSONHTML":
        """ Attempts to load a JSON file and return the class """
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    def to_file(cls, filename: str) -> None:
        """ Writes the data to HTML file """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.prettify(cls.render(cls._data)))

    def element(self, tag: str, data: dict) -> str:
        """ Returns a HTML element with attributes and content """
        attrs = []

        content = data.get("content", "")

        for k, v in data.items():
            if k != "content" and k not in self._elements:
                attrs.append(f'{k}="{v}"')

        attrs_str = " ".join(attrs)

        if attrs_str:
            attrs_str = " " + attrs_str

        return f"<{tag}{attrs_str}>{content}"

    def render(self, data: dict = None) -> str:
        """ Returns a HTML string """
        html = ""
        data: dict = data or self._data

        for k, v in data.items():
            if isinstance(v, dict):
                if k in self._attrs:
                    continue
                if k in self._elements:
                    html += self.element(k, v)
                    html += self.render(v)
                    html += f"</{k}>"
            else:
                if k in self._attrs:
                    continue
                html += self.element(k, {"content": str(v)})

        return html

    def prettify(self, html_content, indent_width: int = 2) -> str:
        """ Returns a indented HTML string """
        soup = BeautifulSoup(html_content, "html.parser")
        pretty_html = soup.prettify(formatter=None)
        lines = pretty_html.split("\n")
        indented_html = "\n".join(
            self.re_space.sub(
                lambda m: " " * (len(m.group()) * indent_width),
                line
            )
            for line in lines
        )

        return indented_html
