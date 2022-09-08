# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:41:58 2022

@author: jrmfi
"""

# -*- coding: utf-8 -*-
# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from multiprocessing import Process
from datetime import datetime
from kivymd.app import MDApp
from typing import NoReturn
import os, sys
from libs.funcoes import *
from libs.dados import *
from libs.composite import Composite



# objetivo = {
#                 1: 'Criar uma interface',
#                 2: 'Mostrar todas as tags e as propriedades',
#                 3: 'Verificar se existem duplicidades ou nomes parecidos',
#                 4: 'Alterar os nomes das tags',
#                 5: 'Criar tags',
#                 6: 'Deletar tags',
#                 7: 'Otimizar a utilização das tags, confor-me a necessidade de uso',
#                 8: 'Salvar as alterações de tags para que sejam importadas pelo EasyBuilder',
#                 9: 'oi',
#     }

# comandos gits
# atualizar repositorio online:
    # git add .
    # git commit -m "descricao das alteracoes"
    # git push
    
# atualizar o repositorio local
    # git pull
    
    
MODE = 'development'

module_registration = ['main.py','interface_conexao.py'] # add modules that trigger reloading

def new_process(module: str)-> NoReturn:
    '''function that executes the desired module in the terminal'''
    try:
        commands = {'nt': f"start python {module}",
                    'posix': f"gnome-terminal -- python3 {module}"}
        os.system(commands[os.name])
        exit()
    except Exception as e:
        print(e)

class KvHandler(FileSystemEventHandler):

    def __init__(self, app, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.app = app

    def on_modified(self, event):
        ''' checks if there have been any changes  in the registered module '''
        for module in module_registration:
            if os.path.basename(event.src_path) == module:                
                p = Process(target=new_process,args=('main.py',))
                p.start()
                p.join()
                self.app.stop()
                return

def run(app: object):
    ''' register the observer with the folder to observe - '''
    o = Observer()
    o.schedule(KvHandler(app), os.getcwd(), recursive=True)
    o.start()

class AppReload(MDApp):

    def __init__(self, *args, **kwargs):
        super(AppReload, self).__init__(*args, **kwargs)
        Window.system_size = [360, 731]
        Window.top = 40
        Window.left = 10

    def build(self):
        return Composite()()
        # return MDLabel(text="Hello, World reload 4", halign="center")

    def on_start(self):
        if MODE == 'development':
            run(self)
            
    def on_stop(self):
        print(self)

if __name__ == "__main__":
    ''' Run the application in a terminal, and through the code editor make your changes,
    when you save, they will be changed automatically. It is necessary to register the
    module to be  monitored.
    OBS: I have little programming experience, but I had difficulties when I started my
    applications in kivy, I hadn't found something for automatic reloading (reactive),
    for ".py" files. If there is a better solution, please help me.'''
    app = AppReload()
    app.run()
