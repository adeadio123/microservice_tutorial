install:
	#install the package
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format the code
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#run the tests
	python3.11 -m pytest -vv --cov=mylib test_logic.py
build:
	#build container
deploy:
	#deploy the package
all: install format lint test deploy