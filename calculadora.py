from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.metrics import dp, sp
import math
import random


class CalculadoraApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expresion = ""
        self.expresion_calc_div = ""
        self.puntuacion = 0
        self.intentos = 0
        self.respuesta_correcta = 0
    
    def build(self):
        self.title = 'Calculadora Completa'
        
        panel = TabbedPanel(do_default_tab=False, tab_pos='top_mid', tab_height=dp(45))
        
        # ========== PESTAÑA 1: BÁSICA ==========
        tab1 = TabbedPanelItem(text='Básica')
        layout1 = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5))
        
        self.display1 = TextInput(
            text='0', readonly=True, halign='right',
            font_size=sp(32), size_hint=(1, 0.2)
        )
        layout1.add_widget(self.display1)
        
        botones_basicos = [
            ['C', '←', '%', '/'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for fila in botones_basicos:
            h = BoxLayout(spacing=dp(5))
            for btn_text in fila:
                if btn_text == '=':
                    btn = Button(text=btn_text, font_size=sp(24), size_hint=(2, 1))
                else:
                    btn = Button(text=btn_text, font_size=sp(20))
                btn.bind(on_press=lambda x, t=btn_text: self.click_basica(t))
                h.add_widget(btn)
            layout1.add_widget(h)
        
        tab1.add_widget(layout1)
        panel.add_widget(tab1)
        
        # ========== PESTAÑA 2: CIENTÍFICA ==========
        tab2 = TabbedPanelItem(text='Científica')
        layout2 = BoxLayout(orientation='vertical', padding=dp(8), spacing=dp(4))
        
        self.display2 = TextInput(
            text='0', readonly=True, halign='right',
            font_size=sp(28), size_hint=(1, None), height=dp(70)
        )
        layout2.add_widget(self.display2)
        
        botones_cientificos = [
            ['sin', 'cos', 'tan', 'π', 'e'],
            ['ln', 'log', '√', 'x²', 'x!'],
            ['(', ')', '^', '1/x', 'C'],
            ['7', '8', '9', '/', '←'],
            ['4', '5', '6', 'x', '-'],
            ['1', '2', '3', '+', '.'],
            ['0', 'ANS', '=']
        ]
        
        for fila in botones_cientificos:
            h = BoxLayout(spacing=dp(3))
            for btn_text in fila:
                if btn_text == '=':
                    btn = Button(text=btn_text, font_size=sp(18), size_hint=(2, 1))
                else:
                    btn = Button(text=btn_text, font_size=sp(16))
                btn.bind(on_press=lambda x, t=btn_text: self.click_cientifica(t))
                h.add_widget(btn)
            layout2.add_widget(h)
        
        tab2.add_widget(layout2)
        panel.add_widget(tab2)
        
        # ========== PESTAÑA 3: JUEGO DIVISIONES ==========
        tab3 = TabbedPanelItem(text='Juego')
        layout3 = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(6))
        
        self.label_titulo = Label(
            text='🎓 Aprende a Dividir',
            font_size=sp(20), size_hint=(1, None), height=dp(45)
        )
        layout3.add_widget(self.label_titulo)
        
        self.label_puntuacion = Label(
            text='Puntos: 0/0',
            font_size=sp(16), size_hint=(1, None), height=dp(35)
        )
        layout3.add_widget(self.label_puntuacion)
        
        self.label_problema = Label(
            text='',
            font_size=sp(26), size_hint=(1, None), height=dp(55)
        )
        layout3.add_widget(self.label_problema)
        
        self.display3 = TextInput(
            text='',
            font_size=sp(28), halign='center',
            size_hint=(1, None), height=dp(65), input_filter='int'
        )
        layout3.add_widget(self.display3)
        
        self.label_mensaje = Label(
            text='¡Escribe tu respuesta!',
            font_size=sp(16), size_hint=(1, None), height=dp(50)
        )
        layout3.add_widget(self.label_mensaje)
        
        # Botones de control
        controles = BoxLayout(size_hint=(1, None), height=dp(50), spacing=dp(5))
        
        btn_verificar = Button(text='✓ Verificar', font_size=sp(16))
        btn_verificar.bind(on_press=self.verificar)
        controles.add_widget(btn_verificar)
        
        btn_nuevo = Button(text='Siguiente', font_size=sp(16))
        btn_nuevo.bind(on_press=self.nuevo_problema)
        controles.add_widget(btn_nuevo)
        
        btn_reset = Button(text='Reiniciar', font_size=sp(16))
        btn_reset.bind(on_press=self.reiniciar)
        controles.add_widget(btn_reset)
        
        layout3.add_widget(controles)
        
        # MINI CALCULADORA DE DIVISIONES
        calc_label = Label(
            text='📱 Mini Calculadora de Divisiones',
            font_size=sp(14), size_hint=(1, None), height=dp(30)
        )
        layout3.add_widget(calc_label)
        
        self.display_calc_div = TextInput(
            text='',
            font_size=sp(20), halign='right',
            size_hint=(1, None), height=dp(50), readonly=True
        )
        layout3.add_widget(self.display_calc_div)
        
        botones_division = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '←'],
            ['1', '2', '3', '.'],
            ['0', 'Calcular', '=']
        ]
        
        for fila in botones_division:
            h = BoxLayout(spacing=dp(4))
            for btn_text in fila:
                if btn_text == 'Calcular':
                    btn = Button(text=btn_text, font_size=sp(14), size_hint=(2, 1))
                else:
                    btn = Button(text=btn_text, font_size=sp(18))
                btn.bind(on_press=lambda x, t=btn_text: self.click_calc_div(t))
                h.add_widget(btn)
            calc_div_layout = h
            layout3.add_widget(calc_div_layout)
        
        tab3.add_widget(layout3)
        panel.add_widget(tab3)
        
        self.ultimo_resultado = 0
        self.nuevo_problema(None)
        
        return panel
    
    # ========== CALCULADORA BÁSICA ==========
    def click_basica(self, tecla):
        if tecla == 'C':
            self.expresion = ""
            self.display1.text = "0"
        elif tecla == '←':
            self.expresion = self.expresion[:-1]
            self.display1.text = self.expresion if self.expresion else "0"
        elif tecla == '=':
            try:
                resultado = eval(self.expresion.replace('x', '*'))
                self.display1.text = str(resultado)
                self.expresion = str(resultado)
            except:
                self.display1.text = "Error"
                self.expresion = ""
        else:
            if self.expresion == "" and self.display1.text == "0":
                self.expresion = tecla
            else:
                self.expresion += tecla
            self.display1.text = self.expresion
    
    # ========== CALCULADORA CIENTÍFICA ==========
    def click_cientifica(self, tecla):
        try:
            if tecla == 'C':
                self.expresion = ""
                self.display2.text = "0"
            elif tecla == '←':
                self.expresion = self.expresion[:-1]
                self.display2.text = self.expresion if self.expresion else "0"
            elif tecla == '=':
                expr = self.expresion.replace('x', '*').replace('^', '**')
                expr = expr.replace('π', str(math.pi)).replace('e', str(math.e))
                resultado = eval(expr)
                self.ultimo_resultado = resultado
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'sin':
                val = float(eval(self.expresion))
                resultado = math.sin(math.radians(val))
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'cos':
                val = float(eval(self.expresion))
                resultado = math.cos(math.radians(val))
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'tan':
                val = float(eval(self.expresion))
                resultado = math.tan(math.radians(val))
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'ln':
                val = float(eval(self.expresion))
                resultado = math.log(val)
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'log':
                val = float(eval(self.expresion))
                resultado = math.log10(val)
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == '√':
                val = float(eval(self.expresion))
                resultado = math.sqrt(val)
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'x²':
                val = float(eval(self.expresion))
                resultado = val ** 2
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'x!':
                val = int(float(eval(self.expresion)))
                resultado = math.factorial(val)
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == '1/x':
                val = float(eval(self.expresion))
                resultado = 1 / val
                self.display2.text = str(resultado)
                self.expresion = str(resultado)
            elif tecla == 'π':
                self.expresion += str(math.pi)
                self.display2.text = self.expresion
            elif tecla == 'e':
                self.expresion += str(math.e)
                self.display2.text = self.expresion
            elif tecla == 'ANS':
                self.expresion += str(self.ultimo_resultado)
                self.display2.text = self.expresion
            elif tecla == '^':
                self.expresion += '**'
                self.display2.text = self.expresion
            else:
                if self.expresion == "" and self.display2.text == "0":
                    self.expresion = tecla
                else:
                    self.expresion += tecla
                self.display2.text = self.expresion
        except:
            self.display2.text = "Error"
            self.expresion = ""
    
    # ========== JUEGO DE DIVISIONES ==========
    def nuevo_problema(self, instance):
        divisor = random.randint(2, 12)
        cociente = random.randint(1, 20)
        dividendo = divisor * cociente
        self.respuesta_correcta = cociente
        
        self.label_problema.text = f'{dividendo} ÷ {divisor} = ?'
        self.display3.text = ''
        self.label_mensaje.text = '¡Escribe tu respuesta!'
        self.label_mensaje.color = (1, 1, 1, 1)
    
    def verificar(self, instance):
        if not self.display3.text:
            self.label_mensaje.text = '⚠️ Escribe una respuesta'
            return
        
        respuesta = int(self.display3.text)
        self.intentos += 1
        
        if respuesta == self.respuesta_correcta:
            self.puntuacion += 1
            self.label_mensaje.text = random.choice([
                '🎉 ¡Excelente!',
                '⭐ ¡Correcto!',
                '🏆 ¡Muy bien!',
                '💯 ¡Perfecto!'
            ])
            self.label_mensaje.color = (0, 1, 0, 1)
        else:
            self.label_mensaje.text = f'❌ Incorrecto. Era {self.respuesta_correcta}'
            self.label_mensaje.color = (1, 0, 0, 1)
        
        self.label_puntuacion.text = f'Puntos: {self.puntuacion}/{self.intentos}'
    
    def reiniciar(self, instance):
        self.puntuacion = 0
        self.intentos = 0
        self.label_puntuacion.text = 'Puntos: 0/0'
        self.nuevo_problema(None)
    
    # ========== MINI CALCULADORA DE DIVISIONES ==========
    def click_calc_div(self, tecla):
        if tecla == 'Calcular' or tecla == '=':
            try:
                if '/' in self.expresion_calc_div:
                    resultado = eval(self.expresion_calc_div)
                    self.display_calc_div.text = f"{self.expresion_calc_div} = {resultado}"
                    self.expresion_calc_div = ""
                else:
                    self.display_calc_div.text = "Usa el símbolo /"
            except:
                self.display_calc_div.text = "Error"
                self.expresion_calc_div = ""
        elif tecla == '←':
            self.expresion_calc_div = self.expresion_calc_div[:-1]
            self.display_calc_div.text = self.expresion_calc_div
        else:
            self.expresion_calc_div += tecla
            self.display_calc_div.text = self.expresion_calc_div


if __name__ == '__main__':
    CalculadoraApp().run()