@echo off
title Crear Paquete para Linux
color 0B
echo.
echo ========================================
echo   CREAR PAQUETE PARA LINUX
echo ========================================
echo.
echo Este script creara un archivo .tar.gz
echo con todos los archivos necesarios para
echo instalar en Linux.
echo.
pause

echo.
echo Creando directorio temporal...
if exist "CalculadoraProfesional_Linux" rd /s /q "CalculadoraProfesional_Linux"
mkdir "CalculadoraProfesional_Linux"

echo Copiando archivos...
copy /Y "calculadora_completa.py" "CalculadoraProfesional_Linux\" >nul
copy /Y "instalar_linux.sh" "CalculadoraProfesional_Linux\" >nul
copy /Y "icono.ico" "CalculadoraProfesional_Linux\" >nul
copy /Y "INSTALACION_LINUX.md" "CalculadoraProfesional_Linux\README.md" >nul

echo.
echo Archivos copiados:
echo - calculadora_completa.py
echo - instalar_linux.sh
echo - icono.ico
echo - README.md
echo.

echo Para crear el archivo .tar.gz en Linux, ejecuta:
echo tar -czf CalculadoraProfesional_Linux.tar.gz CalculadoraProfesional_Linux/
echo.
echo O comprime la carpeta "CalculadoraProfesional_Linux" con 7-Zip o WinRAR
echo.
echo ========================================
echo   PAQUETE PREPARADO
echo ========================================
echo.
echo La carpeta "CalculadoraProfesional_Linux" contiene
echo todos los archivos necesarios.
echo.
echo Transfiere esta carpeta a Linux y ejecuta:
echo   chmod +x instalar_linux.sh
echo   ./instalar_linux.sh
echo.
pause
