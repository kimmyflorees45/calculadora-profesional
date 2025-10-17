// Smooth scrolling para los enlaces de navegación
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

// Animación de aparición al hacer scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Aplicar animación a las tarjetas
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.feature-card, .screenshot-card, .download-card, .faq-item');
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
});

// Efecto parallax en el hero
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero-content');
    if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.3}px)`;
        hero.style.opacity = 1 - (scrolled / 600);
    }
});

// Animación de los botones de la calculadora mockup
document.addEventListener('DOMContentLoaded', () => {
    const calcButtons = document.querySelectorAll('.calc-btn');
    
    calcButtons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.1)';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
        });
        
        button.addEventListener('click', (e) => {
            e.preventDefault();
            // Efecto de click
            button.style.transform = 'scale(0.95)';
            setTimeout(() => {
                button.style.transform = 'scale(1)';
            }, 100);
            
            // Actualizar display (simulación)
            const display = document.querySelector('.display-result');
            if (display && button.textContent !== '=' && button.textContent !== 'C') {
                const currentText = display.textContent;
                if (button.textContent === '⌫') {
                    display.textContent = currentText.slice(0, -1) || '0';
                } else if (currentText === '0' || currentText === '201') {
                    display.textContent = button.textContent;
                } else {
                    display.textContent = currentText + button.textContent;
                }
            } else if (button.textContent === 'C') {
                display.textContent = '0';
            } else if (button.textContent === '=') {
                // Animación de resultado
                display.style.transform = 'scale(1.1)';
                display.style.color = '#d81b60';
                setTimeout(() => {
                    display.style.transform = 'scale(1)';
                    display.style.color = '#7b4b94';
                }, 200);
            }
        });
    });
});

// Contador animado para las estadísticas
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target + (element.dataset.suffix || '');
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current) + (element.dataset.suffix || '');
        }
    }, 16);
}

// Activar contadores cuando sean visibles
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            const number = entry.target.querySelector('.stat-number');
            const target = parseInt(number.textContent);
            entry.target.dataset.animated = 'true';
            
            if (number.textContent.includes('%')) {
                number.dataset.suffix = '%';
                animateCounter(number, 100);
            } else if (number.textContent.includes('+')) {
                number.dataset.suffix = '+';
                animateCounter(number, target);
            } else {
                animateCounter(number, target);
            }
        }
    });
}, { threshold: 0.5 });

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.stat').forEach(stat => {
        statsObserver.observe(stat);
    });
});

// Efecto de hover en las tarjetas de descarga
document.addEventListener('DOMContentLoaded', () => {
    const downloadCards = document.querySelectorAll('.download-card');
    
    downloadCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Cambiar el color del navbar al hacer scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        navbar.style.backdropFilter = 'blur(10px)';
    } else {
        navbar.style.background = 'transparent';
        navbar.style.boxShadow = 'none';
    }
});

// Animación de las orbs del fondo
document.addEventListener('DOMContentLoaded', () => {
    const orbs = document.querySelectorAll('.gradient-orb');
    
    orbs.forEach((orb, index) => {
        setInterval(() => {
            const randomX = Math.random() * 100 - 50;
            const randomY = Math.random() * 100 - 50;
            orb.style.transform = `translate(${randomX}px, ${randomY}px) scale(${0.9 + Math.random() * 0.2})`;
        }, 3000 + index * 1000);
    });
});

// Easter egg: Click en el logo
document.addEventListener('DOMContentLoaded', () => {
    const logo = document.querySelector('.logo');
    let clickCount = 0;
    
    logo.addEventListener('click', () => {
        clickCount++;
        
        if (clickCount === 5) {
            // Crear confetti
            createConfetti();
            clickCount = 0;
        }
    });
});

function createConfetti() {
    const colors = ['#d81b60', '#f06292', '#7b4b94', '#f4a6d7', '#d4a5d4'];
    const confettiCount = 50;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.style.position = 'fixed';
        confetti.style.width = '10px';
        confetti.style.height = '10px';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.left = Math.random() * window.innerWidth + 'px';
        confetti.style.top = '-10px';
        confetti.style.opacity = '1';
        confetti.style.borderRadius = '50%';
        confetti.style.pointerEvents = 'none';
        confetti.style.zIndex = '9999';
        confetti.style.transition = 'all 3s ease-out';
        
        document.body.appendChild(confetti);
        
        setTimeout(() => {
            confetti.style.top = window.innerHeight + 'px';
            confetti.style.left = (parseInt(confetti.style.left) + (Math.random() * 200 - 100)) + 'px';
            confetti.style.opacity = '0';
            confetti.style.transform = 'rotate(720deg)';
        }, 10);
        
        setTimeout(() => {
            confetti.remove();
        }, 3000);
    }
}

// Tooltip para los botones de descarga
document.addEventListener('DOMContentLoaded', () => {
    const downloadButtons = document.querySelectorAll('.btn-download');
    
    downloadButtons.forEach(button => {
        button.addEventListener('mouseenter', (e) => {
            const tooltip = document.createElement('div');
            tooltip.className = 'download-tooltip';
            tooltip.textContent = 'Click para ver instrucciones';
            tooltip.style.position = 'absolute';
            tooltip.style.background = 'rgba(0, 0, 0, 0.8)';
            tooltip.style.color = 'white';
            tooltip.style.padding = '8px 12px';
            tooltip.style.borderRadius = '8px';
            tooltip.style.fontSize = '12px';
            tooltip.style.pointerEvents = 'none';
            tooltip.style.zIndex = '1000';
            tooltip.style.whiteSpace = 'nowrap';
            
            document.body.appendChild(tooltip);
            
            const rect = button.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            
            button.dataset.tooltip = 'active';
        });
        
        button.addEventListener('mouseleave', () => {
            const tooltip = document.querySelector('.download-tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
});

// Animación de typing en el hero title (opcional)
document.addEventListener('DOMContentLoaded', () => {
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.style.opacity = '0';
        setTimeout(() => {
            heroTitle.style.transition = 'opacity 1s ease';
            heroTitle.style.opacity = '1';
        }, 300);
    }
});

// Lazy loading para imágenes (si se agregan)
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Prevenir el comportamiento por defecto de los enlaces de descarga
// y mostrar instrucciones personalizadas
document.addEventListener('DOMContentLoaded', () => {
    const downloadLinks = document.querySelectorAll('.btn-download');
    
    downloadLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const platform = link.closest('.download-card').querySelector('h3').textContent;
            let message = '';
            
            switch(platform) {
                case 'Windows':
                    message = '📥 Para Windows:\n\n' +
                             '1. Instala Python 3 desde python.org\n' +
                             '2. Descarga calculadora_completa.py\n' +
                             '3. Ejecuta: python calculadora_completa.py\n\n' +
                             '¿Deseas continuar?';
                    break;
                case 'Linux':
                    message = '📥 Para Linux:\n\n' +
                             '1. Descarga install.sh y calculadora_completa.py\n' +
                             '2. chmod +x install.sh\n' +
                             '3. ./install.sh\n\n' +
                             '¿Deseas continuar?';
                    break;
                case 'macOS':
                    message = '📥 Para macOS:\n\n' +
                             '1. Python 3 ya viene instalado\n' +
                             '2. Descarga calculadora_completa.py\n' +
                             '3. Ejecuta: python3 calculadora_completa.py\n\n' +
                             '¿Deseas continuar?';
                    break;
                case 'Android':
                    message = '📥 Para Android:\n\n' +
                             '1. Instala Pydroid 3 desde Play Store\n' +
                             '2. Descarga calculadora_completa.py\n' +
                             '3. Abre el archivo en Pydroid 3\n\n' +
                             '¿Deseas continuar?';
                    break;
            }
            
            if (confirm(message)) {
                // Aquí podrías iniciar la descarga real
                console.log('Iniciando descarga para ' + platform);
            }
        });
    });
});

console.log('🧮 Calculadora Profesional - Website cargado correctamente');
console.log('💜 Hecho con amor para estudiantes y profesionales');
