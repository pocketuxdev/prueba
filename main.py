from fasthtml.common import *
import os

# Application initialization
app, rt = fast_app()

# Static file handling
@rt('/static/images/<path:filename>')
def serve_image(filename):
    """Serve static images from the static/images directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, 'static', 'images', filename)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return f.read(), 200, {'Content-Type': 'image/png'}
    return 'Image not found', 404

def get_common_sidebar():
    """Retorna el HTML y estilos comunes para la barra lateral"""
    return """
    <!-- Estilos comunes del Sidebar -->
    <style>
        /* Sidebar Styles */
        .sidebar {
            position: fixed;
            bottom: 1rem; /* Cambiado de 2rem a 1rem para bajar más el sidebar */
            left: 50%;
            transform: translateX(-50%);
            height: 60px;
            background: rgba(40, 40, 40, 0.95);
            background: rgba(40, 40, 40, 0.75);
            padding: 0 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.5rem;
            backdrop-filter: blur(8px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            border-radius: 20px;
            width: auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        /* Ajustar el padding-bottom del contenido principal */
        .dashboard-layout {
            padding-bottom: 80px; /* Aumentado para dar más espacio al sidebar */
        }
        @media (max-width: 768px) {
            .sidebar {
                bottom: 0.5rem; /* Ajustado para móviles */
                padding: 0.5rem 1rem;
                gap: 1rem;
            }
            .dashboard-layout {
                padding-bottom: 70px; /* Ajustado para móviles */
            }
        }
        /* Resto de los estilos del sidebar se mantienen igual */
        .sidebar-logo {
            width: 40px;
            height: auto;
            filter: brightness(1.2) drop-shadow(0 0 10px rgba(255, 0, 153, 0.5));
            transition: all 0.3s ease;
        }
        .sidebar-logo:hover {
            transform: scale(1.1);
        }
        .nav-item {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            color: var(--text-light);
            background: rgba(255, 255, 255, 0.1);
            background: rgba(255, 255, 255, 0.08); /* Items más transparentes */
        }
        .nav-item:hover {
            background: var(--primary-hover);
            transform: translateY(-3px);
        }
        .nav-item.active {
            background: var(--primary-color);
            color: white;
        }
        .nav-item::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 120%;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 10px;
            font-size: 0.85rem;
            white-space: nowrap;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-color);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .nav-item:hover::after {
            opacity: 1;
            visibility: visible;
            bottom: 110%;
        }
        .dashboard-layout {
            display: grid;
            grid-template-columns: 1fr;
            height: 100vh;
            max-width: 100vw; /* Agregar ancho máximo viewport */
            margin: 0 auto;
            padding: 0.5rem 1rem; /* Reducido aún más */
            overflow-y: auto; /* Restaurar scroll vertical */
            overflow-x: hidden;
        }
        @media (max-width: 768px) {
            .dashboard-layout {
                padding: 1rem 1rem 100px 1rem;
                width: 100vw;
                overflow-x: hidden;
            }
            
            .header {
                background: rgba(0, 0, 0, 0.7);
                border-radius: 20px;
                margin-bottom: 1.5rem;
            }
            
            .header h1 {
                font-size: 1.5rem;
                font-family: 'Playfair Display', serif;
            }
            
            .kpi-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 1.5rem;
                margin-bottom: 2rem;
            }
            
            .kpi-card {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                padding: 1.5rem;
                border: 1px solid var(--border-color);
                height: auto;
            }
            
            .kpi-value {
                font-size: 2.5rem;
                color: var(--primary-color);
                text-align: center;
                margin-bottom: 0.5rem;
            }
            
            .kpi-label {
                font-size: 1rem;
                color: var(--text-light);
                text-align: center;
            }
            
            .metrics-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 1.5rem;
                padding: 0.5rem;
            }
            
            .metric-card {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                padding: 1.5rem;
                border: 1px solid var(--border-color);
                aspect-ratio: 1.2; /* Mantiene una proporción consistente */
                height: auto;
                width: 100%;
            }
            
            .chart-title {
                color: white;
                font-size: 1.4rem;
                text-align: center;
                margin-bottom: 1.5rem;
                font-weight: 500;
                font-family: 'Playfair Display', serif;
            }
            
            .chart-container {
                position: relative;
                width: 100%;
                height: 280px;
                height: 0;
                padding-bottom: 75%; /* Mantiene una proporción 4:3 */
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            canvas {
                position: absolute;
                top: 0;
                left: 0;
                width: 100% !important;
                height: 100% !important;
                object-fit: contain;
            }
            
            /* Ajustes específicos para cada tipo de gráfica */
            .metric-card[data-chart="line"] .chart-container,
            .metric-card[data-chart="bar"] .chart-container {
                height: 200px;
            }
            
            .metric-card[data-chart="bar"] .chart-container,
            .metric-card[data-chart="doughnut"] .chart-container,
            .metric-card[data-chart="pie"] .chart-container {
                height: 220px;
                padding-bottom: 75%; /* Mantiene la misma proporción para todos los tipos */
            }
            
            .chart-title {
                font-size: 1.1rem;
                margin-bottom: 1rem;
                color: white;
                text-align: center;
            }
            
            /* Ajustes para las tarjetas KPI */
            .kpi-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 1rem;
                margin-bottom: 1.5rem;
            }
            
            .kpi-card {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
            }
            
            .kpi-value {
                font-size: 2.5rem;
                color: var(--primary-color);
                margin-bottom: 0.5rem;
            }
            
            .kpi-label {
                font-size: 1rem;
                color: var(--text-light);
            }
            
            .sidebar {
                background: rgba(40, 40, 40, 0.95);
                padding: 0.5rem 1rem;
                gap: 1rem;
            }
            
            .nav-item {
                width: 35px;
                height: 35px;
            }
            
            .sidebar-logo {
                width: 35px;
            }
        }
        /* Ajustes para tablets */
        @media (min-width: 769px) and (max-width: 1024px) {
            .dashboard-layout {
                padding: 0 1.5rem 100px 1.5rem;
            }
            .metrics-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .chart-container {
                height: 300px;
            }
            .calendar-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        /* Ajustes específicos para las gráficas */
        .chart-container {
            position: relative;
            width: 100%;
            height: 300px; /* Aumentado de 180px a 300px */
            background: rgba(255, 255, 255, 0.02);
            border-radius: 15px;
            border: 1px solid rgba(255, 0, 153, 0.1);
            padding: 1.5rem; /* Aumentado padding */
            margin: 1rem auto; /* Centrado con auto */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .chart-title {
            font-size: 1.2rem;
            color: white;
            margin-bottom: 1.5rem;
            font-weight: 500;
            text-align: center; /* Centrar título */
        }
        /* Ajustes para tablets */
        @media (max-width: 1200px) {
            .chart-container {
                height: 350px; /* Aún más alto en tablets */
            }
        }
        /* Ajustes para móvil */
        @media (max-width: 768px) {
            .chart-container {
                height: 400px; /* Máxima altura en móvil */
                padding: 1rem;
                margin: 1rem auto;
                width: 95%; /* Dar un pequeño margen en los bordes */
            }
            
            canvas {
                width: 100% !important;
                height: 100% !important;
                max-width: none !important;
            }
            
            .chart-title {
                font-size: 1.1rem;
                padding: 0;
                margin-bottom: 1rem;
            }
        }
        /* Asegurar que el contenido principal tenga espacio para el sidebar inferior */
        .main-content {
            width: 100%;
            max-width: 100vw; /* Cambiar a viewport width */
            margin: 0 auto;
            padding: 2rem 0;
        }
        /* Ajustes para el scroll */
        html, body {
            overflow-x: hidden;
            scroll-behavior: smooth;
            scroll-padding-bottom: 100px;
        }
    </style>
    <!-- HTML común del Sidebar -->
    <div class="sidebar">
        <img src="/static/images/logopocket.png" alt="Logo" class="sidebar-logo">
        <div class="nav-item" onclick="handleNavigation('dashboard')" data-tooltip="Dashboard">
            <i class="fas fa-home"></i>
        </div>
        <div class="nav-item" onclick="handleNavigation('profile')" data-tooltip="Perfil">
            <i class="fas fa-user"></i>
        </div>
        <div class="nav-item" onclick="handleNavigation('billing')" data-tooltip="Facturación">
            <i class="fas fa-file-invoice-dollar"></i>
        </div>
        <div class="nav-item" onclick="handleLogout()" data-tooltip="Cerrar Sesión">
            <i class="fas fa-sign-out-alt"></i>
        </div>
    </div>
    <!-- JavaScript común -->
    <script>
        function handleNavigation(route) {
            // Remover clase active de todos los items
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            // Agregar clase active al item actual
            const currentItem = document.querySelector(`[onclick="handleNavigation('${route}')"]`);
            if (currentItem) {
                currentItem.classList.add('active');
            }
            // Animación suave antes de la navegación
            document.body.style.opacity = '0.5';
            setTimeout(() => {
                switch(route) {
                    case 'dashboard':
                        window.location.href = '/dashboard';
                        break;
                    case 'profile':
                        window.location.href = '/profile';
                        break;
                    case 'billing':
                        window.location.href = '/billing';
                        break;
                }
            }, 200);
        }
        function handleLogout() {
            if (confirm('¿Estás seguro que deseas cerrar sesión?')) {
                localStorage.removeItem('clientData');
                window.location.href = '/';
            }
        }
        window.onload = function() {
            // Verificar autenticación
            const clientData = localStorage.getItem('clientData');
            if (!clientData) {
                window.location.href = '/';
                return;
            }
            // Activar item actual según la ruta
            const path = window.location.pathname;
            const route = path.substring(1) || 'dashboard';
            const currentItem = document.querySelector(`[onclick="handleNavigation('${route}')"]`);
            if (currentItem) {
                currentItem.classList.add('active');
            }
            // Restaurar opacidad del body
            document.body.style.opacity = '1';
        };
    </script>
    """

# Route definitions
@rt('/')
def login_page():
    return """
    <html>
        <head>
            <title>POCKET UX - Login</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="POCKET UX - Sistema de Gestión Médica">
            
            <!-- External Resources -->
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            
            <!-- Styles -->
            <style>
                /* Root Variables */
                :root {
                    --primary-color: #FF0099;
                    --primary-hover: #D6006F;
                    --background-dark: #000000;
                    --text-light: rgba(255, 255, 255, 0.8);
                    --text-lighter: rgba(255, 255, 255, 0.5);
                    --border-color: rgba(255, 0, 153, 0.2);
                }
                
                /* Reset and Base Styles */
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Poppins', sans-serif;
                }
                
                body {
                    min-height: 100vh;
                    height: 100vh;
                    width: 100vw;
                    background: var(--background-dark);
                    color: var(--text-light);
+                   overflow: hidden; /* Prevenir scroll */
                    overflow: hidden;
                }
                
                /* Layout Components */
                .container {
                    position: relative;
                    z-index: 2;
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    min-height: 100vh;
                    height: 100vh;
                    width: 100vw;
                    backdrop-filter: blur(10px);
+                   overflow: hidden; /* Prevenir scroll en el contenedor */
                    overflow: hidden;
                }
                
                /* Image Section */
                .image-section {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    position: relative;
                    overflow: hidden;
                    background: rgba(0, 0, 0, 0.5);
                }
                
                .logo {
                    width: 400px;
                    height: auto;
                    filter: brightness(1.2) drop-shadow(0 0 30px rgba(255, 0, 153, 0.7));
                    animation: logoFloat 6s ease-in-out infinite,
                              logoGlow 3s ease-in-out infinite,
                              logoRotate 12s linear infinite;
                    transform-origin: center center;
                    perspective: 1000px;
                }
                
                @keyframes logoFloat {
                    0%, 100% { transform: translateY(0) rotateY(0deg); }
                    50% { transform: translateY(-20px) rotateY(180deg); }
                }
                
                @keyframes logoGlow {
                    0%, 100% { 
                        filter: brightness(1) drop-shadow(0 0 20px rgba(255, 0, 153, 0.5)); 
                    }
                    50% { 
                        filter: brightness(1.4) drop-shadow(0 0 30px rgba(255, 0, 153, 0.7)); 
                    }
                }
                
                @keyframes logoRotate {
                    0% { transform: rotateY(0deg); }
                    100% { transform: rotateY(360deg); }
                }
                
                /* Form Section */
                .form-section {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 2rem;
                    background: rgba(255, 255, 255, 0.05); /* Agregado el fondo semi-transparente */
                }
                
                .login-container {
                    background: rgba(40, 40, 40, 0.95);
                    padding: 2.5rem;
                    border-radius: 20px;
                    width: 100%;
                    max-width: 400px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    backdrop-filter: blur(10px); /* Agregado el efecto de blur */
                }
                
                h1 {
                    color: white;
                    font-size: 2rem;
                    text-align: center;
                    margin-bottom: 2rem;
                }
                
                .form-group {
                    position: relative;
                    margin-bottom: 1.5rem;
                    background: rgba(60, 60, 60, 0.95);
                    padding: 0.8rem;
                    border-radius: 12px;
                    border: 1px solid var(--border-color);
                }
                
                .form-group i {
                    position: absolute;
                    left: 1rem;
                    top: 50%;
                    transform: translateY(-50%);
                    color: var(--primary-color);
                    font-size: 1.2rem;
                }
                
                input {
                    width: 100%;
                    background: transparent;
                    border: none;
                    color: white;
                    font-size: 0.95rem;
                    padding-left: 2.5rem;
                }
                
                input::placeholder {
                    color: var(--text-lighter);
                }
                
                input:focus {
                    outline: none;
                }
                
                button {
                    width: 100%;
                    padding: 1rem;
                    background: var(--primary-color);
                    border: none;
                    border-radius: 12px;
                    color: white;
                    font-size: 1rem;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
                
                button:hover {
                    background: var(--primary-hover);
                }
                
                /* Reset Password Link */
                .reset-password-link {
                    margin-top: 1.5rem;
                    text-align: center;
                }
                
                .reset-password-link a {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    gap: 8px;
                    color: var(--text-lighter);
                    text-decoration: none;
                    font-size: 0.9rem;
                    padding: 1rem;
                    border-radius: 12px;
                    background: rgba(60, 60, 60, 0.95);
                    border: 1px solid var(--border-color);
                    transition: all 0.3s ease;
                }
                
                .reset-password-link a:hover {
                    background: rgba(255, 0, 153, 0.15);
                }
                
                /* Media Queries */
                @media (max-width: 768px) {
                    .container {
                        grid-template-columns: 1fr;
+                       height: 100vh; /* Altura fija en móvil */
+                       overflow: hidden; /* Prevenir scroll */
                        height: 100vh;
                        width: 100vw;
                        overflow: hidden;
                    }
                    
                    .image-section {
                        display: none;
                    }
                    
                    .form-section {
                        padding: 1.5rem;
+                       height: 100vh; /* Altura fija en móvil */
+                       overflow: hidden; /* Prevenir scroll */
                        height: 100vh;
                        width: 100vw;
                        overflow: hidden;
                    }
                    
                    .login-container {
                        padding: 2rem;
+                       max-height: 100%; /* Asegurar que no exceda la altura de la pantalla */
                        max-height: 100vh;
                        width: 100%;
                    }
                    
                    h1 {
                        font-size: 1.8rem;
                        margin-bottom: 1.5rem;
                    }
                }
                /* Message Styles */
                #message {
                    margin-top: 1rem;
                    text-align: center;
                    padding: 0.8rem;
                    border-radius: 12px;
                    font-size: 0.9rem;
                    transition: all 0.3s ease;
                }
                .success {
                    background: rgba(0, 179, 104, 0.2);
                    border: 1px solid #00b368;
                    color: #00b368;
                    animation: successAnimation 0.3s ease-out forwards;
                }
                .error {
                    background: rgba(255, 0, 0, 0.2);
                    border: 1px solid #ff0000;
                    color: #ff0000;
                    animation: errorAnimation 0.3s ease-out forwards;
                }
                /* Animaciones */
                @keyframes errorAnimation {
                    0% { transform: translateX(-10px); opacity: 0; }
                    50% { transform: translateX(10px); }
                    100% { transform: translateX(0); opacity: 1; }
                }
                /* Estilos para inputs no válidos */
                input:invalid {
                    border-color: #ff0000;
                    animation: shake 0.3s ease-in-out;
                }
                @keyframes shake {
                    0%, 100% { transform: translateX(0); }
                    25% { transform: translateX(-5px); }
                    75% { transform: translateX(5px); }
                }
            </style>
        </head>
        <body>
            <!-- Main Container -->
            <div class="container">
                <!-- Logo Section -->
                <div class="image-section">
                    <img src="/static/images/logopocket.png" alt="POCKET UX Logo" class="logo">
                </div>
                
                <!-- Login Form Section -->
                <div class="form-section">
                    <div class="login-container">
                        <h1>Bienvenido</h1>
                        <form id="loginForm">
                            <div class="form-group">
                                <i class="fas fa-envelope"></i>
                                <input type="email" id="email" required placeholder="Email">
                            </div>
                            <div class="form-group">
                                <i class="fas fa-lock"></i>
                                <input type="password" id="password" required placeholder="Contraseña">
                            </div>
                            <button type="submit" id="submitButton">Ingresar</button>
                        </form>
                        <div id="message"></div>
                        <div class="reset-password-link">
                            <a href="/reset-password">
                                <i class="fas fa-key"></i>
                                ¿No recuerdas tu contraseña? ¡Recupérala aquí!
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Scripts -->
            <script>
                document.getElementById('loginForm').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    
                    const email = document.getElementById('email').value;
                    const password = document.getElementById('password').value;
                    const submitButton = document.getElementById('submitButton');
                    const messageDiv = document.getElementById('message');
                    submitButton.disabled = true;
                    submitButton.textContent = 'Iniciando sesión...';
                    try {
                        const response = await fetch('https://tifanny-back.vercel.app/v1/tifanny/loginClient', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'Accept': 'application/json'
                            },
                            credentials: 'include',
                            body: JSON.stringify({
                                email,
                                password
                            })
                        });
                        const data = await response.json();
                        if (response.ok) {
                            messageDiv.className = 'success';
                            messageDiv.innerHTML = `<p>${data.message}</p>`;
                            localStorage.setItem('clientData', JSON.stringify(data.clientData));
                            setTimeout(() => {
                                window.location.href = '/dashboard';
                            }, 1000);
                        } else {
                            messageDiv.className = 'error';
                            messageDiv.innerHTML = `<p>${data.message}</p>`;
                        }
                    } catch (error) {
                        messageDiv.className = 'error';
                        messageDiv.innerHTML = '<p>Error de conexión: ' + error.message + '</p>';
                    } finally {
                        submitButton.disabled = false;
                        submitButton.textContent = 'Ingresar';
                    }
                });
            </script>
        </body>
    </html>
    """

@rt('/dashboard')
def dashboard_page():
    charts_js = """
    Chart.defaults.color = '#fff';
    Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';
    Chart.defaults.font.size = 11;
    Chart.defaults.layout.padding = 10;
    // Opciones comunes para todos los gráficos
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: true,
        aspectRatio: 1.5,
        plugins: {
            legend: {
                position: 'top',
                labels: {
                    boxWidth: 12,
                    padding: 8
                }
            },
            title: {
                display: false
            }
        },
        scales: {
            x: {
                grid: {
                    display: false
                }
            },
            y: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                }
            }
        }
    };
    // 1. User Engagement Metrics
    const userEngagementChart = new Chart(
        document.getElementById('userEngagementChart').getContext('2d'),
        {
            type: 'line',
            data: {
                labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
                datasets: [{
                    label: 'Tasa de Engagement',
                    data: [65, 70, 75, 80, 85, 90],
                    borderColor: '#FF0099',
                    tension: 0.4,
                    fill: true,
                    backgroundColor: 'rgba(255, 0, 153, 0.1)'
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Engagement de Usuarios Activos',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 2. Automation Performance
    const automationChart = new Chart(
        document.getElementById('automationChart').getContext('2d'),
        {
            type: 'bar',
            data: {
                labels: ['Agendamiento', 'Follow-ups', 'Recordatorios', 'Onboarding'],
                datasets: [{
                    label: 'Tasa de Éxito de Automatización',
                    data: [95, 88, 92, 85],
                    backgroundColor: 'rgba(255, 0, 153, 0.5)'
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Rendimiento de Automatización',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 3. Patient Care Metrics
    const patientCareChart = new Chart(
        document.getElementById('patientCareChart').getContext('2d'),
        {
            type: 'line',
            data: {
                labels: ['8am', '10am', '12pm', '2pm', '4pm', '6pm'],
                datasets: [{
                    label: 'Tiempo de Respuesta Urgencias (min)',
                    data: [12, 8, 15, 10, 7, 13],
                    borderColor: '#FF0099',
                    tension: 0.4
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Tiempos de Respuesta en Urgencias',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 4. Operational Efficiency
    const efficiencyChart = new Chart(
        document.getElementById('efficiencyChart').getContext('2d'),
        {
            type: 'bar',
            data: {
                labels: ['Pre-Tiffany', 'Post-Tiffany'],
                datasets: [{
                    label: 'Tiempo en Tareas Administrativas (horas)',
                    data: [7.5, 5.6],
                    backgroundColor: ['rgba(255, 0, 153, 0.3)', 'rgba(255, 0, 153, 0.7)']
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Reducción de Tareas Administrativas',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 5. Training and Support
    const trainingChart = new Chart(
        document.getElementById('trainingChart').getContext('2d'),
        {
            type: 'doughnut',
            data: {
                labels: ['Completado', 'En Progreso', 'No Iniciado'],
                datasets: [{
                    data: [70, 20, 10],
                    backgroundColor: [
                        'rgba(255, 0, 153, 0.8)',
                        'rgba(255, 0, 153, 0.5)',
                        'rgba(255, 0, 153, 0.2)'
                    ]
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Estado de Capacitación del Personal',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 6. System Performance
    const systemPerformanceChart = new Chart(
        document.getElementById('systemPerformanceChart').getContext('2d'),
        {
            type: 'line',
            data: {
                labels: ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom'],
                datasets: [{
                    label: 'Uptime (%)',
                    data: [99.9, 99.8, 99.9, 99.7, 99.9, 99.9, 99.8],
                    borderColor: '#FF0099',
                    fill: true,
                    backgroundColor: 'rgba(255, 0, 153, 0.1)'
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Rendimiento del Sistema',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 7. Adoption Metrics
    const adoptionChart = new Chart(
        document.getElementById('adoptionChart').getContext('2d'),
        {
            type: 'bar',
            data: {
                labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
                datasets: [{
                    label: 'Tasa de Adopción de Nuevas Funciones (%)',
                    data: [30, 45, 65, 80],
                    backgroundColor: 'rgba(255, 0, 153, 0.5)'
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Adopción de Nuevas Funcionalidades',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    // 8. General Insights
    const insightsChart = new Chart(
        document.getElementById('insightsChart').getContext('2d'),
        {
            type: 'radar',
            data: {
                labels: ['Satisfacción', 'Engagement', 'Efectividad', 'Confianza', 'Usabilidad'],
                datasets: [{
                    label: 'Métricas Generales',
                    data: [85, 88, 92, 87, 90],
                    backgroundColor: 'rgba(255, 0, 153, 0.2)',
                    borderColor: '#FF0099',
                    pointBackgroundColor: '#FF0099'
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    ...commonOptions.plugins,
                    title: {
                        display: true,
                        text: 'Insights Generales',
                        padding: {
                            top: 0,
                            bottom: 10
                        }
                    }
                }
            }
        }
    );
    """

    return f"""
    <html>
        <head>
            <title>Tiffany Medical Assistant - Dashboard</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            
            <style>
                :root {{
                    --primary-color: #FF0099;
                    --primary-hover: #D6006F;
                    --background-dark: #000000;
                    --text-light: rgba(255, 255, 255, 0.8);
                    --text-lighter: rgba(255, 255, 255, 0.5);
                    --border-color: rgba(255, 0, 153, 0.2);
                }}
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                body {{
                    background: var(--background-dark);
                    color: var(--text-light);
                    min-height: 100vh;
                }}
                .dashboard-layout {{
                    display: grid;
                    grid-template-columns: 1fr;
                    height: 100vh;
                    max-width: 100vw;
                    margin: 0 auto;
                    padding: 0.5rem 1rem;
                    overflow-y: auto;
                    overflow-x: hidden;
                }}
                .main-content {{
                    height: calc(100vh - 1rem);
                    display: flex;
                    flex-direction: column;
                    gap: 0.4rem;
                }}
                .header {{
                    display: flex;
                    align-items: flex-start; /* Alinear al inicio */
                    align-items: flex-start;
                    padding: 1.5rem;
                    background: rgba(20, 20, 20, 0.8);
                    border-radius: 20px;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 1rem; /* Reducido de 2rem */
                    padding: 1rem; /* Reducido de 1.5rem */
                    background: rgba(40, 40, 40, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 15px;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    margin-bottom: 1.5rem;
                    backdrop-filter: blur(10px);
                }}
                .header h1 {{
                    font-size: 2.2rem;
                    font-weight: 600;
                    font-size: 1.5rem; /* Reducido de 2rem */
                    color: white;
                    font-family: 'Playfair Display', serif; /* Fuente más elegante */
                    font-family: 'Playfair Display', serif;
                    line-height: 1.2;
                    display: flex;
                    align-items: center;
                    gap: 0.8rem; /* Reducido de 1rem */
                }}
                .header-icon {{
                    color: var(--primary-color);
                }}
                .metrics-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 1rem;
                    margin-bottom: 2rem;
                    height: auto;
                    width: 100%;
                    padding: 0 1rem;
                }}
                /* Resoluciones más comunes y Safari fixes */
                
                /* 4K - 3840x2160 */
                @media screen and (min-width: 2560px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(4, 1fr);
                        max-width: 90vw;
                        margin: 0 auto;
                    }}
                    
                    .metric-card {{
                        min-height: 30vh;
                    }}
                }}
                /* Desktop grande - 1920x1080 */
                @media screen and (min-width: 1920px) and (max-width: 2559px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(4, 1fr);
                        gap: 1.5vw;
                    }}
                    
                    .metric-card {{
                        min-height: 35vh;
                    }}
                }}
                /* Desktop común - 1366x768 */
                @media screen and (min-width: 1366px) and (max-width: 1919px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(4, 1fr);
                        gap: 1vw;
                    }}
                    
                    .metric-card {{
                        min-height: 40vh;
                    }}
                }}
                /* MacBook Pro 13" - 1280x800 */
                @media screen and (min-width: 1280px) and (max-width: 1365px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(2, 1fr);
                        gap: 1.5vw;
                    }}
                    
                    .metric-card {{
                        min-height: 45vh;
                    }}
                }}
                /* Safari específico */
                @supports (-webkit-hyphens:none) {{
                    .metrics-grid {{
                        display: grid;
                        grid-template-columns: repeat(4, minmax(0, 1fr)); /* Fix para Safari */
                        gap: 1rem;
                        width: 100%;
                        height: auto;
                        padding: 0 1rem;
                    }}
                    .metric-card {{
                        min-width: 0; /* Fix para Safari */
                        height: auto;
                        min-height: 40vh;
                    }}
                    .chart-container {{
                        width: 100%;
                        min-height: 25vh;
                        transform: translateZ(0); /* Fix para renderizado en Safari */
                        -webkit-transform: translateZ(0);
                    }}
                }}
                /* Tablet landscape */
                @media screen and (min-width: 1024px) and (max-width: 1279px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(2, 1fr);
                        gap: 1.5vw;
                    }}
                    
                    .metric-card {{
                        min-height: 42vh;
                    }}
                }}
                /* Tablet portrait */
                @media screen and (min-width: 768px) and (max-width: 1023px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(2, 1fr);
                        gap: 2vw;
                    }}
                    
                    .metric-card {{
                        min-height: 45vh;
                    }}
                }}
                /* Mobile landscape */
                @media screen and (min-width: 480px) and (max-width: 767px) {{
                    .metrics-grid {{
                        grid-template-columns: 1fr;
                        gap: 2vh;
                    }}
                    
                    .metric-card {{
                        min-height: 48vh;
                    }}
                }}
                /* Mobile portrait */
                @media screen and (max-width: 479px) {{
                    .metrics-grid {{
                        grid-template-columns: 1fr;
                        gap: 2vh;
                        padding: 0 0.5rem;
                    }}
                    
                    .metric-card {{
                        min-height: 45vh;
                    }}
                }}
                /* Fix específico para Safari en diferentes resoluciones */
                @media not all and (min-resolution:.001dpcm) {{ 
                    @supports (-webkit-appearance:none) {{
                        .metrics-grid {{
                            display: grid;
                            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                            gap: 1rem;
                            width: 100%;
                            height: auto;
                        }}
                        
                        .metric-card {{
                            break-inside: avoid;
                            page-break-inside: avoid;
                            -webkit-column-break-inside: avoid;
                        }}
                    }}
                }}
                /* Asegurar compatibilidad con diferentes alturas de viewport */
                @media screen and (max-height: 800px) {{
                    .metric-card {{
                        min-height: 45vh;
                    }}
                }}
                @media screen and (max-height: 600px) {{
                    .metric-card {{
                        min-height: 50vh;
                    }}
                }}
                .metric-card {{
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 15px;
                    padding: 1.5rem 1rem;
                    border: 1px solid var(--border-color);
                    height: auto;
                    min-height: 35vh;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: flex-start; /* Cambiado a flex-start para mejor control del espacio */
                    overflow: hidden;
                }}
                .chart-title {{
                    font-size: 1.2rem;
                    margin: 0 0 1rem 0; /* Margen uniforme */
                    text-align: center;
                    width: 100%;
                    padding: 0.5rem;
                    white-space: normal; /* Permitir múltiples líneas */
                    overflow-wrap: break-word; /* Romper palabras largas si es necesario */
                    word-wrap: break-word;
                    min-height: 2.5em; /* Altura mínima para dos líneas */
                    display: -webkit-box;
                    -webkit-line-clamp: 2; /* Máximo dos líneas */
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                    line-height: 1.2;
                }}
                .chart-container {{
                    flex: 1;
                    position: relative;
                    width: 95%;
                    min-height: 28vh;
                    padding: 0.5rem;
                    margin: 0 auto;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }}
                canvas {{
                    width: 100% !important;
                    height: 100% !important;
                    max-height: calc(100% - 2rem) !important; /* Prevenir desbordamiento */
                }}
                .kpi-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr); /* Cambio de 1fr a repeat(4, 1fr) */
                    gap: 1rem;
                    margin-bottom: 1.5rem;
                }}
                .kpi-card {{
                    background: rgba(20, 20, 20, 0.8);
                    padding: 1.5rem;
                    border-radius: 20px;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .kpi-value {{
                    font-size: 3rem;
                    font-size: 1.8rem; /* Reducido de 2rem */
                    font-weight: 600;
                    color: #FF0099;
                    margin-bottom: 0.5rem;
                    margin-bottom: 0.3rem; /* Reducido de 0.5rem */
                }}
                .kpi-label {{
                    font-size: 1.2rem;
                    font-size: 0.9rem; /* Reducido de 1.1rem */
                    color: rgba(255, 255, 255, 0.8);
                    font-weight: 400;
                }}
                .billing-grid {{
                    display: grid;
                    grid-template-columns: 2fr 1fr;
                    gap: 2rem;
                    margin-bottom: 2rem;
                }}
                .billing-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 15px;
                    padding: 1.5rem;
                    border: 1px solid var(--border-color);
                    backdrop-filter: blur(10px);
                }}
                .billing-summary {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 1rem;
                    margin-bottom: 2rem;
                }}
                .summary-item {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 0, 153, 0.1);
                    padding: 1.5rem;
                    border-radius: 12px;
                    text-align: center;
                    border: 1px solid var(--border-color);
                    border: 1px solid var(--primary-color);
                    transition: all 0.3s ease;
                }}
                .summary-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    transform: translateY(-5px);
                    box-shadow: 0 5px 15px rgba(255, 0, 153, 0.2);
                }}
                .summary-value {{
                    font-size: 2rem;
                    font-weight: 600;
                    color: var(--primary-color);
                    margin-bottom: 0.5rem;
                }}
                .summary-label {{
                    font-size: 0.9rem;
                    color: var(--text-light);
                }}
                .calendar-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .month-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    padding: 1rem;
                    border-radius: 10px;
                    text-align: center;
                    transition: all 0.3s ease;
                }}
                .month-card:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: scale(1.05);
                }}
                .month-name {{
                    font-size: 1.1rem;
                    margin-bottom: 0.5rem;
                    color: white;
                }}
                .month-amount {{
                    font-size: 1.2rem;
                    color: var(--primary-color);
                    font-weight: 600;
                }}
                .month-status {{
                    font-size: 0.8rem;
                    margin-top: 0.5rem;
                    padding: 0.3rem 0.8rem;
                    border-radius: 12px;
                    display: inline-block;
                }}
                .status-paid {{
                    background: rgba(0, 179, 104, 0.2);
                    color: #00b368;
                }}
                .status-pending {{
                    background: rgba(255, 170, 0, 0.2);
                    color: #ffaa00;
                }}
                .chart-container {{
                    height: 300px;
                    margin-top: 2rem;
                    height: 250px; /* Reducido de 300px */
                    margin: 1rem 0; /* Reducido de 2rem */
                    padding: 0.8rem; /* Reducido de 1rem */
                }}
                .payment-methods {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .payment-method {{
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    padding: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 10px;
                    transition: all 0.3s ease;
                }}
                .payment-method:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateX(5px);
                }}
                .method-icon {{
                    width: 40px;
                    height: 40px;
                    background: var(--primary-color);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .section-title {{
                    font-size: 1.3rem;
                    color: white;
                    margin-bottom: 1rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .section-title i {{
                    color: var(--primary-color);
                }}
                @media (max-width: 1200px) {{
                    .billing-grid {{
                        grid-template-columns: 1fr;
                    }}
                    .calendar-grid {{
                        grid-template-columns: repeat(3, 1fr);
                    }}
                }}
                @media (max-width: 768px) {{
                    .calendar-grid {{
                        grid-template-columns: repeat(2, 1fr);
                    }}
                    .billing-summary {{
                        grid-template-columns: 1fr;
                    }}
                }}
                .payment-method {{
                    position: relative;
                    overflow: hidden;
                }}
                .method-details {{
                    flex: 1;
                }}
                .method-status {{
                    font-size: 0.8rem;
                    padding: 0.2rem 0.5rem;
                    background: rgba(255, 0, 153, 0.1);
                    border-radius: 12px;
                    color: var(--primary-color);
                }}
                .action-btn {{
                    background: transparent;
                    border: none;
                    color: var(--text-light);
                    cursor: pointer;
                    padding: 0.5rem;
                    border-radius: 50%;
                    transition: all 0.3s ease;
                }}
                .action-btn:hover {{
                    background: rgba(255, 255, 255, 0.1);
                    color: var(--primary-color);
                }}
                .payment-history {{
                    margin-top: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    overflow: hidden;
                }}
                .history-header {{
                    display: grid;
                    grid-template-columns: 2fr 1fr 1fr 1fr;
                    padding: 1rem;
                    background: rgba(255, 0, 153, 0.1);
                    font-weight: 500;
                }}
                .history-item {{
                    display: grid;
                    grid-template-columns: 2fr 1fr 1fr 1fr;
                    padding: 1rem;
                    align-items: center;
                    transition: all 0.3s ease;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                }}
                .history-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.05);
                }}
                .history-item.pending {{
                    background: rgba(255, 170, 0, 0.15);
                    background: rgba(255, 170, 0, 0.05);
                }}
                .status-badge {{
                    padding: 0.3rem 0.8rem;
                    border-radius: 12px;
                    font-size: 0.85rem;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .status-badge.paid {{
                    background: rgba(0, 179, 104, 0.2);
                    color: #00b368;
                }}
                .status-badge.pending {{
                    background: rgba(255, 170, 0, 0.2);
                    color: #ffaa00;
                }}
                .payment-stats {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .stat-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    padding: 1rem;
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    transition: all 0.3s ease;
                }}
                .stat-card:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateY(-2px);
                }}
                .stat-icon {{
                    width: 40px;
                    height: 40px;
                    background: var(--primary-color);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .stat-info h4 {{
                    font-size: 0.9rem;
                    margin-bottom: 0.2rem;
                }}
                .stat-info p {{
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: var(--primary-color);
                }}
                .mt-4 {{
                    margin-top: 2rem;
                }}
                .text-success {{
                    color: #00b368;
                }}
                .text-warning {{
                    color: #ffaa00;
                }}
                .chart-container {{
                    height: 300px;
                    margin: 2rem 0;
                    padding: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.02);
                    border-radius: 15px;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    height: 250px; /* Reducido de 300px */
                    margin: 1rem 0; /* Reducido de 2rem */
                    padding: 0.8rem; /* Reducido de 1rem */
                }}
                @media (max-width: 768px) {{
                    .payment-stats {{
                        grid-template-columns: 1fr;
                    }}
                    .history-item {{
                        font-size: 0.9rem;
                    }}
                }}
            </style>
            <!-- Agregar en el <style> de cada página -->
            <style>
                html {{
                    scroll-behavior: smooth;
                    scroll-padding-bottom: 100px; /* Para que el scroll no oculte contenido detrás del sidebar */
                }}
            </style>
        </head>
        <body>
            {get_common_sidebar()}
            <div class="dashboard-layout">
                <div class="main-content">
                    <div class="header">
                        <h1>
                            <i class="fas fa-chart-line header-icon"></i>
                            Dashboard Tiffany Medical Assistant
                        </h1>
                    </div>
                    
                    <div class="kpi-grid">
                        <div class="kpi-card">
                            <div class="kpi-value">30%</div>
                            <div class="kpi-label">Incremento en Follow-ups</div>
                        </div>
                        <div class="kpi-card">
                            <div class="kpi-value">25%</div>
                            <div class="kpi-label">Reducción Tareas Admin</div>
                        </div>
                        <div class="kpi-card">
                            <div class="kpi-value">5min</div>
                            <div class="kpi-label">Tiempo Onboarding</div>
                        </div>
                        <div class="kpi-card">
                            <div class="kpi-value">80%</div>
                            <div class="kpi-label">Resolución WhatsApp</div>
                        </div>
                    </div>
                    <div class="metrics-grid">
                        <div class="metric-card">
                            <div class="chart-title">Engagement de Usuarios Activos</div>
                            <div class="chart-container">
                                <canvas id="userEngagementChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Rendimiento de Automatización</div>
                            <div class="chart-container">
                                <canvas id="automationChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Tiempos de Respuesta en Urgencias</div>
                            <div class="chart-container">
                                <canvas id="patientCareChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Reducción de Tareas Administrativas</div>
                            <div class="chart-container">
                                <canvas id="efficiencyChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Estado de Capacitación del Personal</div>
                            <div class="chart-container">
                                <canvas id="trainingChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Rendimiento del Sistema</div>
                            <div class="chart-container">
                                <canvas id="systemPerformanceChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Adopción de Nuevas Funcionalidades</div>
                            <div class="chart-container">
                                <canvas id="adoptionChart"></canvas>
                            </div>
                        </div>
                        <div class="metric-card">
                            <div class="chart-title">Insights Generales</div>
                            <div class="chart-container">
                                <canvas id="insightsChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                {charts_js}
            </script>
        </body>
    </html>
    """

@rt('/profile')
def profile_page():
    return f"""
    <html>
        <head>
            <title>Tiffany Medical Assistant - Perfil</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            
            <style>
                :root {{
                    --primary-color: #FF0099;
                    --primary-hover: #D6006F;
                    --background-dark: #000000;
                    --text-light: rgba(255, 255, 255, 0.8);
                    --text-lighter: rgba(255, 255, 255, 0.5);
                    --border-color: rgba(255, 0, 153, 0.2);
                }}
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Poppins', sans-serif;
                }}
                body {{
                    min-height: 100vh;
                    background: var(--background-dark);
                    color: var(--text-light);
                    min-height: 100vh;
                }}
                .dashboard-layout {{
                    display: grid;
                    grid-template-columns: 1fr;
                    padding: 0 3rem 150px 3rem;
                    min-height: 100vh;
                }}
                .main-content {{
                    width: min(1400px, 100% - 2rem);
                    margin-inline: auto;
                    padding: 2rem 0;
                    overflow: visible;
                }}
                .profile-header {{
                    display: flex;
                    align-items: center;
                    gap: 2rem;
                    padding: 2rem;
                    background: rgba(40, 40, 40, 0.95);
                    background: rgba(255, 0, 153, 0.1);
                    border-radius: 20px;
                    margin-bottom: 2rem;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    border: 1px solid var(--primary-color);
                }}
                .profile-avatar {{
                    width: 120px;
                    height: 120px;
                    border-radius: 50%;
                    background: var(--primary-color);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 3rem;
                    color: white;
                    border: 4px solid rgba(255, 255, 255, 0.1);
                }}
                .profile-info {{
                    flex: 1;
                }}
                .profile-name {{
                    font-size: 2rem;
                    color: white;
                    margin-bottom: 0.5rem;
                }}
                .profile-role {{
                    font-size: 1.1rem;
                    color: var(--primary-color);
                    margin-bottom: 1rem;
                }}
                .profile-stats {{
                    display: flex;
                    gap: 2rem;
                }}
                .stat-item {{
                    text-align: center;
                }}
                .stat-value {{
                    font-size: 1.5rem;
                    font-weight: 600;
                    color: white;
                }}
                .stat-label {{
                    font-size: 0.9rem;
                    color: var(--text-light);
                }}
                .profile-grid {{
                    display: grid;
                    grid-template-columns: 2fr 1fr;
                    gap: 2rem;
                }}
                .profile-section {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 20px;
                    padding: 2rem;
                    border: 1px solid var(--border-color);
                }}
                .section-title {{
                    font-size: 1.3rem;
                    color: white;
                    margin-bottom: 1.5rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .section-title i {{
                    color: var(--primary-color);
                }}
                .info-grid {{
                    display: grid;
                    gap: 1.5rem;
                }}
                .info-item {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    padding: 1.2rem;
                    border-radius: 12px;
                    transition: all 0.3s ease;
                }}
                .info-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateX(5px);
                }}
                .info-label {{
                    font-size: 0.9rem;
                    color: var(--text-light);
                    margin-bottom: 0.5rem;
                }}
                .info-value {{
                    font-size: 1.1rem;
                    color: white;
                }}
                .activity-list {{
                    display: flex;
                    flex-direction: column;
                    gap: 1rem;
                }}
                .activity-item {{
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    padding: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    transition: all 0.3s ease;
                }}
                .activity-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateX(5px);
                }}
                .activity-icon {{
                    width: 40px;
                    height: 40px;
                    background: var(--primary-color);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .activity-details {{
                    flex: 1;
                }}
                .activity-title {{
                    font-size: 1rem;
                    color: white;
                    margin-bottom: 0.2rem;
                }}
                .activity-time {{
                    font-size: 0.85rem;
                    color: var(--text-light);
                }}
                .subscription-info {{
                    padding: 1.5rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 0, 153, 0.1);
                    border-radius: 15px;
                    margin-top: 2rem;
                }}
                .subscription-status {{
                    display: inline-block;
                    padding: 0.5rem 1rem;
                    background: rgba(0, 179, 104, 0.2);
                    color: #00b368;
                    border-radius: 20px;
                    font-size: 0.9rem;
                    margin-bottom: 1rem;
                }}
                .action-buttons {{
                    display: flex;
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .action-btn {{
                    padding: 0.8rem;
                    border: none;
                    border-radius: 10px;
                    font-size: 1rem;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 40px;
                    height: 40px;
                }}
                .btn-primary {{
                    background: var(--primary-color);
                    color: white;
                }}
                .btn-primary:hover {{
                    background: var(--primary-hover);
                    transform: translateY(-2px);
                }}
                .btn-secondary {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.1);
                    color: white;
                }}
                .btn-secondary:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 255, 255, 0.2);
                    transform: translateY(-2px);
                }}
                @media (max-width: 1200px) {{
                    .profile-grid {{
                        grid-template-columns: 1fr;
                    }}
                }}
                @media (max-width: 768px) {{
                    .profile-header {{
                        flex-direction: column;
                        text-align: center;
                        padding: 1rem;
                        margin-bottom: 1rem;
                    }}
                    .profile-stats {{
                        justify-content: center;
                        flex-wrap: wrap;
                        gap: 1rem;
                    }}
                    .profile-grid {{
                        grid-template-columns: 1fr;
                        gap: 1rem;
                    }}
                    .profile-section {{
                        padding: 1rem;
                    }}
                    .section-title {{
                        font-size: 1.1rem;
                        margin-bottom: 1rem;
                    }}
                    .info-grid {{
                        gap: 1rem;
                    }}
                    .info-item {{
                        padding: 1rem;
                    }}
                    .activity-item {{
                        padding: 0.8rem;
                    }}
                }}
                @media (min-width: 769px) and (max-width: 1024px) {{
                    .dashboard-layout {{
                        padding: 0 1.5rem 100px 1.5rem;
                    }}
                    
                    .profile-grid {{
                        grid-template-columns: 1fr;
                        gap: 1.5rem;
                    }}
                }}
                /* Ajustes específicos para tablets */
                @media (max-width: 1200px) {{
                    .chart-container {{
                        height: 350px;
                    }}
                }}
                /* Ajustes para móvil */
                @media (max-width: 768px) {{
                    .chart-container {{
                        height: 400px;
                        padding: 1rem;
                        margin: 1rem auto;
                        width: 95%;
                    }}
                }}
                /* Asegurar que el contenido principal tenga espacio para el sidebar inferior */
                .main-content {{
                    width: 100%;
                    max-width: 100vw;
                    margin: 0 auto;
                    padding: 2rem 0;
                }}
                /* Ajustes para el scroll */
                html, body {{
                    overflow-x: hidden;
                    scroll-behavior: smooth;
                    scroll-padding-bottom: 100px;
                }}
            </style>
        </head>
        <body>
            {get_common_sidebar()}
            <div class="dashboard-layout">
                <div class="main-content">
                    <div class="profile-header">
                        <div class="profile-avatar">
                            <i class="fas fa-user"></i>
                        </div>
                        <div class="profile-info">
                            <h1 class="profile-name" id="userName">Cargando...</h1>
                            <div class="profile-role" id="userRole">Cargando...</div>
                            <div class="profile-stats">
                                <div class="stat-item">
                                    <div class="stat-value">28</div>
                                    <div class="stat-label">Consultas</div>
                                </div>
                                <div class="stat-item">
                                    <div class="stat-value">15</div>
                                    <div class="stat-label">Reportes</div>
                                </div>
                                <div class="stat-item">
                                    <div class="stat-value">95%</div>
                                    <div class="stat-label">Satisfacción</div>
                                </div>
                            </div>
                        </div>
                        <div class="action-buttons">
                            <button class="action-btn btn-primary">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="action-btn btn-secondary">
                                <i class="fas fa-cog"></i>
                            </button>
                        </div>
                    </div>
                    <div class="profile-grid">
                        <div class="profile-section">
                            <div class="section-title">
                                <i class="fas fa-user-circle"></i>
                                Información Personal
                            </div>
                            <div class="info-grid" id="userInfo">
                                <!-- Se llenará con JavaScript -->
                            </div>
                            <div class="section-title mt-4">
                                <i class="fas fa-clock"></i>
                                Actividad Reciente
                            </div>
                            <div class="activity-list">
                                <div class="activity-item">
                                    <div class="activity-icon">
                                        <i class="fas fa-file-medical"></i>
                                    </div>
                                    <div class="activity-details">
                                        <div class="activity-title">Reporte Generado</div>
                                        <div class="activity-time">Hace 2 horas</div>
                                    </div>
                                </div>
                                <div class="activity-item">
                                    <div class="activity-icon">
                                        <i class="fas fa-user-md"></i>
                                    </div>
                                    <div class="activity-details">
                                        <div class="activity-title">Consulta Completada</div>
                                        <div class="activity-time">Hace 5 horas</div>
                                    </div>
                                </div>
                                <div class="activity-item">
                                    <div class="activity-icon">
                                        <i class="fas fa-chart-line"></i>
                                    </div>
                                    <div class="activity-details">
                                        <div class="activity-title">Análisis de Datos</div>
                                        <div class="activity-time">Ayer</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="profile-section">
                            <div class="section-title">
                                <i class="fas fa-shield-alt"></i>
                                Estado de la Cuenta
                            </div>
                            <div class="subscription-info">
                                <span class="subscription-status">
                                    <i class="fas fa-check-circle"></i>
                                    Activa
                                </span>
                                <h3>Plan Premium</h3>
                                <p>Próxima facturación: 15/04/2024</p>
                            </div>
                            <div class="section-title mt-4">
                                <i class="fas fa-bell"></i>
                                Notificaciones
                            </div>
                            <div class="info-grid">
                                <div class="info-item">
                                    <div class="info-label">Email</div>
                                    <div class="info-value">Activadas</div>
                                </div>
                                <div class="info-item">
                                    <div class="info-label">SMS</div>
                                    <div class="info-value">Activadas</div>
                                </div>
                                <div class="info-item">
                                    <div class="info-label">WhatsApp</div>
                                    <div class="info-value">Activado</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                window.onload = function() {{
                    const clientData = localStorage.getItem('clientData');
                    if (!clientData) {{
                        window.location.href = '/';
                        return;
                    }}
                    
                    const userData = JSON.parse(clientData);
                    console.log('userData:', userData); // Para debug
                    
                    // Actualizar nombre y rol
                    document.getElementById('userName').textContent = userData.fullName || 'Usuario';
                    document.getElementById('userRole').textContent = userData.roles?.[0] || 'Usuario';
                    
                    // Actualizar información personal
                    const userInfo = document.getElementById('userInfo');
                    userInfo.innerHTML = `
                        <div class="info-item">
                            <div class="info-label">Email</div>
                            <div class="info-value">${{userData.email || 'No especificado'}}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">Empresa</div>
                            <div class="info-value">${{userData.company?.name || 'No especificado'}}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">Teléfono</div>
                            <div class="info-value">${{userData.phone || 'No especificado'}}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">Ubicación</div>
                            <div class="info-value">${{userData.address?.street || 'No especificado'}} ${{userData.address?.city ? ',' + userData.address?.city : ''}} ${{userData.address?.state || ''}} ${{userData.address?.country || ''}}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">Departamento</div>
                            <div class="info-value">${{userData.company?.department || 'No especificado'}}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">Cargo</div>
                            <div class="info-value">${{userData.company?.position || 'No especificado'}}</div>
                        </div>
                    `;
                }};
            </script>
        </body>
    </html>
    """

@rt('/reset-password')
def reset_password_page():
    return """
    <html>
        <head>
            <title>POCKET UX - Recuperar Contraseña</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
            <!-- External Resources -->
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            
            <style>
                :root {
                    --primary-color: #FF0099;
                    --primary-hover: #D6006F;
                    --background-dark: #000000;
                    --text-light: rgba(255, 255, 255, 0.8);
                    --text-lighter: rgba(255, 255, 255, 0.5);
                    --border-color: rgba(255, 0, 153, 0.2);
                }
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Poppins', sans-serif;
                }
                body {
                    min-height: 100vh;
                    background: var(--background-dark);
                }
                .container {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    min-height: 100vh;
                }
                .logo-section {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: rgba(0, 0, 0, 0.5);
                }
                .logo {
                    width: 400px;
                    height: auto;
                    filter: brightness(1.2) drop-shadow(0 0 30px rgba(255, 0, 153, 0.7));
                    animation: logoFloat 6s ease-in-out infinite,
                             logoGlow 3s ease-in-out infinite,
                             logoRotate 12s linear infinite;
                             logoGlow 3s ease-in-out infinite;
                    transform-origin: center center;
                }
                .form-section {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 2rem;
                    background: rgba(255, 255, 255, 0.05);
                }
                .form-container {
                    background: rgba(40, 40, 40, 0.95);
                    padding: 2.5rem;
                    border-radius: 20px;
                    width: 100%;
                    max-width: 400px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    backdrop-filter: blur(10px);
                    margin: 0 auto; /* Centrar el contenedor */
                }
                h1 {
                    color: white;
                    font-size: 2rem;
                    text-align: center;
                    margin-bottom: 0.5rem;
                }
                .subtitle {
                    color: var(--text-lighter);
                    text-align: center;
                    font-size: 0.9rem;
                    margin-bottom: 2rem;
                }
                .phone-input {
                    display: flex;
                    align-items: stretch;
                    gap: 8px;
                    margin-bottom: 1rem;
                    background: rgba(255, 255, 255, 0.05);
                    padding: 0.8rem;
                    border-radius: 12px;
                    border: 1px solid var(--border-color);
                    width: 100%; /* Asegurar que el contenedor ocupe todo el ancho disponible */
                }
                .country-code {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 0.5rem 0.8rem;
                    border-radius: 8px;
                    border: 1px solid var(--border-color);
                    height: 42px;
                    min-width: 90px; /* Ancho mínimo para el código de país */
                    flex-shrink: 0; /* Evitar que se encoja */
                }
                .country-code input {
                    width: 50px;
                    background: transparent;
                    border: none;
                    color: white;
                    font-size: 0.9rem;
                    text-align: center;
                    padding: 0;
                }
                .country-flag {
                    width: 24px;
                    height: 16px;
                    border-radius: 4px;
                    transition: all 0.3s ease;
                }
                .phone-number {
                    flex: 1;
                    background: rgba(255, 255, 255, 0.1);
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    padding: 0 1rem;
                    color: white;
                    font-size: 0.95rem;
                    height: 42px;
                    width: 100%; /* Asegurar que ocupe el espacio restante */
                    min-width: 0; /* Permitir que se encoja si es necesario */
                }
                .submit-button {
                    width: 100%;
                    padding: 1rem;
                    background: var(--primary-color);
                    border: none;
                    border-radius: 10px;
                    color: white;
                    font-size: 1rem;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
                .submit-button:hover {
                    background: var(--primary-hover);
                    transform: translateY(-2px);
                }
                .back-link {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                    margin-top: 1.5rem;
                    color: var(--text-lighter);
                    text-decoration: none;
                    font-size: 0.9rem;
                    transition: all 0.3s ease;
                    padding: 8px 16px;
                    border-radius: 20px;
                    background: rgba(255, 0, 153, 0.1);
                    border: 1px solid var(--border-color);
                }
                .back-link:hover {
                    color: var(--primary-color);
                    background: rgba(255, 0, 153, 0.15);
                    border-color: var(--primary-color);
                    transform: translateY(-2px);
                }
                #message {
                    margin-top: 1rem;
                    text-align: center;
                    padding: 0.8rem;
                    border-radius: 12px;
                    border-radius: 8px;
                    font-size: 0.9rem;
                    transition: all 0.3s ease;
                }
                .success {
                    background: rgba(0, 179, 104, 0.2);
                    border: 1px solid #00b368;
                    color: #00b368;
                    animation: successAnimation 0.3s ease-out forwards;
                }
                .error {
                    background: rgba(255, 0, 0, 0.2);
                    border: 1px solid #ff0000;
                    color: #ff0000;
                    animation: errorAnimation 0.3s ease-out forwards;
                    background: rgba(255, 68, 68, 0.2);
                    color: #ff4444;
                }
                @keyframes logoRotate {
                    0% { transform: rotateY(0deg); }
                    100% { transform: rotateY(360deg); }
                }
                @keyframes logoFloat {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-20px); }
                }
                @keyframes logoGlow {
                    0%, 100% { filter: brightness(1) drop-shadow(0 0 20px rgba(255, 0, 153, 0.5)); }
                    50% { filter: brightness(1.2) drop-shadow(0 0 30px rgba(255, 0, 153, 0.7)); }
                }
                @media (max-width: 768px) {
                    .container {
                        grid-template-columns: 1fr;
                    }
                    .logo-section {
                        display: none;
                    }
                    .form-section {
                        padding: 1.5rem;
                    }
                    .form-container {
                        padding: 2rem;
                    }
                }
                /* Validación del número */
                .phone-validation {
                    font-size: 0.85rem;
                    margin-top: 0.5rem;
                    padding: 0.5rem;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    transition: all 0.3s ease;
                }
                .phone-validation.valid {
                    color: #00b368;
                    background: rgba(0, 179, 104, 0.1);
                }
                .phone-validation.invalid {
                    color: #ff4444;
                    background: rgba(255, 68, 68, 0.1);
                }
                /* Ajustes de espaciado */
                .form-container {
                    padding: 2rem;
                    max-width: 380px;
                }
                .phone-input {
                    margin-bottom: 1rem;
                }
                .subtitle {
                    margin-bottom: 1.5rem;
                    line-height: 1.4;
                }
                /* Mejoras visuales */
                .phone-number:focus, .country-code input:focus {
                    outline: none;
                    border-color: var(--primary-color);
                    box-shadow: 0 0 0 2px rgba(255, 0, 153, 0.2);
                }
                .submit-button:disabled {
                    opacity: 0.7;
                    cursor: not-allowed;
                }
                /* Animación para el mensaje de éxito */
                @keyframes successAnimation {
                    0% { 
                        transform: scale(0.9);
                        opacity: 0;
                    }
                    50% { 
                        transform: scale(1.1);
                    }
                    100% { 
                        transform: scale(1);
                        opacity: 1;
                    }
                }
                .success {
                    animation: successAnimation 0.3s ease-out forwards;
                }
                /* Animaciones */
                @keyframes errorAnimation {
                    0% { 
                        transform: translateX(-10px);
                        opacity: 0;
                    }
                    50% { 
                        transform: translateX(10px);
                    }
                    100% { 
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                /* Estilos para inputs no válidos */
                input:invalid {
                    border-color: #ff0000;
                    animation: shake 0.3s ease-in-out;
                }
                @keyframes shake {
                    0%, 100% { transform: translateX(0); }
                    25% { transform: translateX(-5px); }
                    75% { transform: translateX(5px); }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo-section">
                    <img src="/static/images/logopocket.png" alt="POCKET UX" class="logo">
                </div>
                
                <div class="form-section">
                    <div class="form-container">
                        <h1>Restablecer Contraseña</h1>
                        <p class="subtitle">
                            Ingresa tu número de teléfono y te enviaremos un código de verificación 
                            para restablecer tu contraseña.
                        </p>
                        
                        <form id="resetForm">
                            <div class="phone-input">
                                <div class="country-code">
                                    <input type="text" id="dialCode" value="+57" maxlength="4">
                                    <img src="https://flagcdn.com/w160/co.png" 
                                         alt="Country flag" 
                                         class="country-flag" 
                                         id="countryFlag">
                                </div>
                                <input type="tel" 
                                       class="phone-number" 
                                       id="phone" 
                                       placeholder="Teléfono Ej. 300..."
                                       required>
                            </div>
                            
                            <div class="phone-validation">
                                <i class="fas fa-circle-info"></i>
                                Ingresa un número válido
                            </div>
                            
                            <button type="submit" class="submit-button" id="submitButton" disabled>
                                Enviar código
                            </button>
                        </form>
                        
                        <div id="message"></div>
                        
                        <a href="/" class="back-link">
                            <i class="fas fa-arrow-left"></i>
                            Volver al inicio de sesión
                        </a>
                    </div>
                </div>
            </div>
            <script>
                // Country Codes Configuration
                const countryCodeMap = {
                    '+57': 'co', '+52': 'mx', '+34': 'es', '+54': 'ar',
                    '+51': 'pe', '+56': 'cl', '+55': 'br', '+58': 've',
                    '+593': 'ec', '+502': 'gt', '+503': 'sv', '+504': 'hn',
                    '+505': 'ni', '+506': 'cr', '+507': 'pa', '+591': 'bo',
                    '+595': 'py', '+598': 'uy', '+1': 'us'
                };
                // Initialize elements
                const dialCodeInput = document.getElementById('dialCode');
                const countryFlag = document.getElementById('countryFlag');
                const phoneInput = document.getElementById('phone');
                // Validación del número de teléfono
                function validatePhoneNumber(number) {
                    // Eliminar espacios y caracteres especiales
                    number = number.replace(/[^0-9]/g, '');
                    return number.length >= 10 && number.length <= 12;
                }
                function updateValidationUI(isValid, message) {
                    const validation = document.querySelector('.phone-validation');
                    const submitButton = document.getElementById('submitButton');
                    
                    if (isValid) {
                        validation.className = 'phone-validation valid';
                        validation.innerHTML = '<i class="fas fa-check-circle"></i>' + message;
                        submitButton.disabled = false;
                    } else {
                        validation.className = 'phone-validation invalid';
                        validation.innerHTML = '<i class="fas fa-exclamation-circle"></i>' + message;
                        submitButton.disabled = true;
                    }
                }
                // Event listeners para validación en tiempo real
                phoneInput.addEventListener('input', function() {
                    const number = this.value;
                    const dialCode = dialCodeInput.value;
                    const isValidCode = countryCodeMap[dialCode];
                    
                    if (!isValidCode) {
                        updateValidationUI(false, 'Código de país no válido');
                        return;
                    }
                    if (validatePhoneNumber(number)) {
                        updateValidationUI(true, 'Número válido');
                    } else {
                        updateValidationUI(false, 'El número debe tener entre 10 y 12 dígitos');
                    }
                });
                dialCodeInput.addEventListener('input', function(e) {
                    let value = e.target.value;
                    if (!value.startsWith('+')) {
                        value = '+' + value;
                    }
                    e.target.value = value;
                    
                    const countryCode = countryCodeMap[value];
                    if (countryCode) {
                        countryFlag.src = `https://flagcdn.com/w160/${countryCode}.png`;
                        if (phoneInput.value) {
                            validatePhoneNumber(phoneInput.value);
                        }
                    } else {
                        updateValidationUI(false, 'Código de país no válido');
                    }
                });
                // Handle form submission
                document.getElementById('resetForm').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const fullNumber = dialCodeInput.value + phoneInput.value;
                    const submitButton = document.getElementById('submitButton');
                    const messageDiv = document.getElementById('message');
                    
                    submitButton.disabled = true;
                    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Enviando...';
                    try {
                        const response = await fetch('https://tifanny-back.vercel.app/v1/tifanny/resetPassword', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ phone: fullNumber })
                        });
                        if (response.ok) {
                            messageDiv.className = 'success';
                            messageDiv.innerHTML = `
                                <i class="fas fa-check-circle"></i>
                                Código enviado correctamente
                            `;
                            localStorage.setItem('resetPhoneNumber', fullNumber);
                            setTimeout(() => {
                                window.location.href = '/verify-code';
                            }, 2000);
                        } else {
                            messageDiv.className = 'error';
                            messageDiv.innerHTML = `
                                <i class="fas fa-exclamation-circle"></i>
                                Error al enviar el código
                            `;
                        }
                    } catch (error) {
                        messageDiv.className = 'error';
                        messageDiv.innerHTML = `
                            <i class="fas fa-times-circle"></i>
                            Error de conexión
                        `;
                    } finally {
                        submitButton.disabled = false;
                        submitButton.innerHTML = 'Enviar código';
                    }
                });
            </script>
        </body>
    </html>
    """

@rt('/billing')
def billing_page():
    return f"""
    <html>
        <head>
            <title>Tiffany Medical Assistant - Facturación</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            
            <style>
                :root {{
                    --primary-color: #FF0099;
                    --primary-hover: #D6006F;
                    --background-dark: #000000;
                    --text-light: rgba(255, 255, 255, 0.8);
                    --text-lighter: rgba(255, 255, 255, 0.5);
                    --border-color: rgba(255, 0, 153, 0.2);
                }}
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Poppins', sans-serif;
                }}
                body {{
                    background: var(--background-dark);
                    color: var(--text-light);
                    min-height: 100vh;
                }}
                .dashboard-layout {{
                    display: grid;
                    grid-template-columns: 1fr;
                    padding-left: 100px;
                    min-height: 100vh;
                }}
                .main-content {{
                    padding: 2rem 2rem 120px 2rem; /* Aumentar padding inferior */
                }}
                .header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 2rem;
                    padding: 1.5rem;
                    margin-bottom: 1rem; /* Reducido de 2rem */
                    padding: 1rem; /* Reducido de 1.5rem */
                    background: rgba(40, 40, 40, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 15px;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    backdrop-filter: blur(10px);
                }}
                .header h1 {{
                    font-size: 2rem;
                    font-size: 1.5rem; /* Reducido de 2rem */
                    color: white;
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    gap: 0.8rem; /* Reducido de 1rem */
                }}
                .header-icon {{
                    color: var(--primary-color);
                }}
                .billing-grid {{
                    display: grid;
                    grid-template-columns: 2fr 1fr;
                    gap: 2rem;
                    margin-bottom: 2rem;
                }}
                .billing-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 15px;
                    padding: 1.5rem;
                    border: 1px solid var(--border-color);
                    backdrop-filter: blur(10px);
                }}
                .billing-summary {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 1rem;
                    margin-bottom: 2rem;
                }}
                .summary-item {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 0, 153, 0.1);
                    padding: 1.5rem;
                    border-radius: 12px;
                    text-align: center;
                    border: 1px solid var(--border-color);
                    border: 1px solid var(--primary-color);
                    transition: all 0.3s ease;
                }}
                .summary-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    transform: translateY(-5px);
                    box-shadow: 0 5px 15px rgba(255, 0, 153, 0.2);
                }}
                .summary-value {{
                    font-size: 2rem;
                    font-weight: 600;
                    color: var(--primary-color);
                    margin-bottom: 0.5rem;
                }}
                .summary-label {{
                    font-size: 0.9rem;
                    color: var(--text-light);
                }}
                .calendar-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .month-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    padding: 1rem;
                    border-radius: 10px;
                    text-align: center;
                    transition: all 0.3s ease;
                }}
                .month-card:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: scale(1.05);
                }}
                .month-name {{
                    font-size: 1.1rem;
                    margin-bottom: 0.5rem;
                    color: white;
                }}
                .month-amount {{
                    font-size: 1.2rem;
                    color: var(--primary-color);
                    font-weight: 600;
                }}
                .month-status {{
                    font-size: 0.8rem;
                    margin-top: 0.5rem;
                    padding: 0.3rem 0.8rem;
                    border-radius: 12px;
                    display: inline-block;
                }}
                .status-paid {{
                    background: rgba(0, 179, 104, 0.2);
                    color: #00b368;
                }}
                .status-pending {{
                    background: rgba(255, 170, 0, 0.2);
                    color: #ffaa00;
                }}
                .chart-container {{
                    height: 300px;
                    margin-top: 2rem;
                    height: 250px; /* Reducido de 300px */
                    margin: 1rem 0; /* Reducido de 2rem */
                    padding: 0.8rem; /* Reducido de 1rem */
                }}
                .payment-methods {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .payment-method {{
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    padding: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 10px;
                    transition: all 0.3s ease;
                }}
                .payment-method:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateX(5px);
                }}
                .method-icon {{
                    width: 40px;
                    height: 40px;
                    background: var(--primary-color);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .section-title {{
                    font-size: 1.3rem;
                    color: white;
                    margin-bottom: 1rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .section-title i {{
                    color: var(--primary-color);
                }}
                @media (max-width: 1200px) {{
                    .billing-grid {{
                        grid-template-columns: 1fr;
                    }}
                    .calendar-grid {{
                        grid-template-columns: repeat(3, 1fr);
                    }}
                }}
                @media (max-width: 768px) {{
                    .calendar-grid {{
                        grid-template-columns: repeat(2, 1fr);
                    }}
                    .billing-summary {{
                        grid-template-columns: 1fr;
                    }}
                }}
                .payment-method {{
                    position: relative;
                    overflow: hidden;
                }}
                .method-details {{
                    flex: 1;
                }}
                .method-status {{
                    font-size: 0.8rem;
                    padding: 0.2rem 0.5rem;
                    background: rgba(255, 0, 153, 0.1);
                    border-radius: 12px;
                    color: var(--primary-color);
                }}
                .action-btn {{
                    background: transparent;
                    border: none;
                    color: var(--text-light);
                    cursor: pointer;
                    padding: 0.5rem;
                    border-radius: 50%;
                    transition: all 0.3s ease;
                }}
                .action-btn:hover {{
                    background: rgba(255, 255, 255, 0.1);
                    color: var(--primary-color);
                }}
                .payment-history {{
                    margin-top: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    overflow: hidden;
                }}
                .history-header {{
                    display: grid;
                    grid-template-columns: 2fr 1fr 1fr 1fr;
                    padding: 1rem;
                    background: rgba(255, 0, 153, 0.1);
                    font-weight: 500;
                }}
                .history-item {{
                    display: grid;
                    grid-template-columns: 2fr 1fr 1fr 1fr;
                    padding: 1rem;
                    align-items: center;
                    transition: all 0.3s ease;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                }}
                .history-item:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.05);
                }}
                .history-item.pending {{
                    background: rgba(255, 170, 0, 0.15);
                    background: rgba(255, 170, 0, 0.05);
                }}
                .status-badge {{
                    padding: 0.3rem 0.8rem;
                    border-radius: 12px;
                    font-size: 0.85rem;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                .status-badge.paid {{
                    background: rgba(0, 179, 104, 0.2);
                    color: #00b368;
                }}
                .status-badge.pending {{
                    background: rgba(255, 170, 0, 0.2);
                    color: #ffaa00;
                }}
                .payment-stats {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 1rem;
                    margin-top: 1rem;
                }}
                .stat-card {{
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.05);
                    padding: 1rem;
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    transition: all 0.3s ease;
                }}
                .stat-card:hover {{
                    background: rgba(255, 0, 153, 0.15);
                    background: rgba(255, 0, 153, 0.1);
                    transform: translateY(-2px);
                }}
                .stat-icon {{
                    width: 40px;
                    height: 40px;
                    background: var(--primary-color);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .stat-info h4 {{
                    font-size: 0.9rem;
                    margin-bottom: 0.2rem;
                }}
                .stat-info p {{
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: var(--primary-color);
                }}
                .mt-4 {{
                    margin-top: 2rem;
                }}
                .text-success {{
                    color: #00b368;
                }}
                .text-warning {{
                    color: #ffaa00;
                }}
                .chart-container {{
                    height: 300px;
                    margin: 2rem 0;
                    padding: 1rem;
                    background: rgba(60, 60, 60, 0.95);
                    background: rgba(255, 255, 255, 0.02);
                    border-radius: 15px;
                    border: 1px solid rgba(255, 0, 153, 0.1);
                    height: 250px; /* Reducido de 300px */
                    margin: 1rem 0; /* Reducido de 2rem */
                    padding: 0.8rem; /* Reducido de 1rem */
                }}
                @media (max-width: 768px) {{
                    .payment-stats {{
                        grid-template-columns: 1fr;
                    }}
                    .history-item {{
                        font-size: 0.9rem;
                    }}
                }}
            </style>
        </head>
        <body>
            {get_common_sidebar()}
            <div class="dashboard-layout">
                <div class="main-content">
                    <div class="header">
                        <h1>
                            <i class="fas fa-file-invoice-dollar header-icon"></i>
                            Centro de Facturación
                        </h1>
                    </div>
                    <div class="billing-grid">
                        <div class="billing-card">
                            <div class="billing-summary">
                                <div class="summary-item">
                                    <div class="summary-value">$25,500</div>
                                    <div class="summary-label">Facturación Anual</div>
                                </div>
                                <div class="summary-item">
                                    <div class="summary-value">15</div>
                                    <div class="summary-label">Facturas Pendientes</div>
                                </div>
                                <div class="summary-item">
                                    <div class="summary-value">85%</div>
                                    <div class="summary-label">Tasa de Pago</div>
                                </div>
                            </div>
                            <div class="section-title">
                                <i class="fas fa-calendar-alt"></i>
                                Facturación Mensual 2024
                            </div>
                            <div class="calendar-grid">
                                <div class="month-card">
                                    <div class="month-name">Enero</div>
                                    <div class="month-amount">$2,500</div>
                                    <div class="month-status status-paid">Pagado</div>
                                </div>
                                <div class="month-card">
                                    <div class="month-name">Febrero</div>
                                    <div class="month-amount">$2,300</div>
                                    <div class="month-status status-paid">Pagado</div>
                                </div>
                                <div class="month-card">
                                    <div class="month-name">Marzo</div>
                                    <div class="month-amount">$2,800</div>
                                    <div class="month-status status-pending">Pendiente</div>
                                </div>
                                <div class="month-card">
                                    <div class="month-name">Abril</div>
                                    <div class="month-amount">$2,100</div>
                                    <div class="month-status status-pending">Próximo</div>
                                </div>
                                <!-- Continuar con los demás meses... -->
                            </div>
                            <div class="chart-container">
                                <canvas id="billingChart"></canvas>
                            </div>
                        </div>
                        <div class="billing-card">
                            <div class="section-title">
                                <i class="fas fa-credit-card"></i>
                                Métodos de Pago y Estado de Cuenta
                            </div>
                            
                            <div class="payment-methods">
                                <div class="payment-method">
                                    <div class="method-icon">
                                        <i class="fab fa-cc-visa"></i>
                                    </div>
                                    <div class="method-details">
                                        <h3>Visa Premium</h3>
                                        <p>**** 4589</p>
                                        <span class="method-status">Principal</span>
                                    </div>
                                    <div class="method-actions">
                                        <button class="action-btn">
                                            <i class="fas fa-pencil-alt"></i>
                                        </button>
                                    </div>
                                </div>
                                <div class="payment-method">
                                    <div class="method-icon mastercard">
                                        <i class="fab fa-cc-mastercard"></i>
                                    </div>
                                    <div class="method-details">
                                        <h3>Mastercard Business</h3>
                                        <p>**** 7856</p>
                                        <span class="method-status">Respaldo</span>
                                    </div>
                                    <div class="method-actions">
                                        <button class="action-btn">
                                            <i class="fas fa-pencil-alt"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div class="section-title mt-4">
                                <i class="fas fa-history"></i>
                                Historial de Pagos
                            </div>
                            
                            <div class="payment-history">
                                <div class="history-header">
                                    <span>Período</span>
                                    <span>Estado</span>
                                    <span>Monto</span>
                                    <span>Método</span>
                                </div>
                                <div class="history-item">
                                    <div class="period">
                                        <i class="fas fa-calendar-check text-success"></i>
                                        Marzo 2024
                                    </div>
                                    <div class="status">
                                        <span class="status-badge paid">
                                            <i class="fas fa-check"></i> Pagado
                                        </span>
                                    </div>
                                    <div class="amount">$2,800</div>
                                    <div class="payment-type">
                                        <i class="fab fa-cc-visa"></i> Visa
                                    </div>
                                </div>
                                <div class="history-item">
                                    <div class="period">
                                        <i class="fas fa-calendar-check text-success"></i>
                                        Febrero 2024
                                    </div>
                                    <div class="status">
                                        <span class="status-badge paid">
                                            <i class="fas fa-check"></i> Pagado
                                        </span>
                                    </div>
                                    <div class="amount">$2,300</div>
                                    <div class="payment-type">
                                        <i class="fab fa-cc-mastercard"></i> Mastercard
                                    </div>
                                </div>
                                <div class="history-item pending">
                                    <div class="period">
                                        <i class="fas fa-clock text-warning"></i>
                                        Abril 2024
                                    </div>
                                    <div class="status">
                                        <span class="status-badge pending">
                                            Pendiente
                                        </span>
                                    </div>
                                    <div class="amount">$2,100</div>
                                    <div class="payment-type">
                                        <i class="fas fa-clock"></i> Por definir
                                    </div>
                                </div>
                            </div>
                            <div class="section-title mt-4">
                                <i class="fas fa-chart-pie"></i>
                                Resumen de Pagos
                            </div>
                            <div class="payment-stats">
                                <div class="stat-card">
                                    <div class="stat-icon">
                                        <i class="fas fa-check-circle"></i>
                                    </div>
                                    <div class="stat-info">
                                        <h4>Pagos a Tiempo</h4>
                                        <p>98%</p>
                                    </div>
                                </div>
                                <div class="stat-card">
                                    <div class="stat-icon">
                                        <i class="fas fa-bolt"></i>
                                    </div>
                                    <div class="stat-info">
                                        <h4>Tiempo Promedio</h4>
                                        <p>2 días antes</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                // Configuración del gráfico
                const ctx = document.getElementById('billingChart').getContext('2d');
                new Chart(ctx, {{
                    type: 'line',
                    data: {{
                        labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
                        datasets: [{{
                            label: 'Facturación Mensual',
                            data: [2500, 2300, 2800, 2100, 2600, 2400, 2700, 2900, 2200, 2400, 2600, 2800],
                            borderColor: '#FF0099',
                            backgroundColor: 'rgba(255, 0, 153, 0.1)',
                            tension: 0.4,
                            fill: true,
                            pointBackgroundColor: '#FF0099',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: '#FF0099',
                            pointRadius: 4,
                            pointHoverRadius: 6
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{
                            legend: {{
                                display: false
                            }},
                            tooltip: {{
                                backgroundColor: 'rgba(0, 0, 0, 0.8)',
                                titleColor: '#FF0099',
                                bodyColor: '#fff',
                                padding: 12,
                                displayColors: false,
                                callbacks: {{
                                    label: function(context) {{
                                        return '$ ' + context.parsed.y;
                                    }}
                                }}
                            }}
                        }},
                        scales: {{
                            y: {{
                                beginAtZero: true,
                                grid: {{
                                    color: 'rgba(255, 255, 255, 0.1)'
                                }},
                                ticks: {{
                                    color: 'rgba(255, 255, 255, 0.8)',
                                    callback: function(value) {{
                                        return '$ ' + value;
                                    }}
                                }}
                            }},
                            x: {{
                                grid: {{
                                    display: false
                                }},
                                ticks: {{
                                    color: 'rgba(255, 255, 255, 0.8)'
                                }}
                            }}
                        }},
                        interaction: {{
                            intersect: false,
                            mode: 'index'
                        }},
                        hover: {{
                            mode: 'nearest',
                            intersect: true
                        }}
                    }}
                }});
            </script>
        </body>
    </html>
    """

serve()