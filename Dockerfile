FROM python:3.11.13-slim-bookworm

RUN mkdir -p /app
COPY . main.py requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]