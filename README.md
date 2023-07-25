# json_html.py
Python code that translates JSON template to HTML

## Requirements
- Python >=3.10

## Install
Simply use the command `pip install json-html` to install the package.

## Usage (Python)
```py
import json
from json_html import JSONHTML

with open("./FILENAME.json", "r", encoding="utf-8") as f:
    data = json.load(f)

html = JSONHTML(data)
html.to_file("./FILENAME.html")
```

## Usage (Command)
```
usage: [-h] [-o OUTPUT] [-v] [filename]

Python code that translates JSON template to HTML

positional arguments:
  filename              JSON template file

options:
  -h, --help                  show this help message and exit
  -o OUTPUT, --output OUTPUT  Output filename
  -v, --version               Show the version number and exit
```
