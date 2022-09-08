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

   
    
    
class InterfaceConexao(MDScreen):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        
    def __call__(self):
        layout = MDBoxLayout(md_bg_color="#C3C3C3", orientation='horizontal')
        input_ip = MDTextField(hint_text='ip_conexao')
        button = MDRaisedButton(text='conectar',theme_text_color= "Custom",text_color= "orange")
        layout.add_widget(button)
        layout.add_widget(input_ip)
        self.add_widget(layout)
        return self
        
