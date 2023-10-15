from fastapi import FastAPI, Path, Response
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from svgwrite import Drawing
import datetime
import os
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins
origins = ["*"]

# Add middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get('/')
def index():
    return RedirectResponse('https://pesu-badges.vercel.app/')

@app.get("/badgelist")
def list_files():
    try:
        files = os.listdir('./static/')
        return {"files": [re.match(r'([a-zA-Z\-_]+).svg', file)[1] for file in files]}
    except FileNotFoundError:
        return {"error": "Directory not found"}

@app.get("/badge/{file_name}")
def get_svg(file_name: str = Path(..., title="The name of your SVG file")):
    file_path = f"./static/{file_name}.svg"
    return FileResponse(file_path, media_type="image/svg+xml")

@app.get('/badgepics', response_class=HTMLResponse)
def get_badge_pics():
    para = '<p align="center">\n'
    for f in list_files()['files']:
        para += f"<img src='https://pesu-badges-api.vercel.app/badge/{f}' width='98px' height='30px' />\n"
    para += '</p>'
    return para