from PIL import Image, ImageDraw, ImageOps, ImageChops
import os

def process_favicon():
    img_path = r'c:\web\ezvideo\favicon.png'
    img = Image.open(img_path).convert("RGBA")
    
    # Get image data
    data = img.getdata()
    
    # Find bounding box of non-white content
    new_data = []
    # If a pixel is very close to white, make it completely transparent (if it's the outer border)
    # A simpler approach: trim the white border
    bg = Image.new(img.mode, img.size, (255, 255, 255, 255))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    if bbox:
        img = img.crop(bbox)
        
    # Now that it's cropped to the actual icon content, let's create a squircle/circle mask
    size = min(img.size)
    # Crop to exact square from center
    left = (img.size[0] - size)/2
    top = (img.size[1] - size)/2
    right = (img.size[0] + size)/2
    bottom = (img.size[1] + size)/2
    img = img.crop((left, top, right, bottom))
    
    # Make a squircle mask
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size, size), radius=size//4, fill=255)
    
    # Apply the mask
    img.putalpha(mask)
    
    # Resize to standard favicon sizes (save as 256x256)
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    img.save(img_path, "PNG")
    print("Favicon processed and white border removed successfully.")

if __name__ == '__main__':
    process_favicon()
