# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:28:58 2022

@author: jrmfi
"""

from kivymd.app import MDApp
from kivymd.uix.controllers import WindowController
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from libs.funcoes import conexaoCLP, rastrearIP
import trio

from kivy.app import async_runTouchApp
from functools import partial

   
    
    
class InterfaceConexao(MDScreen):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        
    def __call__(self):
        # layout 
        layout = MDBoxLayout(md_bg_color="#C3C3C3", orientation='horizontal')
        # componentes
        input_ip = MDTextField(hint_text='ip_conexao')
        button = MDRaisedButton(text='conectar',theme_text_color= "Custom",text_color= "orange")
        # metodos
        button.fbind('on_press',self.conectar,input_ip)
        # composicao
        layout.add_widget(button)
        layout.add_widget(input_ip)
        self.add_widget(layout)
        # retorno
        return self
    def conectar(self,*args):
        print(args[0].text)
        rastrearIP('192.168.0')
        # async_runTouchApp_func = partial(async_runTouchApp, async_lib='trio')
        # obj = trio.run(async_runTouchApp_func, conexaoCLP(args[0].text))
        # if obj:
        #     print('conexao realizada com sucesso')

