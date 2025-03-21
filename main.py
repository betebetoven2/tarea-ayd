from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Información Personal")

# Crear directorio para archivos estáticos si no existe
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)

# Crear archivo CSS
css_dir = os.path.join(static_dir, "css")
os.makedirs(css_dir, exist_ok=True)
with open(os.path.join(css_dir, "styles.css"), "w") as f:
    f.write("""
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    :root {
        --primary: #4776E6;
        --secondary: #8E54E9;
        --dark: #131a36;
        --light: #f5f5f5;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
    }

    body {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        color: var(--light);
        overflow: hidden;
        position: relative;
    }

    body::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.3/particles.min.js') no-repeat center center/cover;
        opacity: 0.1;
        z-index: -1;
    }

    .container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        width: 90%;
        max-width: 600px;
        transform-style: preserve-3d;
        perspective: 1000px;
        transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .container:hover {
        transform: translateY(-5px) rotateX(5deg) rotateY(5deg);
    }

    h1 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(to right, #fff, #aaa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        position: relative;
    }

    h1::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 50px;
        height: 3px;
        background: linear-gradient(to right, var(--primary), var(--secondary));
        border-radius: 10px;
    }

    .info-container {
        margin: 2rem 0;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    .visible {
        opacity: 1;
        transform: translateY(0);
    }

    .info-item {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
        transform: translateX(-20px);
        opacity: 0;
    }

    .info-item.animate {
        transform: translateX(0);
        opacity: 1;
    }

    .info-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: scale(1.02);
    }

    .info-item i {
        font-size: 1.5rem;
        margin-right: 1rem;
        color: var(--secondary);
    }

    .info-label {
        font-weight: 600;
        margin-right: 0.5rem;
    }

    .btn {
        display: block;
        width: 100%;
        padding: 1rem;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border: none;
        border-radius: 50px;
        color: white;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }

    .btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0%;
        height: 100%;
        background: linear-gradient(135deg, var(--secondary), var(--primary));
        transition: all 0.5s ease;
        z-index: -1;
        border-radius: 50px;
    }

    .btn:hover::before {
        width: 100%;
    }

    .btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }

    .btn:active {
        transform: translateY(-1px);
    }

    .particles {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    .floating {
        animation: floating 3s ease-in-out infinite;
    }

    @keyframes floating {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }

    .circle {
        position: absolute;
        border-radius: 50%;
        background: linear-gradient(to right, var(--primary), var(--secondary));
        opacity: 0.2;
        filter: blur(20px);
        z-index: -1;
        animation: pulse 4s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    }

    .circle-1 {
        width: 300px;
        height: 300px;
        top: -150px;
        left: -150px;
    }

    .circle-2 {
        width: 200px;
        height: 200px;
        bottom: -100px;
        right: -100px;
        animation-delay: -1s;
    }

    @keyframes pulse {
        0% {
            transform: scale(0.8);
            opacity: 0.2;
        }
        50% {
            transform: scale(1);
            opacity: 0.4;
        }
        100% {
            transform: scale(0.8);
            opacity: 0.2;
        }
    }

    .fade-in {
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    /* Añadir animación de typing al título */
    .typing {
        position: relative;
    }

    .typing::after {
        content: '|';
        position: absolute;
        right: -8px;
        color: white;
        animation: blink 0.7s infinite;
    }

    @keyframes blink {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0;
        }
    }

    /* Animación para el botón */
    .btn-pulse {
        animation: btnPulse 2s infinite;
    }

    @keyframes btnPulse {
        0% {
            box-shadow: 0 0 0 0 rgba(142, 84, 233, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(142, 84, 233, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(142, 84, 233, 0);
        }
    }
    """)

# Crear archivo JS
js_dir = os.path.join(static_dir, "js")
os.makedirs(js_dir, exist_ok=True)
with open(os.path.join(js_dir, "scripts.js"), "w") as f:
    f.write("""
    document.addEventListener('DOMContentLoaded', function() {
        const button = document.getElementById('show-info');
        const infoContainer = document.getElementById('info-container');
        const infoItems = document.querySelectorAll('.info-item');
        const title = document.querySelector('h1');
        let titleText = title.textContent;
        
        // Animación de typing para el título
        title.textContent = '';
        title.classList.add('typing');
        let i = 0;
        
        function typeWriter() {
            if (i < titleText.length) {
                title.textContent += titleText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                title.classList.remove('typing');
            }
        }
        
        setTimeout(typeWriter, 500);
        
        // Añadir clase para animar el botón
        setTimeout(() => {
            button.classList.add('btn-pulse');
        }, 1500);
        
        // Manejar clic en el botón
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Toggle visibilidad del contenedor de información
            infoContainer.classList.toggle('visible');
            
            if (infoContainer.classList.contains('visible')) {
                button.textContent = 'Ocultar Información';
                
                // Animar cada elemento de información con retraso
                infoItems.forEach((item, index) => {
                    setTimeout(() => {
                        item.classList.add('animate');
                    }, 200 * index);
                });
            } else {
                button.textContent = 'Mostrar Información';
                
                // Restablecer animaciones
                infoItems.forEach(item => {
                    item.classList.remove('animate');
                });
            }
        });
        
        // Crear efecto de partículas
        particlesJS('particles', {
            particles: {
                number: {
                    value: 80,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: '#ffffff'
                },
                shape: {
                    type: 'circle',
                    stroke: {
                        width: 0,
                        color: '#000000'
                    },
                    polygon: {
                        nb_sides: 5
                    }
                },
                opacity: {
                    value: 0.5,
                    random: false,
                    anim: {
                        enable: false,
                        speed: 1,
                        opacity_min: 0.1,
                        sync: false
                    }
                },
                size: {
                    value: 3,
                    random: true,
                    anim: {
                        enable: false,
                        speed: 40,
                        size_min: 0.1,
                        sync: false
                    }
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#ffffff',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 3,
                    direction: 'none',
                    random: false,
                    straight: false,
                    out_mode: 'out',
                    bounce: false,
                    attract: {
                        enable: false,
                        rotateX: 600,
                        rotateY: 1200
                    }
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'grab'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                },
                modes: {
                    grab: {
                        distance: 140,
                        line_linked: {
                            opacity: 1
                        }
                    },
                    bubble: {
                        distance: 400,
                        size: 40,
                        duration: 2,
                        opacity: 8,
                        speed: 3
                    },
                    repulse: {
                        distance: 200,
                        duration: 0.4
                    },
                    push: {
                        particles_nb: 4
                    },
                    remove: {
                        particles_nb: 2
                    }
                }
            },
            retina_detect: true
        });
        
        // Añadir efecto 3D al mover el ratón
        const container = document.querySelector('.container');
        
        document.addEventListener('mousemove', function(e) {
            const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
            const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
            container.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
        });
        
        // Efecto al entrar/salir del contenedor
        container.addEventListener('mouseenter', function() {
            container.style.transition = 'none';
        });
        
        container.addEventListener('mouseleave', function() {
            container.style.transition = 'all 0.5s ease';
            container.style.transform = 'rotateY(0deg) rotateX(0deg)';
        });
    });
    """)

# Configurar archivos estáticos
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# HTML con CSS y JS externos
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información Personal</title>
    <link rel="stylesheet" href="/static/css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.3/particles.min.js"></script>
</head>
<body>
    <div id="particles" class="particles"></div>
    
    <div class="circle circle-1"></div>
    <div class="circle circle-2"></div>
    
    <div class="container fade-in">
        <h1 class="floating">Información Personal</h1>
        
        <div id="info-container" class="info-container">
            <div class="info-item">
                <i class="fas fa-user"></i>
                <span class="info-label">Nombre:</span>
                <span class="info-value">Alberto Josué Hernández Armas</span>
            </div>
            
            <div class="info-item">
                <i class="fas fa-id-card"></i>
                <span class="info-label">Carnet:</span>
                <span class="info-value">201903553</span>
            </div>
            
            <div class="info-item">
                <i class="fas fa-book"></i>
                <span class="info-label">Curso:</span>
                <span class="info-value">Análisis y Diseño de Sistemas 1</span>
            </div>
        </div>
        
        <button id="show-info" class="btn">Mostrar Información</button>
    </div>
    
    <script src="/static/js/scripts.js"></script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content
