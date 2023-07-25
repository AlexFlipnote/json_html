import json

from json_html import JSONHTML

with open("./hello_world.json", "r", encoding="utf-8") as f:
    data = json.load(f)

html = JSONHTML(data)
html.to_file("./hello_world.html")
