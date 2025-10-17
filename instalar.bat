@echo off
title Instalador - Calculadora Profesional
color 0B
echo.
echo ========================================
echo   INSTALADOR - CALCULADORA PROFESIONAL
echo ========================================
echo.
echo Este instalador copiara la calculadora a:
echo %LOCALAPPDATA%\CalculadoraProfesional
echo.
echo Y creara accesos directos en:
echo - Menu Inicio
echo - Escritorio
echo.
pause

REM Crear directorio de instalacion
set "INSTALL_DIR=%LOCALAPPDATA%\CalculadoraProfesional"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copiar archivos
echo.
echo Copiando archivos...
copy /Y "CalculadoraProfesional.exe" "%INSTALL_DIR%\" >nul
copy /Y "icono.ico" "%INSTALL_DIR%\" >nul

REM Crear acceso directo en el escritorio
echo Creando acceso directo en el escritorio...
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Calculadora Profesional.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\CalculadoraProfesional.exe'; $Shortcut.IconLocation = '%INSTALL_DIR%\icono.ico'; $Shortcut.Save()"

REM Crear acceso directo en el menu inicio
echo Creando acceso directo en el menu inicio...
set "START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs"
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%START_MENU%\Calculadora Profesional.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\CalculadoraProfesional.exe'; $Shortcut.IconLocation = '%INSTALL_DIR%\icono.ico'; $Shortcut.Save()"

REM Crear desinstalador
echo Creando desinstalador...
(
echo @echo off
echo title Desinstalador - Calculadora Profesional
echo color 0C
echo echo.
echo echo ==========================================
echo echo   DESINSTALADOR - CALCULADORA PROFESIONAL
echo echo ==========================================
echo echo.
echo echo Esto eliminara:
echo echo - La aplicacion instalada
echo echo - Los accesos directos
echo echo.
echo pause
echo.
echo echo Eliminando archivos...
echo del /Q "%%USERPROFILE%%\Desktop\Calculadora Profesional.lnk" 2^>nul
echo del /Q "%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\Calculadora Profesional.lnk" 2^>nul
echo rd /S /Q "%%LOCALAPPDATA%%\CalculadoraProfesional" 2^>nul
echo.
echo echo.
echo echo Desinstalacion completada.
echo echo.
echo pause
echo exit
) > "%INSTALL_DIR%\desinstalar.bat"

echo.
echo ========================================
echo   INSTALACION COMPLETADA EXITOSAMENTE
echo ========================================
echo.
echo La calculadora ha sido instalada en:
echo %INSTALL_DIR%
echo.
echo Accesos directos creados en:
echo - Escritorio
echo - Menu Inicio
echo.
echo Para desinstalar, ejecuta:
echo %INSTALL_DIR%\desinstalar.bat
echo.
echo Presiona cualquier tecla para salir...
pause >nul
exit
