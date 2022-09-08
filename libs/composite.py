# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:38:09 2022

@author: jrmfi
"""

from kivy.uix.screenmanager import ScreenManager
import random
# meus modulos
# from controllers.excpetions.RootException import InterfaceException
from libs.interfaces.interface_conexao import InterfaceConexao
# from view.layouts.interface import Interface
# from view.layouts.login import Login
# from view.layouts.config import Config
# from view.layouts.create_user import CreateUser
# from view.layouts.error import Error
# from view.layouts.recover import RecoverPassword
# from routes.routes import define_manager


class Composite(ScreenManager):
    '''
    description: composição dos layouts em uma classe central
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        try:
            self.add_widget(InterfaceConexao(name='conexao')())
            # self.add_widget(Interface(name='principal')())
            # self.add_widget(Config(name='config')())
            # self.add_widget(CreateUser(name='createuser')())
            # self.add_widget(Error(name='error')())
            # self.add_widget(RecoverPassword(name='recover')())
            # self.current = 'login'
            # define_manager(self)
            return self
        except Exception as e:
            print(e)
            # raise InterfaceException(e)()

    def slide(self, *args):
        self.current = random.choice(self.screen_names)