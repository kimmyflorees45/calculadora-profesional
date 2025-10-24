// Sistema de Cookies
(function() {
    // Verificar si ya aceptó las cookies
    if (localStorage.getItem('cookiesAccepted')) {
        return;
    }

    // Crear banner de cookies
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.innerHTML = `
        <div class="cookie-content">
            <div class="cookie-text">
                <h3>🍪 Uso de Cookies</h3>
                <p>Usamos cookies para mejorar tu experiencia. Al continuar navegando, aceptas nuestros 
                <a href="terminos.html" target="_blank">Términos y Condiciones</a> y 
                <a href="privacidad.html" target="_blank">Política de Privacidad</a>.</p>
            </div>
            <div class="cookie-buttons">
                <button id="accept-cookies" class="cookie-btn accept">Aceptar</button>
                <button id="reject-cookies" class="cookie-btn reject">Rechazar</button>
            </div>
        </div>
    `;

    // Estilos del banner
    const style = document.createElement('style');
    style.textContent = `
        #cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, #7E22CE 0%, #DB2777 100%);
            color: white;
            padding: 20px;
            box-shadow: 0 -5px 20px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            animation: slideUp 0.5s ease-out;
        }

        @keyframes slideUp {
            from {
                transform: translateY(100%);
            }
            to {
                transform: translateY(0);
            }
        }

        .cookie-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .cookie-text h3 {
            margin: 0 0 10px 0;
            font-size: 18px;
        }

        .cookie-text p {
            margin: 0;
            font-size: 14px;
            line-height: 1.5;
        }

        .cookie-text a {
            color: #FFE6F0;
            text-decoration: underline;
        }

        .cookie-buttons {
            display: flex;
            gap: 10px;
        }

        .cookie-btn {
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 14px;
        }

        .cookie-btn.accept {
            background: white;
            color: #7E22CE;
        }

        .cookie-btn.accept:hover {
            background: #F3E8FF;
            transform: scale(1.05);
        }

        .cookie-btn.reject {
            background: transparent;
            color: white;
            border: 2px solid white;
        }

        .cookie-btn.reject:hover {
            background: rgba(255, 255, 255, 0.1);
        }

        @media (max-width: 768px) {
            .cookie-content {
                flex-direction: column;
                text-align: center;
            }

            .cookie-buttons {
                width: 100%;
                justify-content: center;
            }

            .cookie-btn {
                flex: 1;
            }
        }
    `;

    document.head.appendChild(style);
    document.body.appendChild(banner);

    // Manejar aceptación
    document.getElementById('accept-cookies').addEventListener('click', function() {
        localStorage.setItem('cookiesAccepted', 'true');
        banner.style.animation = 'slideDown 0.5s ease-out';
        setTimeout(() => banner.remove(), 500);
    });

    // Manejar rechazo
    document.getElementById('reject-cookies').addEventListener('click', function() {
        alert('Para usar esta aplicación, debes aceptar las cookies.');
    });

    // Agregar animación de salida
    const slideDownStyle = document.createElement('style');
    slideDownStyle.textContent = `
        @keyframes slideDown {
            from {
                transform: translateY(0);
            }
            to {
                transform: translateY(100%);
            }
        }
    `;
    document.head.appendChild(slideDownStyle);
})();
