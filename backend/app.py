from fastapi import FastAPI, Path, Response
from fastapi.responses import FileResponse, RedirectResponse
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

