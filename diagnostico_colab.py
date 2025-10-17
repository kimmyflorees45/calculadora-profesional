# ========================================
# DIAGNÓSTICO Y SOLUCIÓN DE ERRORES
# Copia este código en una celda de Colab
# ========================================

import os
import subprocess

print("🔍 DIAGNÓSTICO DEL ENTORNO\n")
print("="*50)

# 1. Verificar archivos
print("\n1️⃣ ARCHIVOS EN EL DIRECTORIO:")
print("-"*50)
files = os.listdir('.')
for f in files:
    size = os.path.getsize(f) if os.path.isfile(f) else "DIR"
    print(f"  {'✅' if os.path.isfile(f) else '📁'} {f} ({size} bytes)" if size != "DIR" else f"  📁 {f}")

required_files = ['calculadora_android.py', 'buildozer.spec']
missing = [f for f in required_files if f not in files]

if missing:
    print(f"\n❌ FALTAN ARCHIVOS: {', '.join(missing)}")
else:
    print("\n✅ Todos los archivos necesarios están presentes")

# 2. Verificar buildozer
print("\n2️⃣ VERIFICAR BUILDOZER:")
print("-"*50)
try:
    result = subprocess.run(['buildozer', '--version'], 
                          capture_output=True, text=True)
    print(f"✅ Buildozer instalado: {result.stdout.strip()}")
except:
    print("❌ Buildozer NO está instalado")
    print("   Ejecuta: !pip install buildozer")

# 3. Verificar Java
print("\n3️⃣ VERIFICAR JAVA:")
print("-"*50)
try:
    result = subprocess.run(['java', '-version'], 
                          capture_output=True, text=True, stderr=subprocess.STDOUT)
    version = result.stdout.split('\n')[0]
    print(f"✅ Java instalado: {version}")
except:
    print("❌ Java NO está instalado")
    print("   Ejecuta: !apt-get install -y openjdk-11-jdk")

# 4. Verificar Python
print("\n4️⃣ VERIFICAR PYTHON:")
print("-"*50)
import sys
print(f"✅ Python {sys.version.split()[0]}")

# 5. Verificar contenido de buildozer.spec
print("\n5️⃣ CONTENIDO DE buildozer.spec:")
print("-"*50)
if 'buildozer.spec' in files:
    with open('buildozer.spec', 'r') as f:
        content = f.read()
        # Verificar campos importantes
        checks = {
            'title': 'title =' in content,
            'package.name': 'package.name =' in content,
            'source.dir': 'source.dir =' in content,
            'requirements': 'requirements =' in content
        }
        for key, found in checks.items():
            print(f"  {'✅' if found else '❌'} {key}")
else:
    print("❌ buildozer.spec no encontrado")

# 6. Verificar calculadora_android.py
print("\n6️⃣ VERIFICAR calculadora_android.py:")
print("-"*50)
if 'calculadora_android.py' in files:
    with open('calculadora_android.py', 'r') as f:
        lines = f.readlines()
        print(f"✅ Archivo encontrado ({len(lines)} líneas)")
        # Verificar imports básicos
        imports = ['from kivy.app import App', 'class', 'def']
        for imp in imports:
            found = any(imp in line for line in lines)
            print(f"  {'✅' if found else '❌'} Contiene: {imp}")
else:
    print("❌ calculadora_android.py no encontrado")

# RESUMEN Y RECOMENDACIONES
print("\n" + "="*50)
print("📋 RESUMEN Y PRÓXIMOS PASOS")
print("="*50)

if missing:
    print("\n🚨 ACCIÓN REQUERIDA:")
    print("   Sube los archivos faltantes a Google Drive")
    print(f"   Archivos: {', '.join(missing)}")
else:
    print("\n✅ Archivos OK - Puedes continuar con la compilación")
    print("\n📝 COMANDO PARA COMPILAR:")
    print("   !buildozer android debug")
    print("\n⏱️ Tiempo estimado: 30-60 minutos (primera vez)")

print("\n" + "="*50)
