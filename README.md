# microservice_tutorial

- Create a virtual environment ~'python3 -m venv <env_name>
- Create files (Makefile, requirements.txt, main.py, DOckerfile, mylib/__init__.py)
- Populate 'Makefile' (The makefile helps us to store the steps inside it.)
- Build cli using Python fire library "./cli-fire.py --help" to test the logic

fastapi
Demo of FastAPI + AWS App Runner
run docker

docker build .

Note this is your container name use: docker image ls to find:

docker run -p 127.0.0.1:8000:8000 54a55841264f