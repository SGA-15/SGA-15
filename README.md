# Hi 👋 I'm Aadhithyaa S G

<h3 align="center"><b>⚡ Embedded R&D Engineer | Verilog Specialist | SystemVerilog Beginner | VLSI & RTL Enthusiast ⚡</b></h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Times+New+Roman&size=24&pause=1000&color=00FFAB&center=true&vCenter=true&width=760&lines=Embedded+R%26D+Engineer;VLSI+%26+RTL+Design;FPGA+Prototyping+%7C+SystemVerilog;Hardware+%2B+Software+Integration" alt="typing" />
</p>

<!-- MATRIX GIF HEADER -->
<p align="center">
  <img src="https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif" alt="Matrix Rain" width="100%" />
</p>

---

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio

# === Step 1: Load your face image (black & white) ===
face_img_path = "hacker_face.png"  # Use a small 100x100 or similar image
face_img = Image.open(face_img_path).convert("L")  # grayscale
face_img = face_img.resize((80, 80))              # resize for smaller GIF
face_array = np.array(face_img)

# Threshold to create mask (face area)
face_mask = face_array < 128  # True = part of the face

# === Step 2: GIF parameters ===
width, height = face_img.size
font_size = 6               # small font for lightweight GIF
columns = width
drops = np.random.randint(-20, 0, size=columns)
frames_count = 50           # total frames
font = ImageFont.load_default()
frames = []

# === Step 3: Generate frames ===
for _ in range(frames_count):
    img = Image.new("RGB", (width*font_size, height*font_size), "black")
    draw = ImageDraw.Draw(img)
    
    for x in range(columns):
        y_pos = drops[x]
        if y_pos < height:
            char = np.random.choice(['0', '1'])
            # Draw char in face area or add sparse outside for effect
            if face_mask[y_pos, x] or np.random.random() < 0.05:
                draw.text((x*font_size, y_pos*font_size), char, fill=(0,255,0), font=font)
        drops[x] += 1
        if drops[x] >= height:
            drops[x] = np.random.randint(-20, 0)
    
    frames.append(img)

# === Step 4: Save GIF optimized for GitHub ===
frames[0].save("matrix_hacker_face.gif",
               save_all=True,
               append_images=frames[1:],
               duration=80,   # speed
               loop=0,
               optimize=True)


## 👨‍🔧 About Me
I am a dynamic **Embedded R&D Engineer** with expertise in **Verilog, SystemVerilog, FPGA prototyping, RTL design, and hardware-software integration**.  
I bridge **embedded systems and semiconductor design**, delivering real-time, product-oriented solutions.

**Core strengths:** digital design, RTL verification, FPGA prototyping, embedded firmware, hardware debugging, R&D.

---

## 🏆 Highlighted Projects

<p align="center">
  <a href="https://github.com/SGA-15/AI-Driven-Landslide-Early-Detection-and-Alerting-System" 
     title="🛰️ ML + sensor-based system to detect landslides 1 hour in advance. Real-time environmental sensor integration. Won ₹7,000 cash award. Helps prevent loss of life and property in hilly regions.">
     🔹 Landslide Early Detection & Alerting System
  </a><br/>
  <a href="https://github.com/SGA-15/Raptee-T30-EV" 
     title="🚦 EV project with IoT features. Accident-prone zone detection, auto SOS alerts, and ML-based risk prediction. Embedded firmware, CAN/BMS interface, and hardware control algorithms.">
     🔹 Raptee T30 EV / Ride Guard EV
  </a><br/>
  <a href="https://github.com/SGA-15/Auto-Rechargeable-Electric-Vehicle" 
     title="⚡ Auto Rechargeable Electric Vehicle project. Embedded control and energy management with hardware-software integration.">
     🔹 Auto Rechargeable Electric Vehicle
  </a><br/>
  <a href="https://github.com/SGA-15/Spectacles-for-Blind-People" 
     title="👓 Assistive vision prototype. Sensor integration + embedded processing for visually impaired people.">
     🔹 Spectacles for Blind People
  </a><br/>
  <a href="https://github.com/SGA-15/Bus-Security-System-Using-RFID-Technology" 
     title="🚌 Embedded access control system using RFID technology. Secure bus entry and monitoring.">
     🔹 Bus Security System Using RFID Technology
  </a>
</p>

<p align="center">
  <a href="https://github.com/SGA-15" target="_blank">
    <img src="https://img.shields.io/badge/View%20All%20Projects-GitHub-black?logo=github" />
  </a>
</p>

---

## 💻 Technical Skills
<p align="center">
  <!-- Verilog icon from UXWing -->
  <img src="https://uxwing.com/wp-content/themes/uxwing/download/technology-software/verilog-code-file-icon.png" alt="Verilog" height="50"/>
  <!-- SystemVerilog icon (can reuse Verilog if custom not available) -->
  <img src="https://uxwing.com/wp-content/themes/uxwing/download/technology-software/verilog-code-file-icon.png" alt="SystemVerilog" height="50"/>
  <img src="https://skillicons.dev/icons?i=python,c,cpp,arduino,git,github,linux" alt="other tech icons" height="50"/>
</p>

---

## 🌐 Connect with Me
<p align="center">
  <a href="https://www.linkedin.com/in/aadhithyaasg/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Aadhithyaa%20S%20G-blue?logo=linkedin&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://github.com/SGA-15" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-SGA--15-black?logo=github" />
  </a>
</p>

---

## 📊 GitHub Stats
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=SGA-15&show_icons=true&count_private=true&theme=radical" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=SGA-15&layout=compact&theme=radical" />
</p>
