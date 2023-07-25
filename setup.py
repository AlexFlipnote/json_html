import re

from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('json_html/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


setup(
    name='json-html',
    author='AlexFlipnote',
    url='https://github.com/AlexFlipnote/json_html.py',
    version=version,
    packages=['json_html'],
    license='MIT',
    description='Python code that translates JSON template to HTML',
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'json_html=json_html.cmd:main'
        ]
    }
)
