@echo off
echo ========================================
echo  CREAR PAQUETE PARA macOS
echo ========================================
echo.

REM Crear carpeta temporal
if exist CalculadoraProfesional_macOS rmdir /s /q CalculadoraProfesional_macOS
mkdir CalculadoraProfesional_macOS

REM Copiar archivos necesarios
echo Copiando archivos...
copy calculadora.py CalculadoraProfesional_macOS\
copy Calculadora_macOS.command CalculadoraProfesional_macOS\
copy INSTRUCCIONES_MACOS.txt CalculadoraProfesional_macOS\README.txt
copy icono.ico CalculadoraProfesional_macOS\ 2>nul

echo.
echo Archivos copiados:
dir /b CalculadoraProfesional_macOS

echo.
echo ========================================
echo  AHORA CREA EL ZIP MANUALMENTE:
echo ========================================
echo 1. Haz clic derecho en la carpeta "CalculadoraProfesional_macOS"
echo 2. Selecciona "Enviar a" - "Carpeta comprimida (en zip)"
echo 3. Renombra el zip a: CalculadoraProfesional_macOS.zip
echo 4. Coloca el zip en la carpeta dist/
echo.
echo Presiona cualquier tecla cuando termines...
pause >nul

echo.
echo Limpiando carpeta temporal...
rmdir /s /q CalculadoraProfesional_macOS

echo.
echo ¡Listo! Ahora tienes CalculadoraProfesional_macOS.zip
echo.
pause
