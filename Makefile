bump_version:
	bumpversion patch

publish:
	pip install twine
	python setup.py sdist
	twine upload dist/*
	rm -fr build dist

test:
	tox

