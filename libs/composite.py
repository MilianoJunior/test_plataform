# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:38:09 2022

@author: jrmfi
"""

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.card import MDCard
import random
# meus modulos
from libs.interfaces.interface_conexao import InterfaceConexao


class Composite(ScreenManager):
    '''
    description: composição dos layouts em uma classe central
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        try:
            self.add_widget(InterfaceConexao(name='conexao')())
            return self
        except Exception as e:
            print(e)
            # raise InterfaceException(e)()

    def slide(self, *args):
        self.current = random.choice(self.screen_names)