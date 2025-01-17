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

@rt('/dashboard')
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard Tiffany Medical Assistant</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            :root {
                --primary-color: #FF0099;
                --primary-hover: #D6006F;
                --background-dark: #000000;
                --text-light: rgba(255, 255, 255, 0.8);
                --border-color: rgba(255, 0, 153, 0.2);
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Poppins', sans-serif;
            }

            body {
                background: var(--background-dark);
                color: var(--text-light);
                min-height: 100vh;
            }

            /* Dashboard Layout Styles */
            .dashboard-layout {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1.5rem;
                padding: 2rem;
                max-width: 100%;
                margin: 0 auto;
            }

            /* Stats Cards Container */
            .stats-container {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 1rem;
                grid-column: 1 / -1;
                margin-bottom: 2rem;
            }

            .stat-card {
                background: rgba(255, 255, 255, 0.05);
                padding: 1.5rem;
                border-radius: 20px;
                text-align: center;
                transition: all 0.3s ease;
            }

            .stat-card:hover {
                transform: translateY(-5px);
                background: rgba(255, 0, 153, 0.1);
            }

            .stat-value {
                font-size: 2.5rem;
                font-weight: 600;
                color: var(--primary-color);
                margin-bottom: 0.5rem;
            }

            /* Charts Grid */
            .charts-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1.5rem;
                grid-column: 1 / -1;
            }

            .chart-container {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 20px;
                padding: 1.5rem;
                min-height: 300px;
                border: 1px solid var(--border-color);
            }

            .chart-container canvas {
                width: 100% !important;
                height: 250px !important;
            }

            /* Media Queries */
            @media (max-width: 1400px) {
                .charts-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }

            @media (max-width: 1024px) {
                .stats-container {
                    grid-template-columns: repeat(2, 1fr);
                }
            }

            @media (max-width: 768px) {
                .dashboard-layout {
                    padding: 1rem;
                }

                .charts-grid {
                    grid-template-columns: 1fr;
                }

                .chart-container {
                    min-height: 250px;
                }

                .chart-container canvas {
                    height: 200px !important;
                }
            }

            /* Mantener estilos existentes */
            .sidebar {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                height: 80px;
                background: rgba(255, 255, 255, 0.1);
                padding: 0 1rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 2rem;
                backdrop-filter: blur(10px);
                box-shadow: 0 -5px 20px rgba(255, 0, 153, 0.2);
                z-index: 1000;
                border-top: 1px solid var(--border-color);
            }

            .nav-item {
                width: 45px;
                height: 45px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.3s ease;
                color: var(--text-light);
                background: rgba(255, 255, 255, 0.1);
                position: relative;
            }

            .nav-item:hover {
                background: var(--primary-hover);
                transform: translateY(-5px);
            }

            .nav-item.active {
                background: var(--primary-color);
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="dashboard-layout">
            <h1>Dashboard Tiffany Medical Assistant</h1>
            
            <div class="stats-container">
                <div class="stat-card">
                    <div class="stat-value">30%</div>
                    <div class="stat-label">Incremento en Follow-ups</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">25%</div>
                    <div class="stat-label">Reducción Tareas Admin</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">5min</div>
                    <div class="stat-label">Tiempo Onboarding</div>
                </div>
            </div>

            <div class="charts-grid">
                <div class="chart-container">
                    <canvas id="engagementChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="automationChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="responseChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="trainingChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="performanceChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="adoptionChart"></canvas>
                </div>
            </div>
        </div>

        <nav class="sidebar">
            <div class="nav-item active" title="Dashboard">
                <i class="fas fa-chart-line"></i>
            </div>
            <div class="nav-item" title="Usuarios">
                <i class="fas fa-users"></i>
            </div>
            <div class="nav-item" title="Configuración">
                <i class="fas fa-cog"></i>
            </div>
            <div class="nav-item" title="Perfil">
                <i class="fas fa-user"></i>
            </div>
        </nav>

        <script>
            // Configuración de los gráficos
            const charts = {
                engagement: {
                    type: 'line',
                    data: {
                        labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
                        datasets: [{
                            label: 'Tasa de Engagement',
                            data: [65, 70, 75, 80, 85, 90],
                            borderColor: '#FF0099',
                            tension: 0.4
                        }]
                    }
                },
                automation: {
                    type: 'bar',
                    data: {
                        labels: ['Agendamiento', 'Follow-ups', 'Recordatorios', 'Onboarding'],
                        datasets: [{
                            label: 'Tasa de Éxito de Automatización',
                            data: [85, 75, 90, 70],
                            backgroundColor: '#FF0099'
                        }]
                    }
                },
                response: {
                    type: 'line',
                    data: {
                        labels: ['8am', '10am', '12pm', '2pm', '4pm', '6pm'],
                        datasets: [{
                            label: 'Tiempo de Respuesta',
                            data: [12, 8, 15, 10, 7, 13],
                            borderColor: '#FF0099'
                        }]
                    }
                }
            };

            // Inicializar los gráficos
            Object.entries(charts).forEach(([id, config]) => {
                const ctx = document.getElementById(`${id}Chart`).getContext('2d');
                new Chart(ctx, {
                    type: config.type,
                    data: config.data,
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                grid: {
                                    color: 'rgba(255, 255, 255, 0.1)'
                                },
                                ticks: {
                                    color: 'rgba(255, 255, 255, 0.8)'
                                }
                            },
                            x: {
                                grid: {
                                    display: false
                                },
                                ticks: {
                                    color: 'rgba(255, 255, 255, 0.8)'
                                }
                            }
                        }
                    }
                });
            });
        </script>
    </body>
    </html>
    """

serve()