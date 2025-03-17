document.addEventListener('DOMContentLoaded', function() {
    // Variables para el carrusel de proceso
    let currentProcessStep = 0;
    const processTrack = document.getElementById('process-track');
    const processSteps = document.querySelectorAll('.process-step');
    const processDots = document.querySelectorAll('.process-dot');
    const totalSteps = processSteps.length;
    let processInterval;

    // Función para actualizar las clases de los pasos
    function updateProcessSteps(index) {
        processSteps.forEach((step, i) => {
            step.classList.remove('active', 'prev', 'next');
            if (i === index) {
                step.classList.add('active');
            } else if (i === (index - 1 + totalSteps) % totalSteps) {
                step.classList.add('prev');
            } else if (i === (index + 1) % totalSteps) {
                step.classList.add('next');
            }
        });

        processDots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
    }

    // Función para ir a un paso específico
    window.goToProcessStep = function(index) {
        if (index < 0) index = totalSteps - 1;
        if (index >= totalSteps) index = 0;
        
        currentProcessStep = index;
        updateProcessSteps(currentProcessStep);
        
        // Reiniciar el intervalo
        clearInterval(processInterval);
        startProcessInterval();
    };

    // Función para ir al paso anterior
    window.prevProcessStep = function() {
        goToProcessStep(currentProcessStep - 1);
    };

    // Función para ir al siguiente paso
    window.nextProcessStep = function() {
        goToProcessStep(currentProcessStep + 1);
    };

    // Función para iniciar la rotación automática
    function startProcessInterval() {
        processInterval = setInterval(() => {
            nextProcessStep();
        }, 5000); // Cambiar cada 5 segundos
    }

    // Inicializar el carrusel
    updateProcessSteps(currentProcessStep);
    startProcessInterval();

    // Pausar la rotación automática al hover
    const processSection = document.querySelector('.process');
    processSection.addEventListener('mouseenter', () => {
        clearInterval(processInterval);
    });

    processSection.addEventListener('mouseleave', () => {
        startProcessInterval();
    });

    // Intersection Observer para animaciones al hacer scroll
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
                if (entry.target.classList.contains('service-card')) {
                    observer.unobserve(entry.target);
                }
            }
        });
    }, observerOptions);

    // Observar elementos que deben animarse
    document.querySelectorAll('.reveal, .service-card').forEach(el => {
        observer.observe(el);
    });

    // Función para scroll suave
    window.scrollToSection = function(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
    };

    // Actualizar sidebar activa basada en scroll
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.sidebar a');

    function updateActiveSection() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop - 60) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href').includes(current)) {
                item.classList.add('active');
            }
        });
    }

    // Throttle para el evento scroll
    let isScrolling = false;
    window.addEventListener('scroll', () => {
        if (!isScrolling) {
            window.requestAnimationFrame(() => {
                updateActiveSection();
                isScrolling = false;
            });
            isScrolling = true;
        }
    });

    // Inicializar estado activo
    updateActiveSection();

    // Manejar modales
    window.closeModal = function() {
        const modal = document.querySelector('.modal-overlay');
        if (modal) {
            modal.classList.add('fade-out');
            setTimeout(() => modal.remove(), 300);
        }
    };

    // Cerrar modal con Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    });

    // Cerrar modal al hacer clic fuera
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-overlay')) {
            closeModal();
        }
    });
}); 