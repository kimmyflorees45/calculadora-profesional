"""
CALCULADORA PROFESIONAL - Diseño Rosa/Morado
Optimizada para Android con Kivy
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Ellipse
import math
import random


class CalculadoraRosaApp(App):
    def build(self):
        self.title = "Calculadora Profesional"
        
        # Configurar color de fondo
        Window.clearcolor = (1, 0.9, 0.95, 1)  # Rosa pastel
        
        # NO establecer Window.size para que Android use pantalla completa automáticamente
        
        # Crear ScreenManager
        self.sm = ScreenManager()
        
        # Agregar pantallas
        self.sm.add_widget(CalculadoraScreen(name='calculadora'))
        self.sm.add_widget(JuegoScreen(name='juego'))
        
        return self.sm


class CalculadoraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expresion = ""
        self.resultado_anterior = "0"
        self.modo_cientifico = False
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Layout principal - DEBE ocupar toda la pantalla
        # Usar FloatLayout como base para forzar posicionamiento
        from kivy.uix.floatlayout import FloatLayout
        
        main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        main_layout.size_hint = (1, 1)
        main_layout.pos = (0, 0)
        
        # Barra superior con puntitos y título
        barra_superior = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=dp(40),
            padding=[dp(10), dp(5)],
            spacing=dp(10)
        )
        
        # Fondo morado para la barra
        with barra_superior.canvas.before:
            Color(0.75, 0.65, 0.85, 1)  # Morado claro
            self.barra_bg = RoundedRectangle(
                pos=barra_superior.pos,
                size=barra_superior.size,
                radius=[0]
            )
        barra_superior.bind(
            pos=lambda i, v: setattr(self.barra_bg, 'pos', i.pos),
            size=lambda i, v: setattr(self.barra_bg, 'size', i.size)
        )
        
        # Puntitos de colores (usando Labels simples)
        puntitos_layout = BoxLayout(size_hint=(None, 1), width=dp(60), spacing=dp(8))
        
        # Rojo
        rojo = Label(text='●', font_size=sp(20), color=(1, 0.23, 0.19, 1), size_hint=(None, 1), width=dp(15))
        puntitos_layout.add_widget(rojo)
        
        # Amarillo
        amarillo = Label(text='●', font_size=sp(20), color=(1, 0.76, 0.03, 1), size_hint=(None, 1), width=dp(15))
        puntitos_layout.add_widget(amarillo)
        
        # Verde
        verde = Label(text='●', font_size=sp(20), color=(0.18, 0.8, 0.25, 1), size_hint=(None, 1), width=dp(15))
        puntitos_layout.add_widget(verde)
        
        barra_superior.add_widget(puntitos_layout)
        
        # Título
        titulo_label = Label(
            text='Calculadora Profesional',
            font_size=sp(14),
            color=(0.3, 0.3, 0.3, 1),
            halign='center'
        )
        barra_superior.add_widget(titulo_label)
        
        # Indicador de modo (derecha)
        self.modo_label = Label(
            text='Modo Básico',
            font_size=sp(12),
            color=(0.85, 0.11, 0.38, 1),
            halign='right',
            size_hint=(None, 1),
            width=dp(100)
        )
        barra_superior.add_widget(self.modo_label)
        
        main_layout.add_widget(barra_superior)
        
        # Contenedor con padding para el resto (ocupa todo el espacio restante)
        contenido = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5), size_hint=(1, 1))
        
        # Botones superiores (Modo Científico y Juego)
        botones_superiores = BoxLayout(size_hint=(1, None), height=dp(45), spacing=dp(6))
        
        self.btn_modo = Button(
            text='Modo Científico',
            font_size=sp(13),
            bold=True,
            background_normal='',
            background_color=(0.83, 0.65, 0.83, 1),  # #d4a5d4
            color=(1, 1, 1, 1)
        )
        self.btn_modo.bind(on_press=self.cambiar_modo)
        botones_superiores.add_widget(self.btn_modo)
        
        btn_juego = Button(
            text='Juego de Divisiones',
            font_size=sp(13),
            bold=True,
            background_normal='',
            background_color=(0.96, 0.65, 0.84, 1),  # #f4a6d7
            color=(1, 1, 1, 1)
        )
        btn_juego.bind(on_press=self.abrir_juego)
        botones_superiores.add_widget(btn_juego)
        
        contenido.add_widget(botones_superiores)
        
        # Display después de los botones
        display_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(100), spacing=dp(2))
        
        # Label para expresión (pequeña, arriba)
        self.expresion_label = Label(
            text='',
            font_size=sp(14),
            color=(0.61, 0.48, 0.66, 1),  # #9b7ba8
            halign='right',
            valign='bottom',
            size_hint=(1, 0.3),
            text_size=(Window.width - dp(40), None)
        )
        display_layout.add_widget(self.expresion_label)
        
        # Label para resultado (GRANDE)
        self.resultado_label = Label(
            text='0',
            font_size=sp(48),
            bold=True,
            color=(0.48, 0.29, 0.58, 1),  # #7b4b94
            halign='right',
            valign='top',
            size_hint=(1, 0.7),
            text_size=(Window.width - dp(40), None)
        )
        display_layout.add_widget(self.resultado_label)
        
        contenido.add_widget(display_layout)
        
        # Frame para botones (cambiará según el modo) - ocupa todo el espacio restante
        self.botones_frame = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.crear_botones_basicos()
        contenido.add_widget(self.botones_frame)
        
        main_layout.add_widget(contenido)
        
        # Asegurar que el main_layout ocupe toda la pantalla
        main_layout.size_hint = (1, 1)
        main_layout.pos_hint = {'x': 0, 'y': 0}
        
        # Forzar actualización del layout
        def update_layout(instance, value):
            main_layout.do_layout()
        
        self.bind(size=update_layout, pos=update_layout)
        
        self.add_widget(main_layout)
    
    def crear_botones_basicos(self):
        """Crear botones de calculadora básica"""
        self.botones_frame.clear_widgets()
        
        # Definir botones básicos (igual que en la imagen)
        botones = [
            ['A.C', 'C', '%', '/'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        # Colores
        color_numero = (0.90, 0.82, 0.90, 1)      # #e6d0e6
        color_operador = (0.96, 0.65, 0.84, 1)    # #f4a6d7
        color_especial = (0.83, 0.65, 0.83, 1)    # #d4a5d4
        
        for fila in botones:
            fila_layout = BoxLayout(spacing=dp(6), size_hint=(1, 1), padding=[0, dp(3), 0, dp(3)])
            
            for texto in fila:
                # Determinar color del botón
                if texto in ['A.C', 'C', '%', '±', '(', ')']:
                    bg_color = color_especial
                elif texto in ['/', '×', '-', '+', '=', '^']:
                    bg_color = color_operador
                elif texto == 'ANS':
                    bg_color = color_especial
                else:
                    bg_color = color_numero
                
                btn = Button(
                    text=texto,
                    font_size=sp(24),
                    bold=True,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.click_boton)
                fila_layout.add_widget(btn)
            
            self.botones_frame.add_widget(fila_layout)
    
    def crear_botones_cientificos(self):
        """Crear botones de calculadora científica"""
        self.botones_frame.clear_widgets()
        
        # Definir botones científicos
        botones = [
            ['A.C', 'C', '(', ')', '%'],
            ['sin', 'cos', 'tan', 'π', 'e'],
            ['ln', 'log', '√', 'x²', '^'],
            ['7', '8', '9', '/', 'x!'],
            ['4', '5', '6', '×', '1/x'],
            ['1', '2', '3', '-', 'ANS'],
            ['±', '0', '.', '+', '=']
        ]
        
        # Colores
        color_numero = (0.90, 0.82, 0.90, 1)      # #e6d0e6
        color_operador = (0.96, 0.65, 0.84, 1)    # #f4a6d7
        color_especial = (0.83, 0.65, 0.83, 1)    # #d4a5d4
        color_funcion = (0.78, 0.62, 0.82, 1)     # #c89dd1
        
        for fila in botones:
            fila_layout = BoxLayout(spacing=dp(6), size_hint=(1, 1), padding=[0, dp(3), 0, dp(3)])
            
            for texto in fila:
                # Determinar color del botón
                if texto in ['A.C', 'C', '(', ')', '%', '±']:
                    bg_color = color_especial
                elif texto in ['/', '×', '-', '+', '=']:
                    bg_color = color_operador
                elif texto in ['sin', 'cos', 'tan', 'ln', 'log', '√', 'x²', '^', 'x!', '1/x', 'π', 'e', 'ANS']:
                    bg_color = color_funcion
                else:
                    bg_color = color_numero
                
                btn = Button(
                    text=texto,
                    font_size=sp(16),
                    bold=True,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.click_boton)
                fila_layout.add_widget(btn)
            
            self.botones_frame.add_widget(fila_layout)
    
    def cambiar_modo(self, instance):
        """Cambiar entre modo básico y científico"""
        self.modo_cientifico = not self.modo_cientifico
        
        if self.modo_cientifico:
            self.btn_modo.text = 'Modo Básico'
            self.modo_label.text = 'Modo Científico'
            self.crear_botones_cientificos()
        else:
            self.btn_modo.text = 'Modo Científico'
            self.modo_label.text = 'Modo Básico'
            self.crear_botones_basicos()
    
    def click_boton(self, instance):
        """Manejar clicks en los botones"""
        tecla = instance.text
        
        try:
            if tecla == 'A.C':
                self.limpiar_todo()
            elif tecla == 'C':
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
            elif tecla == '^':
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
    
    def limpiar_todo(self):
        """Limpiar todo (A.C - All Clear)"""
        self.expresion = ""
        self.resultado_anterior = "0"
        self.expresion_label.text = ""
        self.resultado_label.text = "0"
    
    def borrar(self):
        """Borrar el último carácter"""
        if self.expresion:
            self.expresion = self.expresion[:-1]
            self.expresion_label.text = self.expresion
            if not self.expresion:
                self.resultado_label.text = "0"
    
    def agregar_numero(self, numero):
        """Agregar un número a la expresión"""
        self.expresion += str(numero)
        self.expresion_label.text = self.expresion
        self.resultado_label.text = self.expresion
    
    def agregar_operador(self, operador):
        """Agregar un operador a la expresión"""
        if operador == '-':
            if not self.expresion or self.expresion[-1] in ['/', '×', '+', '%', '^', '(']:
                self.expresion += operador
                self.expresion_label.text = self.expresion
                return
        
        if self.expresion and self.expresion[-1] not in ['/', '×', '-', '+', '%', '^', '(']:
            self.expresion += operador
            self.expresion_label.text = self.expresion
        elif operador == '(':
            if not self.expresion or self.expresion[-1] in ['/', '×', '-', '+', '%', '^', '(']:
                self.expresion += operador
                self.expresion_label.text = self.expresion
        elif operador == ')' and self.expresion:
            self.expresion += operador
            self.expresion_label.text = self.expresion
    
    def agregar_constante(self, constante):
        """Agregar una constante matemática"""
        if constante == 'π':
            self.expresion += 'π'
        elif constante == 'e':
            self.expresion += 'e'
        self.expresion_label.text = self.expresion
    
    def agregar_respuesta_anterior(self):
        """Agregar la respuesta anterior"""
        self.expresion += self.resultado_anterior
        self.expresion_label.text = self.expresion
    
    def cambiar_signo(self):
        """Cambiar el signo del número actual"""
        if not self.expresion:
            self.expresion = '-'
            self.expresion_label.text = self.expresion
            return
        
        try:
            valor = float(self.expresion)
            self.expresion = str(-valor)
            self.expresion_label.text = self.expresion
            self.resultado_label.text = self.expresion
        except:
            import re
            match = re.search(r'([+-]?\d+\.?\d*)$', self.expresion)
            if match:
                numero = match.group(1)
                inicio = match.start()
                try:
                    valor = float(numero)
                    nuevo_numero = str(-valor)
                    self.expresion = self.expresion[:inicio] + nuevo_numero
                    self.expresion_label.text = self.expresion
                except:
                    self.expresion += '(-'
                    self.expresion_label.text = self.expresion
            else:
                if self.expresion[-1] in ['/', '×', '+', '-', '%', '^', '(']:
                    self.expresion += '(-'
                else:
                    self.expresion += '×(-'
                self.expresion_label.text = self.expresion
    
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
                self.expresion_label.text = f"{funcion}({valor})"
                self.resultado_label.text = self.formatear_resultado(resultado)
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
                self.expresion_label.text = f"{funcion}({valor})"
                self.resultado_label.text = self.formatear_resultado(resultado)
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
                self.expresion_label.text = f"√({valor})"
                self.resultado_label.text = self.formatear_resultado(resultado)
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
                self.expresion_label.text = f"({valor})²"
                self.resultado_label.text = self.formatear_resultado(resultado)
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
                self.expresion_label.text = f"{valor}!"
                self.resultado_label.text = self.formatear_resultado(resultado)
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
                self.expresion_label.text = f"1/({valor})"
                self.resultado_label.text = self.formatear_resultado(resultado)
            except:
                self.mostrar_error()
    
    def calcular(self):
        """Calcular el resultado de la expresión"""
        if self.expresion:
            try:
                resultado = self.evaluar_expresion(self.expresion)
                self.resultado_anterior = str(resultado)
                self.expresion_label.text = self.expresion
                self.resultado_label.text = self.formatear_resultado(resultado)
                self.expresion = str(resultado)
            except:
                self.mostrar_error()
    
    def evaluar_expresion(self, expresion):
        """Evaluar una expresión matemática"""
        import re
        
        # Reemplazar símbolos
        expresion = expresion.replace('×', '*')
        expresion = expresion.replace('÷', '/')
        expresion = expresion.replace('^', '**')
        
        # Reemplazar constantes matemáticas
        expresion = expresion.replace('π', str(math.pi))
        expresion = re.sub(r'(?<!\d)e(?![-+]?\d)', str(math.e), expresion)
        
        # Manejar multiplicación implícita
        expresion = re.sub(r'(\d)\(', r'\1*(', expresion)
        expresion = re.sub(r'\)(\d)', r')*\1', expresion)
        expresion = re.sub(r'\)\(', r')*(', expresion)
        
        # Evaluar
        try:
            resultado = eval(expresion, {"__builtins__": {}}, {"math": math})
            return resultado
        except:
            resultado = eval(expresion)
            return resultado
    
    def formatear_resultado(self, resultado):
        """Formatear el resultado para mostrarlo"""
        if isinstance(resultado, float):
            if resultado.is_integer():
                return str(int(resultado))
            else:
                return f"{resultado:.10g}"
        return str(resultado)
    
    def mostrar_error(self):
        """Mostrar mensaje de error"""
        self.expresion_label.text = "Error"
        self.resultado_label.text = "Error"
        self.expresion = ""
    
    def abrir_juego(self, instance):
        """Cambiar a la pantalla del juego"""
        self.manager.current = 'juego'


class JuegoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # No necesitamos title ni size_hint en Screen
        
        # Variables del juego
        self.puntos = 0
        self.preguntas_respondidas = 0
        self.nivel = 1
        
        # Variables de la calculadora
        self.calc_dividendo = ""
        self.calc_divisor = ""
        self.calc_estado = "dividendo"
        self.calc_visible = False  # Oculta al inicio
        
        self.generar_pregunta()
        
        # Layout principal con FloatLayout para calculadora flotante
        main_layout = FloatLayout()
        
        # Layout del juego CENTRADO Y BONITO
        layout = BoxLayout(
            orientation='vertical', 
            padding=dp(15), 
            spacing=dp(20),
            size_hint=(1, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.bind(minimum_height=layout.setter('height'))
        
        # Título con decoración y fuente bonita en cursiva
        titulo = Label(
            text='Juego de Divisiones',
            font_size=sp(28),
            bold=True,
            italic=True,  # Cursiva
            color=(0.85, 0.11, 0.38, 1),  # #d81b60
            size_hint=(1, None),
            height=dp(40),
            font_name='Roboto'  # Fuente más bonita
        )
        layout.add_widget(titulo)
        
        subtitulo = Label(
            text='¡Aprende mientras te diviertes!',
            font_size=sp(13),
            color=(0.94, 0.39, 0.57, 1),  # #f06292
            size_hint=(1, None),
            height=dp(25)
        )
        layout.add_widget(subtitulo)
        
        # Info (Nivel y Puntos) con cajas blancas
        info_layout = BoxLayout(size_hint=(1, None), height=dp(100), spacing=dp(15), padding=[dp(10), 0])
        
        # Nivel con fondo lila
        nivel_box = BoxLayout(orientation='vertical', padding=dp(10))
        with nivel_box.canvas.before:
            Color(0.92, 0.85, 0.98, 1)  # Lila claro
            self.nivel_bg = RoundedRectangle(pos=nivel_box.pos, size=nivel_box.size, radius=[dp(10)])
        nivel_box.bind(pos=lambda i, v: setattr(self.nivel_bg, 'pos', i.pos), 
                       size=lambda i, v: setattr(self.nivel_bg, 'size', i.size))
        
        nivel_box.add_widget(Label(
            text='Nivel',
            font_size=sp(12),
            color=(0.94, 0.39, 0.57, 1)
        ))
        self.nivel_label = Label(
            text=str(self.nivel),
            font_size=sp(36),
            bold=True,
            color=(0.85, 0.11, 0.38, 1),
            font_name='Roboto'
        )
        nivel_box.add_widget(self.nivel_label)
        info_layout.add_widget(nivel_box)
        
        # Puntos con fondo lila
        puntos_box = BoxLayout(orientation='vertical', padding=dp(10))
        with puntos_box.canvas.before:
            Color(0.92, 0.85, 0.98, 1)  # Lila claro
            self.puntos_bg = RoundedRectangle(pos=puntos_box.pos, size=puntos_box.size, radius=[dp(10)])
        puntos_box.bind(pos=lambda i, v: setattr(self.puntos_bg, 'pos', i.pos), 
                        size=lambda i, v: setattr(self.puntos_bg, 'size', i.size))
        
        puntos_box.add_widget(Label(
            text='Puntos',
            font_size=sp(12),
            color=(0.94, 0.39, 0.57, 1)
        ))
        self.puntos_label = Label(
            text=str(self.puntos),
            font_size=sp(36),
            bold=True,
            color=(0.85, 0.11, 0.38, 1),
            font_name='Roboto'
        )
        puntos_box.add_widget(self.puntos_label)
        info_layout.add_widget(puntos_box)
        
        layout.add_widget(info_layout)
        
        # Pregunta con fondo lila
        pregunta_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(100), padding=dp(15))
        with pregunta_box.canvas.before:
            Color(0.92, 0.85, 0.98, 1)  # Lila claro
            self.pregunta_bg = RoundedRectangle(pos=pregunta_box.pos, size=pregunta_box.size, radius=[dp(15)])
        pregunta_box.bind(pos=lambda i, v: setattr(self.pregunta_bg, 'pos', i.pos), 
                          size=lambda i, v: setattr(self.pregunta_bg, 'size', i.size))
        
        self.pregunta_label = Label(
            text=f"{self.dividendo} ÷ {self.divisor} = ?",
            font_size=sp(42),
            bold=True,
            color=(0.85, 0.11, 0.38, 1),
            font_name='Roboto'
        )
        pregunta_box.add_widget(self.pregunta_label)
        layout.add_widget(pregunta_box)
        
        # Respuesta
        respuesta_titulo = Label(
            text='Tu respuesta:',
            font_size=sp(15),
            color=(0.94, 0.39, 0.57, 1),
            size_hint=(1, None),
            height=dp(25)
        )
        layout.add_widget(respuesta_titulo)
        
        self.respuesta_input = TextInput(
            text='',
            font_size=sp(24),
            multiline=False,
            input_filter='int',
            halign='center',
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={'center_x': 0.5},
            background_color=(1, 1, 1, 1),
            foreground_color=(0.85, 0.11, 0.38, 1),
            padding=[dp(10), dp(10)]
        )
        layout.add_widget(self.respuesta_input)
        
        # Botón verificar más bonito
        btn_verificar = Button(
            text='Verificar',
            font_size=sp(18),
            bold=True,
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={'center_x': 0.5},
            background_normal='',
            background_color=(0.94, 0.39, 0.57, 1),
            color=(1, 1, 1, 1)
        )
        btn_verificar.bind(on_press=self.verificar_respuesta)
        layout.add_widget(btn_verificar)
        
        # Feedback más pequeño
        self.feedback_label = Label(
            text='',
            font_size=sp(15),
            bold=True,
            size_hint=(1, None),
            height=dp(30)
        )
        layout.add_widget(self.feedback_label)
        
        # Explicación más pequeña
        self.explicacion_label = Label(
            text='',
            font_size=sp(12),
            color=(0.94, 0.39, 0.57, 1),
            size_hint=(1, None),
            height=dp(40)
        )
        layout.add_widget(self.explicacion_label)
        
        # Agregar layout del juego al main_layout
        main_layout.add_widget(layout)
        
        # Botón Inicio/Volver (esquina superior derecha)
        btn_inicio = Button(
            text='Inicio',
            font_size=sp(16),
            background_normal='',
            background_color=(0.97, 0.73, 0.82, 1),  # #f8bbd0
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(dp(80), dp(50)),
            pos_hint={'right': 0.98, 'top': 0.98}
        )
        btn_inicio.bind(on_press=self.volver_calculadora)
        main_layout.add_widget(btn_inicio)
        
        # Botón calculadora flotante (esquina superior IZQUIERDA)
        self.btn_calc = Button(
            text='Calc',
            font_size=sp(16),
            background_normal='',
            background_color=(0.97, 0.73, 0.82, 1),  # Color inactivo
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(dp(80), dp(50)),
            pos_hint={'x': 0.02, 'top': 0.98}  # Esquina superior IZQUIERDA
        )
        self.btn_calc.bind(on_press=self.toggle_calculadora)
        main_layout.add_widget(self.btn_calc)
        
        # Calculadora flotante (OCULTA al inicio) con fondo lila
        self.calc_layout = BoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(5),
            size_hint=(None, None),
            size=(dp(280), dp(400)),
            pos_hint={'right': 0.95, 'top': 0.85}
        )
        
        # Agregar fondo lila con canvas
        with self.calc_layout.canvas.before:
            Color(0.85, 0.75, 0.95, 1)  # Lila claro
            self.calc_bg = RoundedRectangle(
                pos=self.calc_layout.pos,
                size=self.calc_layout.size,
                radius=[dp(15)]
            )
        
        # Actualizar fondo cuando cambie posición/tamaño
        self.calc_layout.bind(pos=self.update_calc_bg, size=self.update_calc_bg)
        
        self.calc_layout.opacity = 0  # Oculta al inicio
        self.crear_calculadora()
        main_layout.add_widget(self.calc_layout)
        
        self.add_widget(main_layout)
    
    def volver_calculadora(self, instance):
        """Volver a la pantalla de la calculadora"""
        self.manager.current = 'calculadora'
    
    def update_calc_bg(self, instance, value):
        """Actualizar posición y tamaño del fondo de la calculadora"""
        self.calc_bg.pos = instance.pos
        self.calc_bg.size = instance.size
    
    def generar_pregunta(self):
        """Generar una nueva pregunta según el nivel"""
        if self.nivel == 1:
            self.divisor = random.randint(2, 5)
            cociente = random.randint(1, 10)
        elif self.nivel == 2:
            self.divisor = random.randint(2, 10)
            cociente = random.randint(1, 15)
        elif self.nivel == 3:
            self.divisor = random.randint(2, 12)
            cociente = random.randint(1, 20)
        else:
            self.divisor = random.randint(2, 15)
            cociente = random.randint(1, 25)
        
        self.dividendo = self.divisor * cociente
        self.respuesta_correcta = cociente
    
    def verificar_respuesta(self, instance):
        """Verificar la respuesta del usuario"""
        if not self.respuesta_input.text:
            self.feedback_label.text = 'Por favor ingresa una respuesta'
            self.feedback_label.color = (1, 0.5, 0, 1)
            return
        
        try:
            respuesta_usuario = int(self.respuesta_input.text)
            self.preguntas_respondidas += 1
            
            if respuesta_usuario == self.respuesta_correcta:
                self.puntos += 1
                self.feedback_label.text = '¡Correcto! ¡Excelente!'
                self.feedback_label.color = (0.2, 0.8, 0.3, 1)
                self.explicacion_label.text = f'¡Muy bien! {self.dividendo} ÷ {self.divisor} = {self.respuesta_correcta}'
                
                # Subir de nivel cada 5 respuestas correctas
                if self.puntos % 5 == 0 and self.nivel < 10:
                    self.nivel += 1
                    self.nivel_label.text = str(self.nivel)
                    self.feedback_label.text += f'\n¡Subiste al nivel {self.nivel}!'
            else:
                self.feedback_label.text = 'Incorrecto. ¡Sigue intentando!'
                self.feedback_label.color = (0.9, 0.2, 0.2, 1)
                self.explicacion_label.text = f'La respuesta correcta es: {self.dividendo} ÷ {self.divisor} = {self.respuesta_correcta}'
            
            self.puntos_label.text = str(self.puntos)
            
            # Generar nueva pregunta después de 2 segundos
            from kivy.clock import Clock
            Clock.schedule_once(self.nueva_pregunta, 2)
            
        except ValueError:
            self.feedback_label.text = '⚠️ Por favor ingresa un número válido'
            self.feedback_label.color = (1, 0.5, 0, 1)
    
    def nueva_pregunta(self, dt):
        """Generar una nueva pregunta"""
        self.generar_pregunta()
        self.pregunta_label.text = f"{self.dividendo} ÷ {self.divisor} = ?"
        self.respuesta_input.text = ''
        self.feedback_label.text = ''
        self.explicacion_label.text = ''
    
    def toggle_calculadora(self, instance):
        """Mostrar u ocultar la calculadora flotante"""
        if self.calc_visible:
            self.calc_layout.opacity = 0
            self.btn_calc.background_color = (0.97, 0.73, 0.82, 1)
            self.calc_visible = False
        else:
            self.calc_layout.opacity = 1
            self.btn_calc.background_color = (0.93, 0.25, 0.48, 1)
            self.calc_visible = True
    
    def crear_calculadora(self):
        """Crear calculadora de divisiones"""
        # Título
        titulo = Label(
            text='Calculadora',
            font_size=sp(18),
            bold=True,
            color=(0.85, 0.11, 0.38, 1),
            size_hint=(1, None),
            height=dp(40)
        )
        self.calc_layout.add_widget(titulo)
        
        # Display
        self.calc_display = Label(
            text='0',
            font_size=sp(24),
            bold=True,
            color=(0.85, 0.11, 0.38, 1),
            size_hint=(1, None),
            height=dp(60)
        )
        self.calc_layout.add_widget(self.calc_display)
        
        # Botones
        botones = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['C', '0', '⌫'],
            ['÷', '=']
        ]
        
        for fila in botones:
            fila_layout = BoxLayout(spacing=dp(3), size_hint=(1, 1))
            for texto in fila:
                if texto == '=':
                    btn = Button(
                        text=texto,
                        font_size=sp(18),
                        bold=True,
                        background_normal='',
                        background_color=(0.94, 0.39, 0.57, 1),
                        color=(1, 1, 1, 1)
                    )
                    btn.bind(on_press=self.calc_click)
                    fila_layout.add_widget(btn)
                    # Agregar espacio vacío para que = ocupe más espacio
                    fila_layout.add_widget(Label(size_hint=(1, 1)))
                else:
                    bg_color = (0.97, 0.73, 0.82, 1) if texto in ['÷', 'C', '⌫'] else (0.99, 0.89, 0.93, 1)
                    btn = Button(
                        text=texto,
                        font_size=sp(18),
                        bold=True,
                        background_normal='',
                        background_color=bg_color,
                        color=(0.85, 0.11, 0.38, 1) if texto not in ['÷', 'C', '⌫'] else (1, 1, 1, 1)
                    )
                    btn.bind(on_press=self.calc_click)
                    fila_layout.add_widget(btn)
            self.calc_layout.add_widget(fila_layout)
    
    def calc_click(self, instance):
        """Manejar clicks en la calculadora"""
        tecla = instance.text
        
        if tecla == 'C':
            self.calc_dividendo = ""
            self.calc_divisor = ""
            self.calc_estado = "dividendo"
            self.calc_display.text = "0"
        
        elif tecla == '⌫':
            if self.calc_estado == "dividendo" and self.calc_dividendo:
                self.calc_dividendo = self.calc_dividendo[:-1]
                self.calc_display.text = self.calc_dividendo if self.calc_dividendo else "0"
            elif self.calc_estado == "divisor" and self.calc_divisor:
                self.calc_divisor = self.calc_divisor[:-1]
                texto = f"{self.calc_dividendo} ÷ {self.calc_divisor}" if self.calc_divisor else f"{self.calc_dividendo} ÷"
                self.calc_display.text = texto
        
        elif tecla == '÷':
            if self.calc_dividendo:
                self.calc_estado = "divisor"
                self.calc_display.text = f"{self.calc_dividendo} ÷"
        
        elif tecla == '=':
            if self.calc_dividendo and self.calc_divisor:
                try:
                    dividendo = float(self.calc_dividendo)
                    divisor = float(self.calc_divisor)
                    if divisor == 0:
                        self.calc_display.text = "Error: ÷ 0"
                    else:
                        resultado = dividendo / divisor
                        if resultado == int(resultado):
                            self.calc_display.text = str(int(resultado))
                        else:
                            self.calc_display.text = f"{resultado:.4f}"
                    self.calc_dividendo = ""
                    self.calc_divisor = ""
                    self.calc_estado = "dividendo"
                except:
                    self.calc_display.text = "Error"
        
        else:  # Números
            if self.calc_estado == "dividendo":
                self.calc_dividendo += tecla
                self.calc_display.text = self.calc_dividendo
            else:  # divisor
                self.calc_divisor += tecla
                self.calc_display.text = f"{self.calc_dividendo} ÷ {self.calc_divisor}"


if __name__ == '__main__':
    CalculadoraRosaApp().run()
