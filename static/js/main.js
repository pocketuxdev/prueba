// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Animaciones de números
const observerOptions = {
    threshold: 0.5
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, observerOptions);

document.querySelectorAll('#estadisticas h3').forEach((el) => observer.observe(el));

// Animaciones al hacer scroll
const observerOptionsScroll = {
    threshold: 0.1,
    rootMargin: '0px'
};

const observerScroll = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            if (entry.target.classList.contains('stats')) {
                animateNumbers();
            }
        }
    });
}, observerOptionsScroll);

// Aplicar animaciones a las secciones
document.addEventListener('DOMContentLoaded', () => {
    // Añadir clase fade-in a todas las secciones
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('fade-in');
        observerScroll.observe(section);
    });

    // Smooth scroll para navegación
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animación para números en estadísticas
    const statsSection = document.querySelector('#estadisticas');
    if (statsSection) {
        let animated = false;
        
        const animateNumbers = () => {
            if (animated) return;
            
            document.querySelectorAll('#estadisticas h3').forEach(number => {
                const finalNumber = number.innerText;
                const isPercentage = finalNumber.includes('%');
                const numericValue = parseInt(finalNumber);
                
                let currentNumber = 0;
                const duration = 2000;
                const steps = 60;
                const increment = numericValue / steps;
                const interval = duration / steps;
                
                const counter = setInterval(() => {
                    currentNumber += increment;
                    if (currentNumber >= numericValue) {
                        number.innerText = finalNumber;
                        clearInterval(counter);
                    } else {
                        number.innerText = Math.floor(currentNumber) + (isPercentage ? '%' : '+');
                    }
                }, interval);
            });
            
            animated = true;
        };

        observerScroll.observe(statsSection);
        statsSection.addEventListener('intersect', animateNumbers);
    }
});

// Manejar formularios con HTMX
document.body.addEventListener('htmx:afterSwap', function(event) {
    if (event.detail.target.classList.contains('alert-success')) {
        setTimeout(() => {
            event.detail.target.style.opacity = '0';
            setTimeout(() => {
                event.detail.target.remove();
            }, 300);
        }, 3000);
    }
});

// Efecto de scroll en la navegación
const nav = document.querySelector('nav');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
});

// Marcar enlace activo al hacer scroll
const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });
    
    document.querySelectorAll('nav a').forEach(a => {
        a.classList.remove('active');
        if (a.getAttribute('href') === `#${current}`) {
            a.classList.add('active');
        }
    });
});

// Función para cerrar el modal
function closeModal(event) {
    // Verificar si el click fue en el selector de país o sus elementos
    if (event && (
        event.target.closest('.iti__country-list') || 
        event.target.closest('.iti__flag-container') ||
        event.target.closest('.iti__selected-flag')
    )) {
        return; // No cerrar el modal si se está interactuando con el selector de país
    }

    const modal = document.querySelector('.modal-overlay');
    if (modal) {
        modal.style.opacity = '0';
        setTimeout(() => {
            modal.remove();
        }, 300);
    }
}

// Cerrar modal al hacer clic fuera
document.addEventListener('click', function(event) {
    const modal = document.querySelector('.modal');
    const overlay = document.querySelector('.modal-overlay');
    
    if (overlay && !modal.contains(event.target) && event.target === overlay) {
        closeModal(event);
    }
});

// Cerrar modal con la tecla Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

// Aplicar imágenes de fondo desde atributos de datos
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.card[data-background]').forEach(card => {
        const bgImage = card.getAttribute('data-background');
        card.style.setProperty('--card-bg-image', `url('${bgImage}')`);
    });
});

// Función para cerrar el modal de detalle de producto
function closeProductModal(event) {
    // Solo cerrar si se hace clic en el overlay o en el botón de cerrar
    const overlay = document.querySelector('.producto-modal-overlay');
    const modal = document.querySelector('.producto-modal');
    const closeBtn = document.querySelector('.producto-modal-close');
    
    if (event.target === overlay || event.target === closeBtn || event.target.closest('.producto-modal-close')) {
        overlay.style.opacity = '0';
        setTimeout(() => {
            overlay.remove();
        }, 300);
        event.stopPropagation();
    }
}

// Prevenir que los clics en el modal cierren el modal
document.addEventListener('click', function(event) {
    const modal = document.querySelector('.producto-modal');
    if (modal && modal.contains(event.target) && !event.target.closest('.producto-modal-close') && !event.target.closest('button')) {
        event.stopPropagation();
    }
});

// Función para desplazamiento suave a secciones
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
    // Prevenir comportamiento predeterminado del enlace
    event.preventDefault();
}

// Asegurarse de que todos los enlaces internos tengan desplazamiento suave
document.addEventListener('DOMContentLoaded', function() {
    // Mejorar todos los enlaces que apuntan a secciones internas
    document.querySelectorAll('a[href^="#"], button[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            scrollToSection(targetId);
        });
    });
});

// Animación para las tarjetas de productos
function animateProductCards() {
    const productSection = document.getElementById('hero-slider');
    const cards = productSection.querySelectorAll('.card');
    
    // Función para animar las tarjetas
    function revealCards() {
        cards.forEach((card, index) => {
            // Añadir un retraso escalonado para cada tarjeta
            setTimeout(() => {
                card.classList.add('animate-in');
            }, index * 200); // 200ms de retraso entre cada tarjeta
        });
    }
    
    // Configurar el observador para la sección de productos
    const productObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                revealCards();
                productObserver.unobserve(entry.target); // Solo animar una vez
            }
        });
    }, {
        threshold: 0.2 // Activar cuando al menos el 20% de la sección sea visible
    });
    
    // Observar la sección de productos
    productObserver.observe(productSection);
    
    // También animar si la sección ya está visible al cargar la página
    if (isElementInViewport(productSection)) {
        revealCards();
    }
}

// Función auxiliar para verificar si un elemento está en el viewport
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

// Funciones para el hero slider
let currentHeroSlide = 0;
let heroSliderInterval;
const totalHeroSlides = document.querySelectorAll('.hero-slide').length || 0;

function initHeroSlider() {
    if (totalHeroSlides === 0) return;
    
    updateHeroSlider();
    updateHeroDots();
    startHeroSliderAutoplay();
    
    const heroSlider = document.querySelector('.hero-slider');
    if (!heroSlider) return;
    
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    const track = document.querySelector('.hero-slider-track');
    
    heroSlider.addEventListener('touchstart', (e) => {
        isDragging = true;
        startPos = e.touches[0].clientX;
        stopHeroSliderAutoplay();
        
        // Desactivar la transición durante el arrastre
        if (track) {
            track.style.transition = 'none';
        }
    }, { passive: true });
    
    heroSlider.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        
        const currentPosition = e.touches[0].clientX;
        const diff = currentPosition - startPos;
        
        // Calcular la nueva posición con resistencia en los extremos
        if (track) {
            const maxTranslate = (totalHeroSlides - 1) * 100;
            currentTranslate = (currentHeroSlide * -100) + (diff / heroSlider.offsetWidth * 100);
            
            // Añadir resistencia en los extremos
            if (currentTranslate > 0) {
                currentTranslate = currentTranslate * 0.3;
            } else if (currentTranslate < -maxTranslate) {
                const overscroll = currentTranslate + maxTranslate;
                currentTranslate = -maxTranslate + (overscroll * 0.3);
            }
            
            track.style.transform = `translateX(${currentTranslate}%)`;
        }
    }, { passive: true });
    
    heroSlider.addEventListener('touchend', (e) => {
        isDragging = false;
        // Restaurar la transición suave
        if (track) {
            track.style.transition = 'transform 0.3s ease-out';
        }
        handleHeroSliderSwipe(e);
    }, { passive: true });
    
    // Resto del código de initHeroSlider...
}

function updateHeroSlider() {
    const track = document.querySelector('.hero-slider-track');
    if (!track) return;
    
    // Añadir transición suave
    track.style.transition = 'transform 0.3s ease-out';
    track.style.transform = `translateX(-${currentHeroSlide * 100}%)`;
}

function updateHeroDots() {
    // Actualizar los puntos indicadores
    const dots = document.querySelectorAll('.slider-dot');
    dots.forEach((dot, index) => {
        if (index === currentHeroSlide) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
    
    // Actualizar la barra de navegación con cuadrados
    const navSquares = document.querySelectorAll('.hero-slider-nav-square');
    navSquares.forEach((square, index) => {
        if (index === currentHeroSlide) {
            square.classList.add('active');
        } else {
            square.classList.remove('active');
        }
    });
}

function nextHeroSlide() {
    currentHeroSlide = (currentHeroSlide + 1) % totalHeroSlides;
    updateHeroSlider();
    updateHeroDots();
    resetHeroSliderAutoplay();
}

function prevHeroSlide() {
    currentHeroSlide = (currentHeroSlide - 1 + totalHeroSlides) % totalHeroSlides;
    updateHeroSlider();
    updateHeroDots();
    resetHeroSliderAutoplay();
}

function goToHeroSlide(index) {
    currentHeroSlide = index;
    updateHeroSlider();
    updateHeroDots();
    resetHeroSliderAutoplay();
}

function startHeroSliderAutoplay() {
    stopHeroSliderAutoplay(); // Limpiar cualquier intervalo existente
    heroSliderInterval = setInterval(nextHeroSlide, 6000); // Cambiar slide cada 6 segundos
}

function stopHeroSliderAutoplay() {
    if (heroSliderInterval) {
        clearInterval(heroSliderInterval);
    }
}

function resetHeroSliderAutoplay() {
    stopHeroSliderAutoplay();
    startHeroSliderAutoplay();
}

// Mejoras para el hero slider
function enhanceHeroSlider() {
    const heroSlider = document.querySelector('.hero-slider');
    if (!heroSlider) return;
    
    // Añadir barra de progreso
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    heroSlider.appendChild(progressBar);
    
    // Actualizar la barra de progreso
    function updateProgressBar() {
        const totalSlides = document.querySelectorAll('.hero-slide').length;
        if (totalSlides === 0) return;
        
        const progress = ((currentHeroSlide + 1) / totalSlides) * 100;
        progressBar.style.width = `${progress}%`;
    }
    
    // Mejorar las transiciones
    function enhanceTransitions() {
        const slides = document.querySelectorAll('.hero-slide');
        slides.forEach((slide, index) => {
            // Añadir clase para controlar la visibilidad
            if (index === currentHeroSlide) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });
        
        updateProgressBar();
    }
    
    // Sobrescribir funciones existentes
    const originalNextHeroSlide = window.nextHeroSlide;
    const originalPrevHeroSlide = window.prevHeroSlide;
    const originalGoToHeroSlide = window.goToHeroSlide;
    
    window.nextHeroSlide = function() {
        originalNextHeroSlide();
        enhanceTransitions();
    };
    
    window.prevHeroSlide = function() {
        originalPrevHeroSlide();
        enhanceTransitions();
    };
    
    window.goToHeroSlide = function(index) {
        originalGoToHeroSlide(index);
        enhanceTransitions();
    };
    
    // Inicializar
    enhanceTransitions();
    
    // Añadir soporte para gestos de deslizamiento más suaves
    let touchStartX = 0;
    let touchEndX = 0;
    let touchStartY = 0;
    let touchEndY = 0;
    
    heroSlider.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });
    
    heroSlider.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        touchEndY = e.changedTouches[0].screenY;
        
        // Calcular la distancia y dirección del deslizamiento
        const deltaX = touchEndX - touchStartX;
        const deltaY = touchEndY - touchStartY;
        
        // Solo procesar si el deslizamiento horizontal es mayor que el vertical
        if (Math.abs(deltaX) > Math.abs(deltaY)) {
            if (deltaX < -50) {
                // Deslizar a la izquierda
                nextHeroSlide();
            } else if (deltaX > 50) {
                // Deslizar a la derecha
                prevHeroSlide();
            }
        }
    }, { passive: true });
    
    // Añadir soporte para teclado
    document.addEventListener('keydown', (e) => {
        if (isElementInViewport(heroSlider)) {
            if (e.key === 'ArrowRight') {
                nextHeroSlide();
            } else if (e.key === 'ArrowLeft') {
                prevHeroSlide();
            }
        }
    });
}

// Actualizar la función de inicialización
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar el hero slider
    initHeroSlider();
    
    // Mejorar la experiencia del hero slider
    enhanceHeroSlider();
    
    // Otras inicializaciones...
    if (document.querySelector('.producto-carousel')) {
        initCarousel();
    }
    
    // Configurar el primer agente Tiffany como seleccionado por defecto
    const firstSelector = document.querySelector('.tiffany-selector');
    if (firstSelector) {
        firstSelector.classList.add('selected');
        const agentType = firstSelector.getAttribute('data-agent');
        const agentInput = document.getElementById('agent_type_input');
        if (agentInput) {
            agentInput.value = agentType;
            // Cargar datos predeterminados para el primer agente
            updateFormByAgentType(agentType);
            updateJsonPreview();
        }
    }
    
    // Inicializar el sidebar
    if (document.getElementById('sidebar')) {
        updateSidebar();
    }
    
    // Inicializar animaciones de tarjetas de productos
    animateProductCards();
});

// Funciones para el carrusel de productos
let currentSlide = 0;
const totalSlides = document.querySelectorAll('.producto-slide').length;

function initCarousel() {
    // Inicializar el carrusel
    updateCarousel();
    updateDots();
    
    // Configurar autoplay si se desea
    // setInterval(nextSlide, 5000);
}

function updateCarousel() {
    const track = document.querySelector('.producto-carousel-track');
    if (!track) return;
    
    track.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function updateDots() {
    const dots = document.querySelectorAll('.carousel-dot');
    dots.forEach((dot, index) => {
        if (index === currentSlide) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateCarousel();
    updateDots();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    updateCarousel();
    updateDots();
}

function goToSlide(index) {
    currentSlide = index;
    updateCarousel();
    updateDots();
}

// Función para generar API key aleatoria
function generateApiKey() {
    const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const prefix = 'tif_';
    const keyLength = 32;
    let apiKey = prefix;
    
    for (let i = 0; i < keyLength; i++) {
        apiKey += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    return apiKey;
}

// Función para seleccionar un agente Tiffany
function selectTiffanyAgent(event) {
    const selector = event.target.closest('.tiffany-selector');
    if (!selector) return;
    
    // Remover selección previa
    document.querySelectorAll('.tiffany-selector').forEach(s => s.classList.remove('selected'));
    selector.classList.add('selected');
    
    // Obtener el tipo de agente y endpoint
    const agentType = selector.getAttribute('data-agent');
    const endpoint = selector.getAttribute('data-endpoint');
    
    // Actualizar el input hidden del agent_type
    const agentInput = document.getElementById('agent_type_input');
    if (agentInput) {
        agentInput.value = agentType;
    }
    
    /// Actualizar el campo POST con el endpoint correspondiente
    const postInput = document.querySelector('.post-url-input');
    if (postInput) {
        postInput.value = endpoint;
    }
    
    // Generar nueva API key
    const apiKeyInput = document.querySelector('input[name="api_key"]');
    if (apiKeyInput) {
        apiKeyInput.value = generateApiKey();
    }

    // Hacer scroll a la sección de Request Preview
    setTimeout(() => {
        const apiCodeSection = document.querySelector('.api-code');
        if (apiCodeSection) {
            apiCodeSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }, 300); // Pequeño retraso para que la animación de selección sea visible
    
    // Actualizar campos de ejemplo según el tipo de agente
    updateFormByAgentType(agentType);
    
    // Actualizar el JSON preview
    updateJsonPreview();
    
    // Habilitar el botón Try it
    const tryButton = document.getElementById('try-button');
    if (tryButton) {
        tryButton.disabled = false;
    }
    // Inicializar los inputs de teléfono si no lo están
    setTimeout(() => {
        initPhoneInputs();
    }, 100);
}

// Función para actualizar los campos del formulario según el tipo de agente
function updateFormByAgentType(agentType) {
    const form = document.querySelector('.api-test-form');
    if (!form) return;
    
    // Datos predeterminados para cada tipo de agente
    const agentData = {
        'medical': {
            client_id: 'Hospital Central',
            last_interaction: 'Paciente con hipertensión arterial y diabetes tipo 2. Última consulta hace 3 meses. Requiere seguimiento de medicación y control de glucemia.',
            age: '58',
            email: 'paciente@ejemplo.com',
            phone: '+525512345678',
            platform: 'wp'
        },
        'paralegal': {
            client_id: 'Bufete Jurídico Internacional',
            last_interaction: 'Cliente en proceso de demanda por incumplimiento de contrato. Fase de recopilación de evidencias. Próxima audiencia en 2 semanas.',
            age: '42',
            email: 'cliente@despacho.legal',
            phone: '+525587654321',
            platform: 'voice'
        },
        'betterself': {
            client_id: 'Usuario Premium',
            last_interaction: 'Usuario siguiendo plan de desarrollo personal. Objetivos: mejorar productividad, establecer rutina matutina y completar curso de programación.',
            age: '34',
            email: 'usuario@mejora.personal',
            phone: '+525599887766',
            platform: 'wp'
        }
    };
    
    // Obtener datos para el tipo de agente seleccionado
    const data = agentData[agentType] || {};
    
    // Actualizar campos del formulario
    for (const [key, value] of Object.entries(data)) {
        const field = form.elements[key];
        if (field) {
            if (key === 'phone' && field.iti) {
                // Si es un campo de teléfono con intl-tel-input inicializado
                field.iti.setNumber(value);
            } else {
            field.value = value;
        }
    }
}

    // Actualizar la vista previa del JSON
    updateJsonPreview();
}

// Función para actualizar la vista previa del JSON
function updateJsonPreview() {
    const form = document.querySelector('.api-test-form');
    if (!form) return;
    
    const formData = new FormData(form);
    const jsonData = {};
    
    for (const [key, value] of formData.entries()) {
        // Excluir el campo post_url del JSON
        if (key !== 'post_url') {
        jsonData[key] = value;
        }
    }
    
    const jsonPreview = document.getElementById('json-preview');
    if (jsonPreview) {
        // Formatear el JSON para que se parezca al código de la imagen
        const formattedJson = JSON.stringify(jsonData, null, 4)
            .replace(/"(\w+)":/g, '"$1":'); // Mantener las comillas en las propiedades
        
        jsonPreview.textContent = formattedJson;
        // Aplicar el resaltado de sintaxis
        Prism.highlightElement(jsonPreview);
    }
}

// Función para copiar el código
function copyCode() {
    const codeElement = document.getElementById('json-preview');
    const textToCopy = codeElement.textContent;
    const copyButton = document.querySelector('.copy-button');
    
    navigator.clipboard.writeText(textToCopy).then(() => {
        // Cambiar el estilo del botón para mostrar éxito
        copyButton.classList.add('copied');
        
        // Restaurar el botón después de 2 segundos
        setTimeout(() => {
            copyButton.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Error al copiar:', err);
    });
}

// Control de visibilidad de la sidebar basado en el scroll
document.addEventListener('DOMContentLoaded', function() {
const sidebar = document.getElementById('sidebar');
    const navbar = document.querySelector('nav');
    let lastScrollY = window.scrollY;
let ticking = false;

    if (sidebar && navbar) {
        // Función para actualizar la visibilidad de la sidebar
        function updateSidebarVisibility() {
    const scrollY = window.scrollY;
            const navbarHeight = navbar.offsetHeight;
            const navbarBottom = navbar.getBoundingClientRect().bottom;
    
            // Mostrar sidebar solo cuando se ha scrolleado más allá del navbar
            if (scrollY > navbarHeight && navbarBottom < 0) {
        sidebar.classList.add('visible');
    } else {
        sidebar.classList.remove('visible');
    }
    
            // Actualizar enlaces activos
            updateSidebarActiveLinks();
    
    lastScrollY = scrollY;
    ticking = false;
}

        // Escuchar eventos de scroll
        window.addEventListener('scroll', function() {
            if (!ticking) {
                window.requestAnimationFrame(updateSidebarVisibility);
                ticking = true;
            }
        });
        
        // Configurar enlaces de la sidebar
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Verificar visibilidad inicial
        updateSidebarVisibility();
    }
});

// Función para actualizar los enlaces activos de la sidebar
function updateSidebarActiveLinks() {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;
    
    const sections = ['hero', 'hero-slider', 'estadisticas', 'nosotros', 'contacto'];
    const scrollPosition = window.scrollY + window.innerHeight / 3;
    
    // Encontrar la sección activa actual
    let activeSection = null;
    
    for (const section of sections) {
        const element = document.getElementById(section);
        if (!element) continue;
        
        const offsetTop = element.offsetTop;
        const offsetBottom = offsetTop + element.offsetHeight;
        
        if (scrollPosition >= offsetTop && scrollPosition < offsetBottom) {
            activeSection = section;
            break;
        }
    }
    
    // Si no se encontró ninguna sección activa, usar la primera
    if (!activeSection && sections.length > 0) {
        activeSection = sections[0];
    }
    
    // Actualizar los enlaces activos en la sidebar
        sidebar.querySelectorAll('a').forEach(link => {
        const href = link.getAttribute('href').substring(1);
        if (href === activeSection) {
                link.classList.add('active');
        } else {
            link.classList.remove('active');
            }
        });
    }

// Buscar y actualizar cualquier referencia a #productos por #hero-slider
// Por ejemplo:
document.querySelectorAll('a[href="#productos"]').forEach(link => {
    link.setAttribute('href', '#hero-slider');
});

// Si hay funciones específicas para el carrusel de productos que ya no se necesitan,
// se pueden eliminar o adaptar para trabajar con el hero slider 
// ... existing code ...

function showResponseMessage(message, type) {
    // Crear o actualizar el contenedor del mensaje
    let messageContainer = document.querySelector('.response-message');
    if (!messageContainer) {
        messageContainer = document.createElement('div');
        messageContainer.className = 'response-message';
        const form = document.querySelector('.api-test-form');
        form.appendChild(messageContainer);
    }

    // Configurar el estilo según el tipo de mensaje
    messageContainer.className = `response-message ${type}`;
    messageContainer.textContent = message;

    // Mostrar el mensaje con animación
    messageContainer.style.opacity = '1';
    messageContainer.style.transform = 'translateY(0)';

    // Ocultar el mensaje después de 5 segundos
    setTimeout(() => {
        messageContainer.style.opacity = '0';
        messageContainer.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            messageContainer.remove();
        }, 300);
    }, 5000);
}

// Función para validar el formato del teléfono
function validatePhoneNumber(phone) {
    // Solo permitir números, +, espacios y guiones
    const phoneRegex = /^[0-9+\s-]+$/;
    return phoneRegex.test(phone);
}

// Función para validar el formulario de la API
function validateApiForm() {
    const form = document.querySelector('.api-form');
    const submitButton = document.getElementById('try-button');
    
    // Campos requeridos
    const requiredFields = [
        'api_key',
        'client_id',
        'agent_type',
        'platform',
        'email',
        'phone'
    ];
    
    // Verificar si todos los campos requeridos están llenos
    const isValid = requiredFields.every(field => {
        const input = form.querySelector(`[name="${field}"]`);
        return input && input.value.trim() !== '';
    });

    // Validar específicamente el campo de teléfono
    const phoneInput = form.querySelector('input[name="phone"]');
    if (phoneInput && phoneInput.value.trim() !== '') {
        if (!validatePhoneNumber(phoneInput.value)) {
            phoneInput.setCustomValidity('Por favor, ingresa solo números, +, espacios o guiones');
            showApiMessage('El número de teléfono solo puede contener números, +, espacios o guiones', 'error');
            submitButton.disabled = true;
            return false;
        } else {
            phoneInput.setCustomValidity('');
        }
    }
    
    // Obtener el endpoint del input post_url
    const postUrlInput = form.querySelector('.post-url-input');
    if (!postUrlInput || !postUrlInput.value) {
        showResponseMessage(' ');
        return false;
    }

    // Habilitar/deshabilitar botón
    submitButton.disabled = !isValid;
    
    return isValid;
}

// Añadir validación en tiempo real para los campos de teléfono
function setupPhoneValidation() {
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            if (!validatePhoneNumber(this.value)) {
                this.setCustomValidity('Por favor, ingresa solo números, +, espacios o guiones');
                this.classList.add('invalid');
                if (this.value.trim() !== '') {
                    showApiMessage('El número de teléfono solo puede contener números, +, espacios o guiones', 'error');
                }
            } else {
                this.setCustomValidity('');
                this.classList.remove('invalid');
            }
            // Actualizar el estado del botón de envío
            const form = this.closest('form');
            if (form) {
                const submitButton = form.querySelector('button[type="submit"]');
                if (submitButton) {
                    submitButton.disabled = !validateApiForm();
                }
            }
        });
    });
}

// Función para mostrar mensajes del formulario API
function showApiMessage(message, type = 'success') {
    const form = document.querySelector('.api-form');
    const existingMessage = form.querySelector('.api-message');


    
    // Remover mensaje existente si hay uno
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Crear nuevo mensaje
    const messageDiv = document.createElement('div');
    messageDiv.className = `api-message ${type}`;
    messageDiv.textContent = message;
    
    // Insertar después del botón
    const button = form.querySelector('button[type="submit"]');
    button.parentNode.insertBefore(messageDiv, button.nextSibling);
    
    // Animar entrada
    setTimeout(() => messageDiv.classList.add('show'), 10);
    
    // Remover después de 5 segundos
    setTimeout(() => {
        messageDiv.classList.remove('show');
        setTimeout(() => messageDiv.remove(), 300);
    }, 5000);
}

// Función para manejar el envío del formulario
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Validar formulario antes de enviar
    if (!validateApiForm()) {
        showApiMessage('Por favor completa todos los campos requeridos para activar Tiffany', 'error');
        return false;
    }
    
    const button = event.target;
    
    try {
        // Añadir estado de carga
        button.disabled = true;
        button.classList.add('loading');
        button.textContent = '';
        
        // Simular envío (reemplazar con tu lógica real)
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        showApiMessage('¡Tiffany ha sido activada con éxito!');
        
        // Resetear formulario
        const form = button.closest('form');
        form.reset();
        
        // Actualizar preview del JSON
        updateJsonPreview();
        
    } catch (error) {
        console.error('Error:', error);
        showApiMessage('Error al activar Tiffany. Intenta nuevamente.', 'error');
    } finally {
        // Restaurar estado del botón
        button.classList.remove('loading');
        button.textContent = 'ACTIVATE TIFFANY';
        button.disabled = false;
    }
    
    return false;
}

// Añadir listeners cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.api-form');
    if (form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        
        inputs.forEach(input => {
            input.addEventListener('input', validateApiForm);
            input.addEventListener('change', validateApiForm);
        });
        
        // Validar inicialmente
        validateApiForm();
    }
});

// Función para inicializar todos los inputs de teléfono
function initPhoneInputs() {
    const phoneInputs = document.querySelectorAll('input[name="phone"], input[name="telefono"]');
    
    phoneInputs.forEach(input => {
        if (!input.classList.contains('iti-initialized')) {
            const iti = window.intlTelInput(input, {
                utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/utils.js",
                initialCountry: "co",
                preferredCountries: ["mx", "us", "es", "co", "ar"],
                separateDialCode: true,
                autoPlaceholder: "aggressive",
                formatOnDisplay: true,
                dropdownContainer: document.body
            });
            
            input.classList.add('iti-initialized');
            input.iti = iti;
            
            // Agregar validación en tiempo real
            input.addEventListener('input', function() {
                if (!validatePhoneNumber(this.value)) {
                    this.setCustomValidity('Por favor, ingresa solo números, +, espacios o guiones');
                    this.classList.add('invalid');
                } else {
                    this.setCustomValidity('');
                    this.classList.remove('invalid');
                }
                updatePhoneValue(input);
            });
            
            // Mantener el resto de los event listeners existentes
            input.addEventListener('countrychange', function() {
                updatePhoneValue(input);
                if (document.getElementById('json-preview')) {
                    updateJsonPreview();
                }
            });
            
            if (input.value) {
                iti.setNumber(input.value);
            }
        }
    });
}

// Función para actualizar el valor del teléfono con formato internacional
function updatePhoneValue(input) {
    if (input.iti) {
        // Obtener el número con formato internacional
        const number = input.iti.getNumber();
        if (number) {
            input.value = number;
        }
    }
}

// Inicializar el selector de teléfono internacional en la carga de la página
document.addEventListener('DOMContentLoaded', function() {
    initPhoneInputs();
    
    // Observar cambios en el DOM para detectar cuando se añaden modales
    setupModalObserver();
});

// Configurar un observador para detectar cuando se añaden modales al DOM
function setupModalObserver() {
    // Crear un observador de mutaciones para detectar cuando se añaden nuevos nodos al body
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                // Verificar si alguno de los nodos añadidos es un modal
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) { // Nodo de elemento
                        // Buscar inputs de teléfono en el nuevo nodo
                        const phoneInputs = node.querySelectorAll('input[name="phone"]');
                        if (phoneInputs.length > 0) {
                            // Inicializar los inputs de teléfono en el modal
                            setTimeout(() => {
                                initPhoneInputs();
                            }, 100);
                        }
                    }
                    });
                }
            });
        });
        
    // Configurar el observador para observar cambios en los hijos del body
    observer.observe(document.body, { childList: true, subtree: true });
}

// Modificar la función que maneja las respuestas HTMX para inicializar los inputs de teléfono
document.body.addEventListener('htmx:afterSwap', function(event) {
    // Inicializar los inputs de teléfono después de que HTMX haya actualizado el DOM
    setTimeout(() => {
        initPhoneInputs();
    }, 100);
});

// También inicializar cuando se abra un modal
document.body.addEventListener('htmx:afterOnLoad', function(event) {
    // Verificar si la respuesta contiene un modal
    if (event.detail.xhr.responseText.includes('modal')) {
        setTimeout(() => {
            initPhoneInputs();
        }, 100);
    }
});

// Función para inicializar los labels flotantes
function initFloatingLabels() {
    // Buscar todos los inputs y textareas en grupos con label flotante
    const inputs = document.querySelectorAll('.form-group.floating-label input, .form-group.floating-label textarea, .form-group.floating-label select');
    
    inputs.forEach(input => {
        // Verificar si el input ya tiene contenido al cargar
        if (input.value.trim() !== '') {
            input.classList.add('has-content');
        }
        
        // Para selects, verificar si tienen una opción seleccionada
        if (input.tagName === 'SELECT' && input.value !== '') {
            input.classList.add('has-content');
        }
        
        // Añadir listeners para los eventos focus y blur
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentNode.classList.remove('focused');
            if (this.value.trim() !== '') {
                this.classList.add('has-content');
            } else {
                this.classList.remove('has-content');
            }
        });
        
        // Añadir listener para el evento input
        input.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                this.classList.add('has-content');
            } else {
                this.classList.remove('has-content');
            }
        });
        
        // Para selects, añadir listener para el evento change
        if (input.tagName === 'SELECT') {
            input.addEventListener('change', function() {
                if (this.value !== '') {
                    this.classList.add('has-content');
                } else {
                    this.classList.remove('has-content');
                }
            });
        }
    });
}

// Inicializar los labels flotantes cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    initFloatingLabels();
});

// Modificar la función que maneja las respuestas HTMX para inicializar los labels flotantes
document.body.addEventListener('htmx:afterSwap', function(event) {
    // Inicializar los labels flotantes después de que HTMX haya actualizado el DOM
    setTimeout(() => {
        initFloatingLabels();
    }, 100);
});

// Modificar el observador para inicializar también los labels flotantes
function setupModalObserver() {
    // Crear un observador de mutaciones para detectar cuando se añaden nuevos nodos al body
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                // Verificar si alguno de los nodos añadidos contiene formularios
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) { // Nodo de elemento
                        // Inicializar los inputs de teléfono y los labels flotantes
                        setTimeout(() => {
                            initPhoneInputs();
                            initFloatingLabels();
                        }, 100);
                    }
                });
            }
        });
    });
    
    // Configurar el observador para observar cambios en los hijos del body
    observer.observe(document.body, { childList: true, subtree: true });
}

// Función para animar las estadísticas cuando sean visibles
function animateStats() {
  const statsSection = document.getElementById('estadisticas');
  const statItems = statsSection.querySelectorAll('.grid div');
  
  // Función para animar los elementos
  function revealStats() {
    statItems.forEach((item, index) => {
      // Añadir un retraso escalonado para cada elemento
      setTimeout(() => {
        item.classList.add('animate-in');
      }, index * 200); // 200ms de retraso entre cada elemento
    });
  }
  
  // Configurar el observador para la sección de estadísticas
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        revealStats();
        statsObserver.unobserve(entry.target); // Solo animar una vez
      }
    });
  }, {
    threshold: 0.2 // Activar cuando al menos el 20% de la sección sea visible
  });
  
  // Observar la sección de estadísticas
  statsObserver.observe(statsSection);
  
  // También animar si la sección ya está visible al cargar la página
  if (isElementInViewport(statsSection)) {
    revealStats();
  }
}

// Llamar a la función cuando se cargue el documento
document.addEventListener('DOMContentLoaded', function() {
  animateStats();
});

function handleHeroSliderSwipe(e) {
    const touchEndTime = new Date().getTime();
    const touchDuration = touchEndTime - touchStartTime;
    
    const deltaX = touchEndX - touchStartX;
    const deltaY = touchEndY - touchStartY;
    
    // Calcular velocidad del swipe
    const velocity = Math.abs(deltaX) / touchDuration;
    
    // Umbral mínimo para considerar un swipe válido (en píxeles)
    const minSwipeDistance = 30;
    // Umbral mínimo de velocidad (píxeles por milisegundo)
    const minVelocity = 0.1;
    
    // Solo procesar si el movimiento horizontal es mayor que el vertical
    if (Math.abs(deltaX) > Math.abs(deltaY) && 
        Math.abs(deltaX) > minSwipeDistance && 
        velocity > minVelocity) {
        
        // Calcular la distancia del swipe como porcentaje del ancho del contenedor
        const heroSlider = document.querySelector('.hero-slider');
        const swipePercentage = (Math.abs(deltaX) / heroSlider.offsetWidth) * 100;
        
        // Si el swipe es menor al 15% del ancho, no cambiar de slide
        if (swipePercentage < 15) {
            updateHeroSlider(); // Volver al slide actual
            return;
        }
        
        if (deltaX < 0) {
            // Swipe hacia la izquierda - siguiente slide
            if (currentHeroSlide < totalHeroSlides - 1) {
                nextHeroSlide();
            } else {
                // Si estamos en el último slide, volver al actual
                updateHeroSlider();
            }
        } else {
            // Swipe hacia la derecha - slide anterior
            if (currentHeroSlide > 0) {
                prevHeroSlide();
            } else {
                // Si estamos en el primer slide, volver al actual
                updateHeroSlider();
            }
        }
    } else {
        // Si el swipe no fue suficiente, volver al slide actual
        updateHeroSlider();
    }
}