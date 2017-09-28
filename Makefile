clear:
	find . -name "*.pyc" -exec rm -rf {} \;

dist: clear
	rm -rf dist
	virtualenv --python python3 venv
	venv/bin/pip install -U pip
	venv/bin/pip install -e .
	venv/bin/pip install twine
	venv/bin/pip install tox
	venv/bin/tox

upload: dist
	venv/bin/python setup.py sdist bdist_wheel
	venv/bin/twine upload dist/*
