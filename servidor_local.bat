@echo off
echo ========================================
echo  SERVIDOR WEB LOCAL
echo ========================================
echo.
echo Iniciando servidor web...
echo.
echo Tu sitio estara disponible en:
echo.
echo   http://localhost:8000
echo.
echo Para acceder desde otra computadora en tu red:
echo   http://TU_IP:8000
echo.
echo Para ver tu IP, abre otra terminal y escribe: ipconfig
echo Busca "Direccion IPv4"
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
echo ========================================
echo.

cd /d "%~dp0"
python -m http.server 8000

pause
