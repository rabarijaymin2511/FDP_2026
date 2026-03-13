<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhishek Jeughale | Portfolio</title>
  <style>
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background-color: #f7f9fc;
      color: #333;
    }
    header {
      background: #007bff;
      color: white;
      padding: 20px 0;
      text-align: center;
    }
    nav {
      display: flex;
      justify-content: center;
      background: #0056b3;
      padding: 10px 0;
    }
    nav a {
      color: white;
      margin: 0 15px;
      text-decoration: none;
      font-weight: 500;
    }
    nav a:hover {
      text-decoration: underline;
    }
    section {
      padding: 50px 20px;
      max-width: 1000px;
      margin: auto;
    }
    h2 {
      color: #0056b3;
      border-bottom: 3px solid #007bff;
      display: inline-block;
      margin-bottom: 20px;
    }
    .btn {
      display: inline-block;
      padding: 10px 20px;
      background: #007bff;
      color: white;
      text-decoration: none;
      border-radius: 5px;
      margin-top: 10px;
    }
    .btn:hover {
      background: #0056b3;
    }
    .project {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    footer {
      text-align: center;
      background: #007bff;
      color: white;
      padding: 20px;
      margin-top: 40px;
    }
    @media(max-width:600px) {
      nav { flex-wrap: wrap; }
      section { padding: 30px 10px; }
    }
  </style>
</head>
<body>

  <header>
    <h1>Abhishek Jeughale</h1>
    <p>Full Stack Developer | Data Analytics with AI</p>
  </header>

  <nav>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#achievements">Achievements</a>
    <a href="#contact">Contact</a>
  </nav>

  <!-- Hero Section -->
  <section id="home">
    <h2>Welcome 👋</h2>
    <p>Hello! I’m <b>Abhishek Jeughale</b>, a passionate developer who loves creating web applications, solving problems, and learning emerging technologies like AI and Data Analytics.</p>
    <a href="#projects" class="btn">View My Projects</a>
    <a href="Abhishek_Resume.pdf" class="btn" download>Download Resume</a>
  </section>

  <!-- About Section -->
  <section id="about">
    <h2>About Me</h2>
    <p>I’m currently pursuing my degree in Computer Science and have completed a course in Data Analytics with AI. I enjoy building efficient backend systems and engaging frontends.</p>
  </section>

  <!-- Skills Section -->
  <section id="skills">
    <h2>Skills</h2>
    <ul>
      <li><b>Frontend:</b> HTML, CSS, JavaScript, React</li>
      <li><b>Backend:</b> Node.js, Express, PHP</li>
      <li><b>Database:</b> MongoDB, MySQL</li>
      <li><b>Tools:</b> Git, VS Code, Postman, Figma</li>
    </ul>
  </section>

  <!-- Projects Section -->
  <section id="projects">
    <h2>Projects</h2>

    <div class="project">
      <h3>🛒 VibeCart</h3>
      <p>An e-commerce platform like Flipkart built using Node.js, Express, and MongoDB.</p>
      <p><b>Features:</b> User login, product filtering, cart, and admin dashboard.</p>
      <a href="#" class="btn">View on GitHub</a>
    </div>

    <div class="project">
      <h3>🌾 Fresh Farm+</h3>
      <p>A crop consulting and marketplace platform for farmers integrating AI-powered recommendations and community support.</p>
      <p><b>Tech Stack:</b> HTML, CSS, JS, Firebase</p>
      <a href="#" class="btn">View on GitHub</a>
    </div>
  </section>

  <!-- Achievements Section -->
  <section id="achievements">
    <h2>Achievements</h2>
    <ul>
      <li>Completed 100 Days of LeetCode Challenge 💻</li>
      <li>Certified in Data Analytics with AI</li>
      <li>Built full-stack apps using Node.js and MongoDB</li>
    </ul>
  </section>

  <!-- Contact Section -->
  <section id="contact">
    <h2>Contact Me</h2>
    <p>📧 <a href="mailto:abhishekjeughale@example.com">abhishekjeughale@example.com</a></p>
    <p>🔗 
      <a href="https://linkedin.com/in/abhishekjeughale" target="_blank">LinkedIn</a> |
      <a href="https://github.com/abhishekjeughale" target="_blank">GitHub</a>
    </p>
  </section>

  <footer>
    <p>©️ 2026 Pushkar Nikam | All Rights Reserved</p>
  </footer>

  <script>
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
          behavior: "smooth"
        });
      });
    });
  </script>

</body>
</html>
