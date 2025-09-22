# Hi 👋 I'm Aadhithyaa S G

<h3 align="center">⚡ Embedded R&D Engineer | Verilog Specialist | SystemVerilog Beginner | VLSI & RTL Enthusiast ⚡</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00FFAB&center=true&vCenter=true&width=760&lines=Embedded+R%26D+Engineer;VLSI+%26+RTL+Design;FPGA+Prototyping+%7C+SystemVerilog;Hardware+%2B+Software+Integration" alt="typing" />
</p>

---

<!-- MATRIX BACKGROUND -->
<style>
  body { margin:0; padding:0; background:#000; color:#00FFAB; font-family: monospace; }
  #matrix { position: fixed; top:0; left:0; z-index:-1; }
  .content { position: relative; z-index: 1; padding: 20px; }
  a { color: #00FFAB; text-decoration: none; }
</style>

<canvas id="matrix"></canvas>

<script>
  const canvas = document.getElementById("matrix");
  const ctx = canvas.getContext("2d");
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const letters = "01";
  const fontSize = 14;
  const columns = canvas.width / fontSize;
  const drops = Array.from({length: columns}, () => 1);

  function drawMatrix() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "#0F0";
    ctx.font = fontSize + "px monospace";

    drops.forEach((y, i) => {
      const text = letters[Math.floor(Math.random() * letters.length)];
      ctx.fillText(text, i * fontSize, y * fontSize);
      drops[i] = y * fontSize > canvas.height && Math.random() > 0.975 ? 0 : y + 1;
    });
  }
  setInterval(drawMatrix, 35);
</script>

<div class="content">

## 👨‍🔧 About Me
I am a dynamic **Embedded R&D Engineer** with expertise in **Verilog, FPGA prototyping, RTL design, and hardware-software integration**.  
I bridge **embedded systems and semiconductor design**, delivering real-time, product-oriented solutions.

**Core strengths:** digital design, RTL verification, FPGA prototyping, embedded firmware, hardware debugging, R&D.

---

## 🏆 Highlighted Projects

### 🔹 Landslide Early Detection and Alerting System *(Main Project)*
- 🛰️ ML + sensor-based system detects **landslides 1 hour in advance**  
- 📊 Real-time environmental sensor integration  
- 🏅 Won **₹7,000 cash award**  
- 🌍 Helps prevent **loss of life and property** in hilly regions

### 🔹 Raptee T30 EV / Ride Guard EV
- 🚦 IoT system detects **accident-prone zones**  
- 📡 Auto SOS alerts with **ML-based risk prediction**

### 🔹 Asynchronous FIFO (Low-Power Design)
- 🔋 Clock gating + voltage scaling  
- 🔄 Optimized data transfer between clock domains  

---

## 💻 Technical Skills
- **Languages:** Verilog, SystemVerilog (Beginner), Python, C, C++, SQL  
- **Tools:** AMD Vivado, Xilinx ISE, Microwind, LTSpice  
- **Domains:** RTL Design, FPGA Prototyping, Embedded Firmware, IoT Systems  

---

## 🌐 Connect with Me
<p align="center">
  <a href="https://www.linkedin.com/in/aadhithyaasg/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Aadhithyaa%20S%20G-blue?logo=linkedin&logoColor=white" /></a>
  &nbsp;
  <a href="https://github.com/SGA-15" target="_blank"><img src="https://img.shields.io/badge/GitHub-SGA--15-black?logo=github" /></a>
</p>

---

## 📊 GitHub Stats
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=SGA-15&show_icons=true&count_private=true&theme=radical" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=SGA-15&layout=compact&theme=radical" />
</p>

</div>
