<h1 align="center">Hi 👋, I'm Aadhithyaa S G</h1>
<h3 align="center">🚀 Embedded (R&D) Engineer | Verilog Specialist | SystemVerilog Beginner</h3>

---

<!-- 🌟 MATRIX BACKGROUND -->
<div align="center">
  <canvas id="matrix"></canvas>
</div>

<script>
  const canvas = document.getElementById("matrix");
  const ctx = canvas.getContext("2d");

  canvas.height = 300;
  canvas.width = window.innerWidth;

  const letters = "01";
  const fontSize = 12;
  const columns = canvas.width / fontSize;
  const drops = [];

  for (let x = 0; x < columns; x++) {
    drops[x] = 1;
  }

  function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0"; // Green matrix
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
      const text = letters[Math.floor(Math.random() * letters.length)];
      ctx.fillText(text, i * fontSize, drops[i] * fontSize);

      if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
  }

  setInterval(draw, 35);
</script>

---

## 🌟 About Me
- 🔭 Working as an **Embedded R&D Engineer**  
- 💡 Specialized in **Verilog (RTL Design)** and **SystemVerilog (Beginner)**  
- ⚡ Passionate about **Digital Electronics, RTL Design, and EV Systems**  
- 📍 Based in **Hosur, Tamil Nadu**

---

## 🏆 Highlighted Projects

### 🔹 Landslide Early Detection and Alerting System *(Main Project)*  
- 🛰️ **Machine learning + sensor-based system** to detect landslides *1 hour in advance*  
- 📊 Integrated **real-time environmental sensor data**  
- 🏅 Won **₹7,000 cash award** + certificate for efficiency  
- 🌍 Helps prevent **loss of life and property** in hilly regions  

---

### 🔹 Ride Guard EV (with Raptee Startup EV)  
- 🚦 IoT system to detect **accident-prone zones**  
- 📡 Auto SOS alerts with **ML-based risk prediction**  

---

### 🔹 Asynchronous FIFO (Low-Power Design)  
- 🔋 Implemented **clock gating + voltage scaling**  
- 🔄 Optimized data transfer between clock domains  

---

## 💻 Technical Skills
- **Languages:** Verilog, SystemVerilog (Beginner), Python, Java, SQL  
- **Tools:** AMD Vivado, Xilinx ISE, Microwind, LTSpice  
- **Domains:** RTL Design, Digital Electronics, IoT Systems  

---

## 📫 Connect with Me
<p align="center">
  <a href="https://www.linkedin.com/in/aadhithyaasg/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Aadhithyaa%20S%20G-blue?logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/SGA-15" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-SGA--15-black?logo=github" />
  </a>
</p>
