import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio

# Load black-and-white face image
face_img_path = "hacker_face.png"  # Place your face image here
face_img = Image.open(face_img_path).convert("L")
face_img = face_img.resize((80, 80))
face_array = np.array(face_img)
face_mask = face_array < 128

# GIF parameters
width, height = face_img.size
font_size = 6
columns = width
drops = np.random.randint(-20, 0, size=columns)
frames_count = 50
font = ImageFont.load_default()
frames = []

for _ in range(frames_count):
    img = Image.new("RGB", (width*font_size, height*font_size), "black")
    draw = ImageDraw.Draw(img)
    
    for x in range(columns):
        y_pos = drops[x]
        if y_pos < height:
            char = np.random.choice(['0', '1'])
            if face_mask[y_pos, x] or np.random.random() < 0.05:
                draw.text((x*font_size, y_pos*font_size), char, fill=(0,255,0), font=font)
        drops[x] += 1
        if drops[x] >= height:
            drops[x] = np.random.randint(-20, 0)
    
    frames.append(img)

frames[0].save("matrix_hacker_face.gif",
               save_all=True,
               append_images=frames[1:],
               duration=80,
               loop=0,
               optimize=True)

print("✅ matrix_hacker_face.gif generated successfully!")
