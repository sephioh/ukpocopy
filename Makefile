bump_patch_version:
	bumpversion patch

bump_minor_version:
	bumpversion minor

bump_major_version:
	bumpversion major

publish:
	pip install twine
	python setup.py sdist
	twine upload dist/*
	rm -fr build dist

test:
	nosetests --with-coverage
