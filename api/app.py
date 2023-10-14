from fastapi import FastAPI, Path, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from svgwrite import Drawing
import datetime

app = FastAPI()

# Mounting the subfolder as a static directory
app.mount("/static", StaticFiles(directory="./api/static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/{file_name}")
def get_svg(file_name: str = Path(..., title="The name of your SVG file")):
    file_path = f"static/{file_name}.svg"
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


@app.get("/badge/{text}")
async def get_version_badge(text:str):
    # Replace this with your actual version retrieval logic
    version = "abcde"

    svg_content = generate_custom_font_badge(text)
    response = Response(content=svg_content, media_type="image/svg+xml")
    response.headers["Cache-Control"] = "no-cache"  # Avoid caching for dynamic content
    return response
    
    # Return the SVG file as a response
    return FileResponse(file_path, media_type="image/svg+xml")
