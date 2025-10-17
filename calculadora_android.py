"""
Calculadora Profesional - Versión Android
Optimizada para dispositivos móviles con Kivy
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import math
import re

# Configurar colores
Window.clearcolor = get_color_from_hex('#f5e6f0')

class CalculadoraAndroid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        self.expresion = ""
        self.resultado_anterior = "0"
        self.modo_cientifico = False
        
        # Crear interfaz
        self.crear_display()
        self.crear_botones()
    
    def crear_display(self):
        """Crear el display de la calculadora"""
        display_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=5)
        
        # Expresión
        self.expresion_label = Label(
            text="",
            font_size='18sp',
            color=get_color_from_hex('#9b7ba8'),
            size_hint_y=0.3,
            halign='right',
            valign='middle'
        )
        self.expresion_label.bind(size=self.expresion_label.setter('text_size'))
        
        # Resultado
        self.resultado_label = Label(
            text="0",
            font_size='48sp',
            bold=True,
            color=get_color_from_hex('#7b4b94'),
            size_hint_y=0.7,
            halign='right',
            valign='middle'
        )
        self.resultado_label.bind(size=self.resultado_label.setter('text_size'))
        
        display_layout.add_widget(self.expresion_label)
        display_layout.add_widget(self.resultado_label)
        
        self.add_widget(display_layout)
    
    def crear_botones(self):
        """Crear los botones de la calculadora"""
        # Botón de modo
        btn_modo = Button(
            text="☰ Modo Científico",
            size_hint_y=0.08,
            background_color=get_color_from_hex('#d4a5d4'),
            color=(1, 1, 1, 1),
            font_size='16sp',
            bold=True
        )
        btn_modo.bind(on_press=self.cambiar_modo)
        self.add_widget(btn_modo)
        self.btn_modo = btn_modo
        
        # Grid de botones
        self.botones_grid = GridLayout(cols=4, spacing=8, size_hint_y=0.62)
        self.add_widget(self.botones_grid)
        
        self.crear_botones_basicos()
    
    def crear_botones_basicos(self):
        """Crear botones básicos"""
        self.botones_grid.clear_widgets()
        
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['(', '0', '.', ')'],
            ['±', '^', 'ANS', '=']
        ]
        
        for fila in botones:
            for texto in fila:
                if texto in ['C', '⌫', '%', '±', '(', ')']:
                    bg_color = '#d4a5d4'
                elif texto in ['/', '×', '-', '+', '=', '^']:
                    bg_color = '#f4a6d7'
                elif texto == 'ANS':
                    bg_color = '#d4a5d4'
                else:
                    bg_color = '#e6d0e6'
                
                btn = Button(
                    text=texto,
                    background_color=get_color_from_hex(bg_color),
                    color=(1, 1, 1, 1),
                    font_size='24sp',
                    bold=True
                )
                btn.bind(on_press=lambda x, t=texto: self.click_boton(t))
                self.botones_grid.add_widget(btn)
    
    def crear_botones_cientificos(self):
        """Crear botones científicos"""
        self.botones_grid.clear_widgets()
        self.botones_grid.cols = 5
        
        botones = [
            ['C', '⌫', '(', ')', '%'],
            ['sin', 'cos', 'tan', 'π', 'e'],
            ['ln', 'log', '√', 'x²', 'xʸ'],
            ['7', '8', '9', '/', 'x!'],
            ['4', '5', '6', '×', '1/x'],
            ['1', '2', '3', '-', 'ANS'],
            ['±', '0', '.', '+', '=']
        ]
        
        for fila in botones:
            for texto in fila:
                if texto in ['C', '⌫', '(', ')', '%', '±']:
                    bg_color = '#d4a5d4'
                elif texto in ['/', '×', '-', '+', '=']:
                    bg_color = '#f4a6d7'
                elif texto in ['sin', 'cos', 'tan', 'ln', 'log', '√', 'x²', 'xʸ', 'x!', '1/x', 'π', 'e', 'ANS']:
                    bg_color = '#c89dd1'
                else:
                    bg_color = '#e6d0e6'
                
                btn = Button(
                    text=texto,
                    background_color=get_color_from_hex(bg_color),
                    color=(1, 1, 1, 1),
                    font_size='18sp',
                    bold=True
                )
                btn.bind(on_press=lambda x, t=texto: self.click_boton(t))
                self.botones_grid.add_widget(btn)
    
    def cambiar_modo(self, instance):
        """Cambiar entre modo básico y científico"""
        self.modo_cientifico = not self.modo_cientifico
        
        if self.modo_cientifico:
            self.btn_modo.text = "☰ Modo Básico"
            self.crear_botones_cientificos()
        else:
            self.btn_modo.text = "☰ Modo Científico"
            self.botones_grid.cols = 4
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
        self.expresion += constante
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
        """Evaluar una expresion matematica"""
        expresion = expresion.replace('×', '*')
        expresion = expresion.replace('÷', '/')
        expresion = expresion.replace('^', '**')
        expresion = expresion.replace('π', str(math.pi))
        expresion = re.sub(r'(?<!\d)e(?![-+]?\d)', str(math.e), expresion)
        expresion = re.sub(r'(\d)\(', r'\1*(', expresion)
        expresion = re.sub(r'\)(\d)', r')*\1', expresion)
        expresion = re.sub(r'\)\(', r')*(', expresion)
        
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


class CalculadoraProfesionalApp(App):
    def build(self):
        self.title = 'Calculadora Profesional'
        return CalculadoraAndroid()


if __name__ == '__main__':
    CalculadoraProfesionalApp().run()
