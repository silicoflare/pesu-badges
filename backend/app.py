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
    allow_methods=["*"],  # You can specify the HTTP methods that are allowed
    allow_headers=["*"],  # You can specify the HTTP headers that are allowed
)

# app.mount("/", StaticFiles(directory="./frontend/dist", html=True))
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

def generate_custom_font_badge(version):
    dwg = Drawing()

    # Badge style
    dwg.add(dwg.rect(insert=(0, 0), size=((len(version)+2)*9, 20), rx=5, ry=5, fill="#4c1"))

    # Custom font style
    font_size = "12px"
    font_weight = "bold"

    # Include the font style from the URL
    custom_font_style = f"""
        @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');
        text {{
            font-family: 'Source Code Pro', monospace;
            font-size: {font_size};
            font-weight: {font_weight};
            fill: white;
        }}
    """
    dwg.add(dwg.style(custom_font_style))

    # Badge text with custom font
    dwg.add(dwg.text(version, insert=(12, 14)))

    return dwg.tostring()

