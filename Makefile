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
	python3.11 -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker 
	docker run -p 127.0.0.1:8000:8000 7eb2365f1e7c	
deploy:
	#deploy the package
all: install format lint test deploy