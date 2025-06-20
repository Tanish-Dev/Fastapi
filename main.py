from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://Tanish-dev:xogtu2-kofwoj-sEpnef@cluster0.n4ytgbb.mongodb.net/")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.findone({ })
    for doc in docs:
        print(doc)
    return templates.TemplateResponse("index.html", {"request": request})
