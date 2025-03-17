from typing import Dict, List, Any

# Site Configuration
SITE_CONFIG: Dict[str, Any] = {
    "name": "Tiffany Paralegal",
    "title": "Tiffany Paralegal - Tu Asistente Legal Virtual",
    "description": "Asistencia legal accesible y comprensible para todos a través de WhatsApp",
    "favicon": "/static/img/favicon.ico",
    "logo": {
        "dark": "/static/img/logo-dark.png",
        "light": "/static/img/logo-light.png"
    }
}

# Theme Configuration
THEME: Dict[str, Any] = {
    "colors": {
        "primary": "#665343",      # Indigo profesional
        "primary_light": "rgba(79, 70, 229, 0.15)",
        "primary_dark": "rgba(79, 70, 229, 0.8)",
        "secondary": "#1E293B",    # Slate oscuro
        "accent": "#818CF8",       # Indigo claro
        "text": "#FFFFFF",
        "background": "e54646",   # Slate más oscuro
        "success": "#10B981",      # Verde para éxito
        "error": "#EF4444",        # Rojo para errores
        "warning": "#F59E0B"       # Amarillo para advertencias
    },
    "glass": {
        "background": "rgba(15, 23, 42, 0.95)",
        "border": "rgba(255, 255, 255, 0.1)"
    },
    "fonts": {
        "heading": {
            "family": "SF Pro Display",
            "weights": {
                "regular": "400",
                "medium": "500",
                "semibold": "600",
                "bold": "700"
            }
        },
        "body": {
            "family": "Poppins",
            "weights": {
                "regular": "400",
                "medium": "500",
                "semibold": "600"
            }
        }
    },
    "spacing": {
        "xs": "0.25rem",
        "sm": "0.5rem",
        "md": "1rem",
        "lg": "1.5rem",
        "xl": "2rem",
        "2xl": "3rem"
    },
    "shadows": {
        "sm": "0 2px 4px rgba(0, 0, 0, 0.1)",
        "md": "0 4px 6px rgba(0, 0, 0, 0.1)",
        "lg": "0 10px 15px rgba(0, 0, 0, 0.1)",
        "primary": "0 4px 15px rgba(79, 70, 229, 0.3)"
    },
    "transitions": {
        "fast": "0.2s ease",
        "normal": "0.3s ease",
        "slow": "0.5s ease"
    },
    "breakpoints": {
        "sm": "640px",
        "md": "768px",
        "lg": "1024px",
        "xl": "1280px"
    }
}

# Sections Configuration
SECTIONS: Dict[str, Any] = {
    "hero": {
        "enabled": True,
        "title": "Bienvenido a Tiffany Paralegal",
        "subtitle": "Tu Asistente Legal Virtual",
        "description": "En Tiffany Paralegal, estamos aquí para hacer que la asistencia legal sea accesible para todos. Sin complicaciones ni jerga legal; solo respuestas claras y soluciones prácticas adaptadas a tus necesidades.",
        "background_image": "/static/img/hero-bg.png",
        "cta_primary": {
            "text": "Comenzar Ahora",
            "url": "#contact"
        },
        "cta_secondary": {
            "text": "Conoce Más",
            "url": "#about"
        }
    },
    "about": {
        "enabled": True,
        "title": "Conócenos",
        "description": "Tiffany Paralegal es un espacio digital creado para brindarte el apoyo legal que necesitas, sin importar tu edad o experiencia. Nuestro objetivo es empoderarte con información y herramientas legales que faciliten tu vida.",
        "items": [
            {
                "icon": "fas fa-balance-scale",
                "title": "Asistencia Legal Accesible",
                "description": "Hacemos que el derecho sea comprensible para todos"
            },
            {
                "icon": "fas fa-comments",
                "title": "Atención por WhatsApp",
                "description": "Respuestas rápidas y personalizadas a tus consultas"
            },
            {
                "icon": "fas fa-file-alt",
                "title": "Documentos Claros",
                "description": "Generamos documentos legales simples y efectivos"
            }
        ]
    },
    "services": {
        "enabled": True,
        "title": "Nuestros Servicios",
        "subtitle": "Soluciones Legales a tu Alcance",
        "description": "Ofrecemos una amplia gama de servicios centrados en la generación de los documentos más solicitados en la legislación colombiana.",
        "items": [
            {
                "title": "Contratos",
                "subtitle": "Documentos Legales",
                "description": "Creación de contratos legales simples, claros y efectivos para tu negocio o necesidades personales.",
                "icon": "fas fa-file-signature",
                "features": [
                    "Contratos de Trabajo",
                    "Contratos de Arrendamiento",
                    "Contratos de Prestación de Servicios",
                    "Contratos de Compraventa"
                ]
            },
            {
                "title": "Demandas",
                "subtitle": "Protección de Derechos",
                "description": "Preparación de demandas que te ayuden a hacer valer tus derechos de manera efectiva.",
                "icon": "fas fa-gavel",
                "features": [
                    "Tutelas",
                    "Derechos de Petición",
                    "Demandas Laborales",
                    "Reclamaciones"
                ]
            },
            {
                "title": "Documentos",
                "subtitle": "Gestiones Administrativas",
                "description": "Elaboración de cartas, solicitudes y documentos para trámites administrativos.",
                "icon": "fas fa-folder-open",
                "features": [
                    "Cartas Formales",
                    "Solicitudes",
                    "Peticiones",
                    "Recursos"
                ]
            }
        ]
    },
    "process": {
        "enabled": True,
        "title": "Tu Proceso Paso a Paso",
        "description": "Simplificamos el proceso legal para que puedas obtener la ayuda que necesitas de manera rápida y efectiva.",
        "items": [
            {
                "number": "01",
                "title": "Consulta",
                "description": "Cuéntanos sobre tu necesidad o situación legal por WhatsApp"
            },
            {
                "number": "02",
                "title": "Generación",
                "description": "Creamos el documento que necesitas de manera sencilla"
            },
            {
                "number": "03",
                "title": "Revisión",
                "description": "Verifica que el documento cumpla con tus expectativas"
            },
            {
                "number": "04",
                "title": "Asistencia",
                "description": "Seguimiento continuo para resolver tus dudas"
            }
        ]
    },
    "contact": {
        "enabled": True,
        "title": "Estamos Aquí Para Ti",
        "description": "¿Necesitas ayuda legal? Contáctanos ahora y obtén la asistencia que necesitas.",
        "info": {
            "address": "Bogotá, Colombia",
            "phone": "+57 300 123 4567",
            "email": "info@tiffanyparalegal.com"
        }
    }
}

# Definición de elementos de navegación
NAV_ITEMS = [
    {"id": "inicio", "text": "Inicio", "icon": "fa-home"},
    {"id": "servicios", "text": "Servicios", "icon": "fa-list-check"},
    {"id": "nosotros", "text": "Nosotros", "icon": "fa-users"},
    {"id": "contacto", "text": "Contacto", "icon": "fa-envelope"}
]


# Social Links
SOCIAL_LINKS: List[Dict[str, str]] = [
    {"platform": "WhatsApp", "url": "https://wa.me/573001234567", "icon": "fab fa-whatsapp"},
    {"platform": "Facebook", "url": "https://facebook.com/tiffanyparalegal", "icon": "fab fa-facebook"},
    {"platform": "Instagram", "url": "https://instagram.com/tiffanyparalegal", "icon": "fab fa-instagram"},
    {"platform": "LinkedIn", "url": "https://linkedin.com/company/tiffanyparalegal", "icon": "fab fa-linkedin"}
]

# Footer Configuration
FOOTER_CONFIG: Dict[str, Any] = {
    "copyright": "© 2024 Tiffany Paralegal. Todos los derechos reservados.",
    "credits": "Desarrollado con <i class='fas fa-heart'></i> por Tiffany Labs",
    "links": [
        {"text": "Términos y Condiciones", "url": "/terms"},
        {"text": "Política de Privacidad", "url": "/privacy"},
        {"text": "Preguntas Frecuentes", "url": "/faq"},
        {"text": "Blog Legal", "url": "/blog"}
    ]
}

# API Configuration
API_CONFIG: Dict[str, Any] = {
    "base_url": "https://api.tiffanyparalegal.com",
    "version": "v1",
    "endpoints": {
        "contact": "/contact",
        "whatsapp": "/whatsapp",
        "documents": "/documents"
    }
} 