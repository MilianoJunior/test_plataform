# Projeto de Conclusão de Curso Engenharia Elétrica - Estudo de Caso - Usina Hidrelétrica PCH JASP
# Estudo de Proteção - Geradores, Transformadores, Usina, Subestação, Linha de Transmissão
# Gabriel Vinícius Gasparetto

from kivymd.uix.card import  MDCard
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, IconLeftWidget, MDList
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.label import MDLabel
from numpy import spacing
from pyautogui import position
from kivymd.uix.card import MDSeparator
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.checkbox import CheckBox
from random import uniform
from functools import partial

class EstudoProtecao(MDScreen):

    defaut = {
                'CELESC 13,8 kV':{'Sb': 100e6,'Vb':13.8e3}, 
                'CELESC 23,1 kV':{'Sb': 100e6,'Vb':21.1e3}, 
                'COPEL':{'Sb': 100e6,'Vb':34.5e3}, 
                'CPFL':{'Sb': 100e6,'Vb':23.1e3}, 
                'ENERGISA':{'Sb': 100e6,'Vb':34.5e3}, 
                'RGE 13,8 kV':{'Sb': 100e6,'Vb':13.8e3}, 
                'RGE 23,1 kV':{'Sb': 100e6,'Vb':23.1e3},
    }

    configuracoes = {
                        1: {'concessionaria':None, 'Value': None},
                        2: {'circuito':None, 'Value': None},

    }

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        # layout menu
        layout_principal = MDBoxLayout(md_bg_color="#C3C3C3", 
                             orientation='vertical',
                             padding=[10,10,10,10],
                             spacing = 10,
                             size_hint=[1,1],
                             adaptive_height= True)
        button = MDRaisedButton(text='Calcular',
                                md_bg_color="0F2983",
                                pos_hint= {'center_x': .5, 'center_y': .0})
        layout_principal.add_widget(button)
        scroll = MDScrollView()
        # Lógica principal

        # Criação do layout
        title = 'Escolha a Concessionária de Energia'
        options = ['CELESC 13,8 kV','CELESC 23,1 kV', 'COPEL', 'CPFL', 'ENERGISA', 'RGE 13,8 kV', 'RGE 23,1 kV']
        size = ['400dp','400dp']
        position = (0.5,0.1)
        choice_concessionaria  = self.gerar_menu(title, options, size, position,1)

        title = 'Escolha a Configuração do Circuito'
        options = ['1TE + 1UG', '1TE + 2UG', '2TE + 2UG', '1TE + 4 UG', '2TE + 4UG']
        size = ['400dp','360dp']
        position = (0.5,0.1)
        choice_circuito  = self.gerar_menu(title, options, size, position,2)

        # self.on_checkbox_active = choice_circuito.on_checkbox_active
        button.fbind('on_press',self.logica_a,choice_concessionaria.children[0])

        # add layout principal
        layout_principal.add_widget(choice_concessionaria)
        layout_principal.add_widget(choice_circuito)
        self.add_widget(layout_principal)
        return self
    

    def logica_a(self,*args):
        print(self.configuracoes)


    def gerar_menu(self, title, options, size, pos, group):
        menu = MDCard(
                    orientation='vertical',
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    padding=[10,10,10,10],
                    spacing=10,
                    size_hint=(None, None),
                    size = (size[0],size[1]),
                    focus_behavior=True,
                    pos_hint={"center_x": pos[0], "center_y": pos[1]},
                    md_bg_color="#FFFFFF",
                    unfocus_color="#FFFFFF",
                    focus_color="#92CCDE",
                )
        titulo =  MDLabel(
                    text=title,
                    halign="center",
                    theme_text_color='Custom',
                    font_style='H6',
                    text_color= "#333333",
                )
        menu.add_widget(titulo)
        lista_obj = MDList(height=10)
        for option in options:
            print(option)
            r, g, b = [uniform(0.2, 1.0) for j in range(3)]
            checkbox = CheckBox(size_hint= (None, None),
                                size= ("40dp", "40dp"),
                                pos_hint= {'center_x': .9, 'center_y': .5},
                                color=(r, g, b,1),
                                group=group)
            checkbox.bind(active=partial(self.on_checkbox_active, option))
            lista = OneLineListItem(text=option)
            lista.add_widget(checkbox)
            lista_obj.add_widget(lista)
        menu.add_widget(lista_obj)
        return menu

    def display(self):
        display_menu = MDCard(
                    orientation='vertical',
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    padding=[10,10,10,10],
                    spacing=10,
                    size_hint=(None, None),
                    size = (100,200),
                    focus_behavior=True,
                    pos_hint={"center_x": .5, "center_y": .5},
                    md_bg_color="#FFFFFF",
                    unfocus_color="#FFFFFF",
                    focus_color="#92CCDE",
                    shadow_softness= 8,
                )
        return display_menu
    def on_checkbox_active(self,*args):
        self.configuracoes[args[1].group][1] = args[0]
        print(args[1].group)
        print(args)


    