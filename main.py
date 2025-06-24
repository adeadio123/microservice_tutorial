from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wiki_logic

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "A simple FastAPI app with wiki function, "
        "call /search/{value} or /search/{name} to search Wikipedia"
    }


@app.get("/search/{value}")
async def search(value: str):
    """ "Page to search wikipedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """ "Page to search wikipedia"""
    result = wiki_logic(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
