test:
	coverage run -m pytest .
	coverage report -m
	coverage html -d htmlcov
