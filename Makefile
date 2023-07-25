upload:
	@echo Uploading to PyPi...
	python setup.py sdist
	twine upload dist/*
	@echo Done!

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./json_html.egg-info

reinstall: uninstall install

install:
	pip install .

uninstall:
	pip uninstall json_html -y
