from PIL import Image, ImageDraw, ImageFont

def get_text_width(text, font_path, font_size):
    image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    width, _ = draw.textsize(text, font)
    return width

# Example usage
font_path = "https://fonts.gstatic.com/s/sourcecodepro/v23/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DMyQtMlrTA.woff2"
font_size = 14
text = "Hello, World!"
width = get_text_width(text, font_path, font_size)
print(f"Width of '{text}': {width} pixels")
