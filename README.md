# Hi 👋 I'm Aadhithyaa S G

<h3 align="center"><b>⚡ Embedded R&D Engineer | Verilog Specialist | SystemVerilog Beginner | VLSI & RTL Enthusiast ⚡</b></h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Times+New+Roman&size=24&pause=1000&color=00FFAB&center=true&vCenter=true&width=760&lines=Embedded+R%26D+Engineer;VLSI+%26+RTL+Design;FPGA+Prototyping+%7C+SystemVerilog;Hardware+%2B+Software+Integration" alt="typing" />
</p>

<!-- MATRIX BACKGROUND -->
<style>
  body { 
    margin:0; padding:0; background:#000; color:#00FFAB; font-family: 'Times New Roman', serif; overflow-x:hidden; 
  }
  #matrix { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; }
  .content { position: relative; z-index: 1; padding: 40px; max-width: 1000px; margin:auto; }
  a { color: #00FFAB; text-decoration: none; font-weight: bold; }
  h2,h3,h4 { color:#00FFAB; font-weight:bold; }
  .tech-icons img { margin: 5px; height:50px; vertical-align:middle; }
</style>

<canvas id="matrix"></canvas>

<script>
const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

const letters = "01";
const fontSize = 16;
let columns = Math.floor(canvas.width / fontSize);
let drops = Array.from({length: columns}, () => Math.floor(Math.random() * canvas.height / fontSize));

function drawMatrix() {
  ctx.fillStyle = "rgba(0,0,0,0.05)";
  ctx.fillRect(0,0,canvas.width,canvas.height);

  ctx.fillStyle = "#0F0";
  ctx.font = fontSize + "px 'Times New Roman'";

  drops.forEach((y, i) => {
    const text = letters[Math.floor(Math.random() * letters.length)];
    ctx.fillText(text, i * fontSize, y * fontSize);

    // reset drop to top randomly for smooth continuous flow
    drops[i] = y * fontSize > canvas.height && Math.random() > 0.975 ? 0 : y + 1;
  });
}

setInterval(drawMatrix, 35);
</script>

<div class="content">

## 👨‍🔧 About Me
I am a dynamic <b>Embedded R&D Engineer</b> with expertise in <b>Verilog, SystemVerilog, FPGA prototyping, RTL design, and hardware-software integration</b>.  
I bridge <b>embedded systems and semiconductor design</b>, delivering real-time, product-oriented solutions.

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
<p class="tech-icons" align="center">
  <!-- Verilog icon from UXWing -->
  <img src="https://uxwing.com/wp-content/themes/uxwing/download/technology-software/verilog-code-file-icon.png" alt="Verilog"/>
  <!-- SystemVerilog icon (can reuse Verilog if custom not available) -->
  <img src="https://uxwing.com/wp-content/themes/uxwing/download/technology-software/verilog-code-file-icon.png" alt="SystemVerilog"/>
  <img src="https://skillicons.dev/icons?i=python,c,cpp,arduino,git,github,linux" alt="other tech icons"/>
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

</div>
