install:
	#install the package
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format the code
lint:
	#flake8 or pylint
test:
	#run the tests
deploy:
	#deploy the package
all: install format lint test deploy