import tkinter as tk
from tkinter import ttk, messagebox
import math
import re
import random

class CalculadoraCompleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Profesional")
        self.root.geometry("450x600")  # Tamaño optimizado
        self.root.minsize(400, 550)
        self.root.resizable(True, True)
        self.root.configure(bg='#f5e6f0')
        
        # No maximizar por defecto para mejor visualización
        # self.root.state('zoomed')
        
        # Variables
        self.expresion = ""
        self.resultado_anterior = "0"
        self.modo_cientifico = False
        
        # Configurar estilo
        self.configurar_estilos()
        
        # Crear interfaz
        self.crear_display()
        self.crear_botones()
        
        # Vincular evento de redimensionamiento
        self.root.bind('<Configure>', self.ajustar_interfaz)
    
    def ajustar_interfaz(self, event=None):
        """Ajustar interfaz cuando cambia el tamaño de la ventana"""
        pass  # Los elementos ya se ajustan automáticamente con pack
        
    def configurar_estilos(self):
        """Configurar estilos modernos para la calculadora"""
        style = ttk.Style()
        style.theme_use('clam')
        
    def crear_display(self):
        """Crear el display de la calculadora"""
        # Frame para el display (compacto)
        display_frame = tk.Frame(self.root, bg='#f5e6f0')
        display_frame.pack(fill='x', padx=3, pady=2)
        
        # Label para mostrar la expresión
        self.expresion_label = tk.Label(
            display_frame,
            text="",
            font=('Arial', 11),
            bg='#f5e6f0',
            fg='#9b7ba8',
            anchor='e',
            justify='right',
            height=1
        )
        self.expresion_label.pack(fill='x', padx=10, pady=(5, 0))
        
        # Label para mostrar el resultado
        self.resultado_label = tk.Label(
            display_frame,
            text="0",
            font=('Arial', 36, 'bold'),
            bg='#f5e6f0',
            fg='#7b4b94',
            anchor='e',
            justify='right',
            height=1
        )
        self.resultado_label.pack(fill='x', padx=10, pady=(0, 5))
        
        # Frame para botones de modo y juego (más anchos)
        botones_superiores = tk.Frame(display_frame, bg='#f5e6f0')
        botones_superiores.pack(fill='x', padx=5, pady=(1, 1))
        
        # Botón para cambiar modo
        self.btn_modo = tk.Button(
            botones_superiores,
            text="☰ Modo Científico",
            font=('Arial', 10, 'bold'),
            bg='#d4a5d4',
            fg='#ffffff',
            activebackground='#e0b8e0',
            activeforeground='#ffffff',
            border=0,
            cursor='hand2',
            command=self.cambiar_modo,
            pady=8,
            relief='flat',
            highlightthickness=0
        )
        self.btn_modo.pack(side='left', fill='both', expand=True, padx=(0, 3))
        
        # Botón para juego de divisiones
        self.btn_juego = tk.Button(
            botones_superiores,
            text="🎮 Juego de Divisiones",
            font=('Arial', 10, 'bold'),
            bg='#f4a6d7',
            fg='#ffffff',
            activebackground='#f7bfe3',
            activeforeground='#ffffff',
            border=0,
            cursor='hand2',
            command=self.abrir_juego_divisiones,
            pady=8,
            relief='flat',
            highlightthickness=0
        )
        self.btn_juego.pack(side='left', fill='both', expand=True, padx=(3, 0))
        
    def crear_botones(self):
        """Crear los botones de la calculadora"""
        # Frame principal para botones con peso para expandir
        self.botones_frame = tk.Frame(self.root, bg='#f5e6f0')
        self.botones_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Crear botones básicos
        self.crear_botones_basicos()
        
    def crear_botones_basicos(self):
        """Crear botones de calculadora básica"""
        # Limpiar frame completamente
        for widget in self.botones_frame.winfo_children():
            widget.destroy()
        
        # Resetear configuración del grid
        for i in range(10):  # Limpiar todas las filas posibles
            self.botones_frame.grid_rowconfigure(i, weight=0)
        for j in range(10):  # Limpiar todas las columnas posibles
            self.botones_frame.grid_columnconfigure(j, weight=0)
        
        # Definir botones básicos
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['(', '0', '.', ')'],
            ['±', '^', 'ANS', '=']
        ]
        
        # Colores para diferentes tipos de botones
        color_numero = '#e6d0e6'
        color_operador = '#f4a6d7'
        color_especial = '#d4a5d4'
        
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                # Determinar color del botón
                if texto in ['C', '⌫', '%', '±', '(', ')']:
                    bg_color = color_especial
                    fg_color = '#ffffff'
                elif texto in ['/', '×', '-', '+', '=', '^']:
                    bg_color = color_operador
                    fg_color = '#ffffff'
                elif texto == 'ANS':
                    bg_color = color_especial
                    fg_color = '#ffffff'
                else:
                    bg_color = color_numero
                    fg_color = '#ffffff'
                
                # Crear botón con tamaño moderado
                btn = tk.Button(
                    self.botones_frame,
                    text=texto,
                    font=('Arial', 20, 'bold'),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=self.color_mas_claro(bg_color),
                    activeforeground='#ffffff',
                    border=0,
                    cursor='hand2',
                    command=lambda t=texto: self.click_boton(t),
                    relief='flat',
                    highlightthickness=0
                )
                
                # Posicionar botón
                btn.grid(row=i, column=j, sticky='nsew', padx=4, pady=4)
                
                # Efecto hover
                btn.bind('<Enter>', lambda e, b=btn, c=bg_color: b.config(bg=self.color_mas_claro(c)))
                btn.bind('<Leave>', lambda e, b=btn, c=bg_color: b.config(bg=c))
        
        # Configurar peso de filas y columnas para que ocupen todo el espacio
        for i in range(6):  # 6 filas que realmente se usan
            self.botones_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # 4 columnas que realmente se usan
            self.botones_frame.grid_columnconfigure(j, weight=1)
    
    def crear_botones_cientificos(self):
        """Crear botones de calculadora científica"""
        # Limpiar frame completamente
        for widget in self.botones_frame.winfo_children():
            widget.destroy()
        
        # Resetear configuración del grid
        for i in range(10):  # Limpiar todas las filas posibles
            self.botones_frame.grid_rowconfigure(i, weight=0)
        for j in range(10):  # Limpiar todas las columnas posibles
            self.botones_frame.grid_columnconfigure(j, weight=0)
        
        # Definir botones científicos
        botones = [
            ['C', '⌫', '(', ')', '%'],
            ['sin', 'cos', 'tan', 'π', 'e'],
            ['ln', 'log', '√', 'x²', 'xʸ'],
            ['7', '8', '9', '/', 'x!'],
            ['4', '5', '6', '×', '1/x'],
            ['1', '2', '3', '-', 'ANS'],
            ['±', '0', '.', '+', '=']
        ]
        
        # Colores
        color_numero = '#e6d0e6'
        color_operador = '#f4a6d7'
        color_especial = '#d4a5d4'
        color_funcion = '#c89dd1'
        
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                # Determinar color del botón
                if texto in ['C', '⌫', '(', ')', '%', '±']:
                    bg_color = color_especial
                    fg_color = '#ffffff'
                elif texto in ['/', '×', '-', '+', '=']:
                    bg_color = color_operador
                    fg_color = '#ffffff'
                elif texto in ['sin', 'cos', 'tan', 'ln', 'log', '√', 'x²', 'xʸ', 'x!', '1/x', 'π', 'e', 'ANS']:
                    bg_color = color_funcion
                    fg_color = '#ffffff'
                else:
                    bg_color = color_numero
                    fg_color = '#ffffff'
                
                # Crear botón más pequeño para científica
                btn = tk.Button(
                    self.botones_frame,
                    text=texto,
                    font=('Arial', 14, 'bold'),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=self.color_mas_claro(bg_color),
                    activeforeground='#ffffff',
                    border=0,
                    cursor='hand2',
                    command=lambda t=texto: self.click_boton(t),
                    relief='flat',
                    highlightthickness=0
                )
                
                # Posicionar botón - hacer que '=' ocupe 2 columnas
                if texto == '=':
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=3, pady=3)
                else:
                    btn.grid(row=i, column=j, sticky='nsew', padx=3, pady=3)
                
                # Efecto hover
                btn.bind('<Enter>', lambda e, b=btn, c=bg_color: b.config(bg=self.color_mas_claro(c)))
                btn.bind('<Leave>', lambda e, b=btn, c=bg_color: b.config(bg=c))
        
        # Configurar peso de filas y columnas
        for i in range(7):
            self.botones_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.botones_frame.grid_columnconfigure(j, weight=1)
    
    def color_mas_claro(self, color_hex):
        """Hacer un color más claro para efecto hover"""
        if color_hex == '#e6d0e6':
            return '#f0dff0'
        elif color_hex == '#f4a6d7':
            return '#f7bfe3'
        elif color_hex == '#d4a5d4':
            return '#e0b8e0'
        elif color_hex == '#c89dd1':
            return '#d6b3dd'
        return color_hex
    
    def cambiar_modo(self):
        """Cambiar entre modo básico y científico"""
        self.modo_cientifico = not self.modo_cientifico
        
        if self.modo_cientifico:
            self.btn_modo.config(text="☰ Modo Básico")
            self.root.minsize(450, 600)
            self.crear_botones_cientificos()
        else:
            self.btn_modo.config(text="☰ Modo Científico")
            self.root.minsize(350, 500)
            self.crear_botones_basicos()
    
    def click_boton(self, tecla):
        """Manejar clicks en los botones"""
        try:
            if tecla == 'C':
                self.limpiar()
            elif tecla == '⌫':
                self.borrar()
            elif tecla == '=':
                self.calcular()
            elif tecla == '±':
                self.cambiar_signo()
            elif tecla == 'sin':
                self.funcion_trigonometrica('sin')
            elif tecla == 'cos':
                self.funcion_trigonometrica('cos')
            elif tecla == 'tan':
                self.funcion_trigonometrica('tan')
            elif tecla == 'ln':
                self.funcion_logaritmica('ln')
            elif tecla == 'log':
                self.funcion_logaritmica('log')
            elif tecla == '√':
                self.raiz_cuadrada()
            elif tecla == 'x²':
                self.cuadrado()
            elif tecla == 'xʸ':
                self.agregar_operador('^')
            elif tecla == 'x!':
                self.factorial()
            elif tecla == '1/x':
                self.inverso()
            elif tecla == 'π':
                self.agregar_constante('π')
            elif tecla == 'e':
                self.agregar_constante('e')
            elif tecla == 'ANS':
                self.agregar_respuesta_anterior()
            elif tecla == '^':
                self.agregar_operador('^')
            elif tecla in ['/', '×', '-', '+', '%', '(', ')']:
                self.agregar_operador(tecla)
            else:
                self.agregar_numero(tecla)
        except Exception as e:
            self.mostrar_error()
    
    def limpiar(self):
        """Limpiar la calculadora"""
        self.expresion = ""
        self.expresion_label.config(text="")
        self.resultado_label.config(text="0")
    
    def borrar(self):
        """Borrar el último carácter"""
        if self.expresion:
            self.expresion = self.expresion[:-1]
            self.expresion_label.config(text=self.expresion)
            if not self.expresion:
                self.resultado_label.config(text="0")
    
    def agregar_numero(self, numero):
        """Agregar un número a la expresión"""
        self.expresion += str(numero)
        self.expresion_label.config(text=self.expresion)
        self.resultado_label.config(text=self.expresion)
    
    def agregar_operador(self, operador):
        """Agregar un operador a la expresión"""
        # Permitir operador menos al inicio o después de otro operador para números negativos
        if operador == '-':
            # Permitir - al inicio o después de operadores/paréntesis
            if not self.expresion or self.expresion[-1] in ['/', '×', '+', '%', '^', '(']:
                self.expresion += operador
                self.expresion_label.config(text=self.expresion)
                return
        
        if self.expresion and self.expresion[-1] not in ['/', '×', '-', '+', '%', '^', '(']:
            self.expresion += operador
            self.expresion_label.config(text=self.expresion)
        elif operador == '(':
            # Permitir paréntesis al inicio o después de operadores
            if not self.expresion or self.expresion[-1] in ['/', '×', '-', '+', '%', '^', '(']:
                self.expresion += operador
                self.expresion_label.config(text=self.expresion)
        elif operador == ')' and self.expresion:
            self.expresion += operador
            self.expresion_label.config(text=self.expresion)
    
    def agregar_constante(self, constante):
        """Agregar una constante matemática"""
        if constante == 'π':
            self.expresion += 'π'
        elif constante == 'e':
            self.expresion += 'e'
        self.expresion_label.config(text=self.expresion)
    
    def agregar_respuesta_anterior(self):
        """Agregar la respuesta anterior"""
        self.expresion += self.resultado_anterior
        self.expresion_label.config(text=self.expresion)
    
    def cambiar_signo(self):
        """Cambiar el signo del número actual o agregar paréntesis con negativo"""
        if not self.expresion:
            # Si está vacío, agregar signo negativo
            self.expresion = '-'
            self.expresion_label.config(text=self.expresion)
            return
        
        # Intentar cambiar el signo del último número en la expresión
        try:
            # Si la expresión completa es un número, cambiar su signo
            valor = float(self.expresion)
            self.expresion = str(-valor)
            self.expresion_label.config(text=self.expresion)
            self.resultado_label.config(text=self.expresion)
        except:
            # Si no es un número simple, agregar (-
            # Buscar el último número en la expresión
            import re
            # Buscar el último número (puede incluir punto decimal)
            match = re.search(r'([+-]?\d+\.?\d*)$', self.expresion)
            if match:
                numero = match.group(1)
                inicio = match.start()
                try:
                    valor = float(numero)
                    nuevo_numero = str(-valor)
                    self.expresion = self.expresion[:inicio] + nuevo_numero
                    self.expresion_label.config(text=self.expresion)
                except:
                    # Si falla, agregar paréntesis con negativo
                    self.expresion += '(-'
                    self.expresion_label.config(text=self.expresion)
            else:
                # Si no hay número al final, agregar paréntesis con negativo
                if self.expresion[-1] in ['/', '×', '+', '-', '%', '^', '(']:
                    self.expresion += '(-'
                else:
                    self.expresion += '×(-'
                self.expresion_label.config(text=self.expresion)
    
    def funcion_trigonometrica(self, funcion):
        """Aplicar función trigonométrica"""
        if self.expresion:
            try:
                valor = self.evaluar_expresion(self.expresion)
                radianes = math.radians(valor)
                
                if funcion == 'sin':
                    resultado = math.sin(radianes)
                elif funcion == 'cos':
                    resultado = math.cos(radianes)
                elif funcion == 'tan':
                    resultado = math.tan(radianes)
                
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"{funcion}({valor})")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def funcion_logaritmica(self, funcion):
        """Aplicar función logarítmica"""
        if self.expresion:
            try:
                valor = self.evaluar_expresion(self.expresion)
                
                if funcion == 'ln':
                    resultado = math.log(valor)
                elif funcion == 'log':
                    resultado = math.log10(valor)
                
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"{funcion}({valor})")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def raiz_cuadrada(self):
        """Calcular raíz cuadrada"""
        if self.expresion:
            try:
                valor = self.evaluar_expresion(self.expresion)
                resultado = math.sqrt(valor)
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"√({valor})")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def cuadrado(self):
        """Calcular cuadrado"""
        if self.expresion:
            try:
                valor = self.evaluar_expresion(self.expresion)
                resultado = valor ** 2
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"({valor})²")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def factorial(self):
        """Calcular factorial"""
        if self.expresion:
            try:
                valor = int(self.evaluar_expresion(self.expresion))
                if valor < 0:
                    self.mostrar_error()
                    return
                resultado = math.factorial(valor)
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"{valor}!")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def inverso(self):
        """Calcular inverso (1/x)"""
        if self.expresion:
            try:
                valor = self.evaluar_expresion(self.expresion)
                if valor == 0:
                    self.mostrar_error()
                    return
                resultado = 1 / valor
                self.expresion = str(resultado)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=f"1/({valor})")
                self.resultado_label.config(text=self.formatear_resultado(resultado))
            except:
                self.mostrar_error()
    
    def calcular(self):
        """Calcular el resultado de la expresión"""
        if self.expresion:
            try:
                resultado = self.evaluar_expresion(self.expresion)
                self.resultado_anterior = str(resultado)
                self.expresion_label.config(text=self.expresion)
                self.resultado_label.config(text=self.formatear_resultado(resultado))
                self.expresion = str(resultado)
            except:
                self.mostrar_error()
    
    def evaluar_expresion(self, expresion):
        """Evaluar una expresion matematica"""
        # Reemplazar simbolos
        expresion = expresion.replace('×', '*')
        expresion = expresion.replace('÷', '/')
        expresion = expresion.replace('^', '**')
        
        # Reemplazar constantes matemáticas (con cuidado de no reemplazar 'e' en números como 1e5)
        import re
        # Reemplazar π
        expresion = expresion.replace('π', str(math.pi))
        # Reemplazar 'e' solo cuando no es parte de notación científica
        expresion = re.sub(r'(?<!\d)e(?![-+]?\d)', str(math.e), expresion)
        
        # Manejar multiplicación implícita antes de paréntesis: 2(3) -> 2*(3)
        expresion = re.sub(r'(\d)\(', r'\1*(', expresion)
        expresion = re.sub(r'\)(\d)', r')*\1', expresion)
        expresion = re.sub(r'\)\(', r')*(', expresion)
        
        # Evaluar de forma segura
        try:
            # Usar eval con un namespace limitado para mayor seguridad
            resultado = eval(expresion, {"__builtins__": {}}, {"math": math})
            return resultado
        except:
            # Si falla, intentar con eval normal
            resultado = eval(expresion)
            return resultado
    
    def formatear_resultado(self, resultado):
        """Formatear el resultado para mostrarlo"""
        if isinstance(resultado, float):
            # Si es un número entero, mostrarlo sin decimales
            if resultado.is_integer():
                return str(int(resultado))
            # Si tiene muchos decimales, redondear
            else:
                return f"{resultado:.10g}"
        return str(resultado)
    
    def mostrar_error(self):
        """Mostrar mensaje de error"""
        self.expresion_label.config(text="Error")
        self.resultado_label.config(text="Error")
        self.expresion = ""
    
    def abrir_juego_divisiones(self):
        """Abrir ventana del juego de divisiones"""
        JuegoDivisiones(self.root)
    
    def iniciar(self):
        """Iniciar la aplicación"""
        # Atajos de teclado
        self.root.bind('<Return>', lambda e: self.click_boton('='))
        self.root.bind('<BackSpace>', lambda e: self.click_boton('⌫'))
        self.root.bind('<Escape>', lambda e: self.click_boton('C'))
        
        # Números y operadores
        for i in range(10):
            self.root.bind(str(i), lambda e, n=i: self.click_boton(str(n)))
        
        self.root.bind('+', lambda e: self.click_boton('+'))
        self.root.bind('-', lambda e: self.click_boton('-'))
        self.root.bind('*', lambda e: self.click_boton('×'))
        self.root.bind('/', lambda e: self.click_boton('/'))
        self.root.bind('.', lambda e: self.click_boton('.'))
        self.root.bind('(', lambda e: self.click_boton('('))
        self.root.bind(')', lambda e: self.click_boton(')'))
        self.root.bind('^', lambda e: self.click_boton('^'))
        
        self.root.mainloop()


class JuegoDivisiones:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Juego de Divisiones")
        self.ventana.geometry("550x650")
        self.ventana.configure(bg='#fce4ec')
        self.ventana.resizable(True, True)
        
        # No maximizar por defecto
        # self.ventana.state('zoomed')
        
        # Variables del juego
        self.puntos = 0
        self.preguntas_respondidas = 0
        self.nivel = 1
        self.generar_pregunta()
        
        # Variables de la calculadora
        self.calc_dividendo = ""
        self.calc_divisor = ""
        self.calc_estado = "dividendo"  # dividendo o divisor
        self.calc_visible = False  # Estado de visibilidad de la calculadora
        
        # Crear interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        """Crear la interfaz del juego"""
        # Frame principal con gradiente suave
        self.main_frame = tk.Frame(self.ventana, bg='#fce4ec')
        self.main_frame.pack(fill='both', expand=True)
        
        # Frame izquierdo - Juego (ocupa toda la pantalla)
        juego_frame = tk.Frame(self.main_frame, bg='#fce4ec')
        juego_frame.pack(fill='both', expand=True, padx=40, pady=30)
        
        # Frame derecho - Calculadora (flotante, inicialmente oculto)
        self.calc_frame = tk.Frame(self.ventana, bg='#ffffff', relief='flat', bd=0)
        self.calc_frame.place_forget()  # Ocultar inicialmente
        
        # Título del juego con diseño lindo
        titulo_frame = tk.Frame(juego_frame, bg='#fce4ec')
        titulo_frame.pack(pady=(0, 20))
        
        titulo = tk.Label(
            titulo_frame,
            text="✨ Juego de Divisiones ✨",
            font=('Comic Sans MS', 32, 'bold'),
            bg='#fce4ec',
            fg='#d81b60'
        )
        titulo.pack()
        
        subtitulo = tk.Label(
            titulo_frame,
            text="¡Aprende mientras te diviertes! 🌸",
            font=('Arial', 14),
            bg='#fce4ec',
            fg='#f06292'
        )
        subtitulo.pack()
        
        # Botón para mostrar/ocultar calculadora (esquina superior derecha)
        self.btn_calc = tk.Button(
            self.ventana,
            text="🧮",
            font=('Segoe UI', 20),
            bg='#f8bbd0',
            fg='#ffffff',
            activebackground='#f48fb1',
            activeforeground='#ffffff',
            border=0,
            cursor='hand2',
            command=self.toggle_calculadora,
            width=3,
            height=1,
            relief='flat'
        )
        self.btn_calc.place(x=20, y=20)
        
        # Frame de información con diseño de tarjetas
        info_frame = tk.Frame(juego_frame, bg='#fce4ec')
        info_frame.pack(pady=15)
        
        # Nivel con estilo de tarjeta
        nivel_card = tk.Frame(info_frame, bg='#ffffff', relief='flat', bd=0)
        nivel_card.grid(row=0, column=0, padx=15)
        
        tk.Label(
            nivel_card,
            text="🌟 Nivel",
            font=('Segoe UI', 12),
            bg='#ffffff',
            fg='#f06292'
        ).pack(padx=30, pady=(10, 5))
        
        self.nivel_label = tk.Label(
            nivel_card,
            text=str(self.nivel),
            font=('Comic Sans MS', 32, 'bold'),
            bg='#ffffff',
            fg='#d81b60'
        )
        self.nivel_label.pack(padx=30, pady=(0, 10))
        
        # Puntos con estilo de tarjeta
        puntos_card = tk.Frame(info_frame, bg='#ffffff', relief='flat', bd=0)
        puntos_card.grid(row=0, column=1, padx=15)
        
        tk.Label(
            puntos_card,
            text="⭐ Puntos",
            font=('Segoe UI', 12),
            bg='#ffffff',
            fg='#f06292'
        ).pack(padx=30, pady=(10, 5))
        
        self.puntos_label = tk.Label(
            puntos_card,
            text=str(self.puntos),
            font=('Comic Sans MS', 32, 'bold'),
            bg='#ffffff',
            fg='#d81b60'
        )
        self.puntos_label.pack(padx=30, pady=(0, 10))
        
        # Pregunta en tarjeta grande
        pregunta_card = tk.Frame(juego_frame, bg='#ffffff', relief='flat', bd=0)
        pregunta_card.pack(pady=30, padx=100, fill='x')
        
        self.pregunta_label = tk.Label(
            pregunta_card,
            text=f"{self.dividendo} ÷ {self.divisor} = ?",
            font=('Comic Sans MS', 48, 'bold'),
            bg='#ffffff',
            fg='#d81b60',
            pady=30
        )
        self.pregunta_label.pack()
        
        # Frame para respuesta
        respuesta_frame = tk.Frame(juego_frame, bg='#fce4ec')
        respuesta_frame.pack(pady=20)
        
        tk.Label(
            respuesta_frame,
            text="💖 Tu respuesta:",
            font=('Segoe UI', 18),
            bg='#fce4ec',
            fg='#f06292'
        ).pack(pady=(0, 10))
        
        # Entry para respuesta con estilo
        entry_container = tk.Frame(respuesta_frame, bg='#ffffff', relief='flat', bd=0)
        entry_container.pack()
        
        self.respuesta_entry = tk.Entry(
            entry_container,
            font=('Comic Sans MS', 28, 'bold'),
            justify='center',
            width=8,
            bg='#ffffff',
            fg='#d81b60',
            insertbackground='#d81b60',
            relief='flat',
            bd=0
        )
        self.respuesta_entry.pack(padx=20, pady=15)
        self.respuesta_entry.focus()
        
        # Validación para solo números
        vcmd = (self.ventana.register(self.validar_numero), '%P')
        self.respuesta_entry.config(validate='key', validatecommand=vcmd)
        
        self.respuesta_entry.bind('<Return>', lambda e: self.verificar_respuesta())
        
        # Botón verificar con estilo lindo
        self.btn_verificar = tk.Button(
            juego_frame,
            text="✨ Verificar ✨",
            font=('Comic Sans MS', 18, 'bold'),
            bg='#f06292',
            fg='#ffffff',
            activebackground='#ec407a',
            activeforeground='#ffffff',
            border=0,
            cursor='hand2',
            command=self.verificar_respuesta,
            padx=50,
            pady=15,
            relief='flat'
        )
        self.btn_verificar.pack(pady=20)
        
        # Label de feedback
        self.feedback_label = tk.Label(
            juego_frame,
            text="",
            font=('Comic Sans MS', 20, 'bold'),
            bg='#fce4ec'
        )
        self.feedback_label.pack(pady=10)
        
        # Explicación
        self.explicacion_label = tk.Label(
            juego_frame,
            text="",
            font=('Segoe UI', 14),
            bg='#fce4ec',
            fg='#f06292',
            wraplength=600
        )
        self.explicacion_label.pack(pady=10)
        
        # Crear calculadora de divisiones (pero no mostrarla aún)
        self.crear_calculadora(self.calc_frame)
        
        # Crear mensaje flotante de feedback (overlay)
        self.crear_mensaje_flotante()
        
    def validar_numero(self, texto):
        """Validar que solo se ingresen números"""
        if texto == "":
            return True
        try:
            int(texto)
            return True
        except ValueError:
            return False
    
    def generar_pregunta(self):
        """Generar una nueva pregunta según el nivel"""
        if self.nivel == 1:
            # Nivel 1: divisiones simples (1-10)
            self.divisor = random.randint(2, 5)
            cociente = random.randint(1, 10)
        elif self.nivel == 2:
            # Nivel 2: divisiones intermedias
            self.divisor = random.randint(2, 9)
            cociente = random.randint(2, 12)
        else:
            # Nivel 3+: divisiones más complejas
            self.divisor = random.randint(2, 12)
            cociente = random.randint(5, 20)
        
        self.dividendo = self.divisor * cociente
        self.respuesta_correcta = cociente
        
    def verificar_respuesta(self):
        """Verificar la respuesta del usuario"""
        try:
            respuesta_usuario = int(self.respuesta_entry.get())
            
            if respuesta_usuario == self.respuesta_correcta:
                # Respuesta correcta
                self.puntos += 10 * self.nivel
                self.preguntas_respondidas += 1
                
                # Mostrar mensaje flotante de éxito (pequeño)
                self.mostrar_mensaje_flotante("✨ ¡Correcto! ✨", "#66bb6a", tamano=20)
                
                self.explicacion_label.config(
                    text=f"{self.dividendo} ÷ {self.divisor} = {self.respuesta_correcta}\n"
                         f"Porque {self.divisor} × {self.respuesta_correcta} = {self.dividendo}"
                )
                
                # Subir de nivel cada 5 preguntas correctas
                if self.preguntas_respondidas % 5 == 0:
                    self.nivel += 1
                    self.nivel_label.config(text=str(self.nivel))
                    # Mostrar mensaje de nivel completado (grande)
                    self.ventana.after(200, lambda: self.mostrar_mensaje_flotante(
                        f"🌟 ¡NIVEL {self.nivel}! 🌟",
                        "#f06292",
                        tamano=36
                    ))
                
                # Generar nueva pregunta inmediatamente
                self.ventana.after(100, self.nueva_pregunta)
                
            else:
                # Respuesta incorrecta
                self.mostrar_mensaje_flotante("❌ Incorrecto", "#ef5350", tamano=20)
                self.explicacion_label.config(
                    text=f"La respuesta correcta es {self.respuesta_correcta}\n"
                         f"{self.dividendo} ÷ {self.divisor} = {self.respuesta_correcta}\n"
                         f"Porque {self.divisor} × {self.respuesta_correcta} = {self.dividendo}"
                )
                # Generar nueva pregunta después de 2 segundos
                self.ventana.after(2000, self.nueva_pregunta)
                
        except ValueError:
            self.mostrar_mensaje_flotante("🤔 Número inválido", "#ffa726", tamano=20)
            
        self.puntos_label.config(text=str(self.puntos))
        
    def nueva_pregunta(self):
        """Generar y mostrar una nueva pregunta"""
        self.generar_pregunta()
        self.pregunta_label.config(text=f"{self.dividendo} ÷ {self.divisor} = ?")
        self.respuesta_entry.delete(0, tk.END)
        self.respuesta_entry.focus()
        self.explicacion_label.config(text="")
    
    def crear_mensaje_flotante(self):
        """Crear el mensaje flotante animado"""
        self.mensaje_flotante = tk.Label(
            self.ventana,
            text="",
            font=('Comic Sans MS', 32, 'bold'),
            bg='#ffffff',
            fg='#66bb6a',
            relief='flat',
            bd=0,
            padx=40,
            pady=20
        )
        # Inicialmente oculto
        self.mensaje_flotante.place_forget()
    
    def mostrar_mensaje_flotante(self, texto, color, tamano=20):
        """Mostrar mensaje flotante animado"""
        # Configurar mensaje con tamaño dinámico
        self.mensaje_flotante.config(
            text=texto, 
            fg=color,
            font=('Comic Sans MS', tamano, 'bold')
        )
        
        # Calcular posición central
        self.ventana.update_idletasks()
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()
        ancho_mensaje = 400
        alto_mensaje = 100
        x = (ancho_ventana - ancho_mensaje) // 2
        y = (alto_ventana - alto_mensaje) // 2 - 100
        
        # Mostrar mensaje
        self.mensaje_flotante.place(x=x, y=y, width=ancho_mensaje, height=alto_mensaje)
        
        # Animar aparición (fade in)
        self.animar_mensaje(0, 1, 0.1, lambda: self.ventana.after(1500, self.ocultar_mensaje_flotante))
    
    def ocultar_mensaje_flotante(self):
        """Ocultar mensaje flotante con animación"""
        self.animar_mensaje(1, 0, -0.1, lambda: self.mensaje_flotante.place_forget())
    
    def animar_mensaje(self, alpha_inicio, alpha_fin, paso, callback):
        """Animar opacidad del mensaje (simulado con color)"""
        # En tkinter no hay opacidad directa, así que solo mostramos/ocultamos
        if paso > 0:
            # Fade in - mostrar inmediatamente
            callback()
        else:
            # Fade out - ocultar después de un delay
            self.ventana.after(300, callback)
    
    def toggle_calculadora(self):
        """Mostrar u ocultar la calculadora flotante"""
        if self.calc_visible:
            # Ocultar calculadora
            self.calc_frame.place_forget()
            self.btn_calc.config(bg='#f8bbd0')
            self.calc_visible = False
        else:
            # Mostrar calculadora flotante en la esquina derecha
            ancho_ventana = self.ventana.winfo_width()
            self.calc_frame.place(x=ancho_ventana-420, y=20, width=400, height=550)
            self.btn_calc.config(bg='#ec407a')
            self.calc_visible = True
    
    def crear_calculadora(self, parent):
        """Crear calculadora de divisiones con diseño lindo"""
        # Título
        titulo_calc = tk.Label(
            parent,
            text="🧮 Calculadora",
            font=('Comic Sans MS', 18, 'bold'),
            bg='#ffffff',
            fg='#d81b60'
        )
        titulo_calc.pack(pady=15)
        
        # Display
        display_frame = tk.Frame(parent, bg='#ffffff')
        display_frame.pack(pady=10, padx=20, fill='x')
        
        self.calc_display = tk.Label(
            display_frame,
            text="0",
            font=('Comic Sans MS', 28, 'bold'),
            bg='#fce4ec',
            fg='#d81b60',
            anchor='e',
            padx=15,
            pady=15,
            relief='flat',
            bd=0
        )
        self.calc_display.pack(fill='x')
        
        # Frame de botones
        botones_frame = tk.Frame(parent, bg='#ffffff')
        botones_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Definir botones
        botones = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['C', '0', '⌫'],
            ['÷', '=', '']
        ]
        
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                if texto == '':
                    continue
                    
                # Determinar color con paleta linda
                if texto == '÷':
                    bg_color = '#f8bbd0'
                elif texto == '=':
                    bg_color = '#f06292'
                elif texto in ['C', '⌫']:
                    bg_color = '#f48fb1'
                else:
                    bg_color = '#fce4ec'
                
                btn = tk.Button(
                    botones_frame,
                    text=texto,
                    font=('Comic Sans MS', 18, 'bold'),
                    bg=bg_color,
                    fg='#d81b60' if texto not in ['÷', '=', 'C', '⌫'] else '#ffffff',
                    activebackground=self.color_mas_claro_calc(bg_color),
                    activeforeground='#ffffff',
                    border=0,
                    cursor='hand2',
                    command=lambda t=texto: self.calc_click(t),
                    relief='flat'
                )
                
                if texto == '=':
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=2, pady=2)
                else:
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        
        # Configurar peso de filas y columnas
        for i in range(5):
            botones_frame.grid_rowconfigure(i, weight=1)
        for j in range(3):
            botones_frame.grid_columnconfigure(j, weight=1)
    
    def color_mas_claro_calc(self, color_hex):
        """Hacer un color más claro para hover de calculadora"""
        colores = {
            '#f8bbd0': '#f48fb1',
            '#f06292': '#ec407a',
            '#f48fb1': '#f06292',
            '#fce4ec': '#f8bbd0'
        }
        return colores.get(color_hex, color_hex)
    
    def calc_click(self, tecla):
        """Manejar clicks en la calculadora"""
        if tecla == 'C':
            self.calc_dividendo = ""
            self.calc_divisor = ""
            self.calc_estado = "dividendo"
            self.calc_display.config(text="0")
        
        elif tecla == '⌫':
            if self.calc_estado == "dividendo" and self.calc_dividendo:
                self.calc_dividendo = self.calc_dividendo[:-1]
                self.calc_display.config(text=self.calc_dividendo if self.calc_dividendo else "0")
            elif self.calc_estado == "divisor" and self.calc_divisor:
                self.calc_divisor = self.calc_divisor[:-1]
                texto = f"{self.calc_dividendo} ÷ {self.calc_divisor}" if self.calc_divisor else f"{self.calc_dividendo} ÷"
                self.calc_display.config(text=texto)
        
        elif tecla == '÷':
            if self.calc_dividendo:
                self.calc_estado = "divisor"
                self.calc_display.config(text=f"{self.calc_dividendo} ÷")
        
        elif tecla == '=':
            if self.calc_dividendo and self.calc_divisor:
                try:
                    dividendo = float(self.calc_dividendo)
                    divisor = float(self.calc_divisor)
                    if divisor == 0:
                        self.calc_display.config(text="Error: ÷ 0")
                    else:
                        resultado = dividendo / divisor
                        # Formatear resultado
                        if resultado == int(resultado):
                            self.calc_display.config(text=str(int(resultado)))
                        else:
                            self.calc_display.config(text=f"{resultado:.4f}")
                    # Reiniciar
                    self.calc_dividendo = ""
                    self.calc_divisor = ""
                    self.calc_estado = "dividendo"
                except:
                    self.calc_display.config(text="Error")
        
        else:  # Números
            if self.calc_estado == "dividendo":
                self.calc_dividendo += tecla
                self.calc_display.config(text=self.calc_dividendo)
            else:  # divisor
                self.calc_divisor += tecla
                self.calc_display.config(text=f"{self.calc_dividendo} ÷ {self.calc_divisor}")


if __name__ == "__main__":
    root = tk.Tk()
    calculadora = CalculadoraCompleta(root)
    calculadora.iniciar()
