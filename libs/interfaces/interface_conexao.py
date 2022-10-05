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
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.card import MDCard
from libs.funcoes import conexaoCLP, rastrearIP, lerCLP, lerTagsCSV
import random
import time

   
    
    
class InterfaceConexao(MDScreen):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.ug01 = None
        self.ug02 = None
        
    def __call__(self):
        # layout menu
        layout_principal = MDBoxLayout(md_bg_color="#C3C3C3", 
                             orientation='vertical',
                             padding=[10,10,10,10],
                             size_hint=[1,1])
        # # layout menu
        layout_menu = MDBoxLayout(md_bg_color="#FFFFFF", 
                                orientation='vertical',
                                padding=[10,30,10,10],
                                adaptive_height= True,
                                size_hint=[1,.2],
                                pos_hint= {"center_x": .5, "center_y": .5})

        layout_body = MDBoxLayout(md_bg_color="#0F2983", 
                                orientation='vertical',
                                padding=[10,30,10,10],
                                size_hint=[1,.5],
                                pos_hint= {"center_x": .5, "center_y": .5})
        # layout_b = MDBoxLayout(md_bg_color="#0303C3", 
        #                      orientation='horizontal',
        #                      padding=[10,10,10,10],
        #                      size_hint=[1,.8])
        # # layout terciario
        # layout_c = MDBoxLayout(md_bg_color="#C0C0C0", 
        #                      orientation='horizontal',
        #                      padding=[10,10,10,10],
        #                      size_hint=[1,.2])
        # layout_d = MDBoxLayout(md_bg_color="#0303C3", 
        #                      orientation='horizontal',
        #                      padding=[10,10,10,10],
        #                      size_hint=[1,.8])
        # # componentes
        # input_ip = MDTextField(hint_text='ip_conexao',
        #                        padding=[10,10,10,10],
        #                        pos_hint= {"center_x": .5, "center_y": .5})
        # button = MDRaisedButton(text='conectar',
        #                         theme_text_color= "Custom",
        #                         text_color= "orange",
        #                         padding=[10,10,10,10],
        #                         pos_hint= {"center_x": .5, "center_y": .5})
        # button_csv = MDRaisedButton(text='ler csv',
        #                         theme_text_color= "Custom",
        #                         text_color= "orange",
        #                         padding=[10,10,10,10],
        #                         pos_hint= {"center_x": .5, "center_y": .5})
        # button_start = MDRaisedButton(text='Escrever',
        #                         theme_text_color= "Custom",
        #                         text_color= "orange",
        #                         padding=[10,10,10,10],
        #                         pos_hint= {"center_x": .5, "center_y": .5})
        
        # metodos
        # button.fbind('on_press',self.conectar,input_ip)
        # button_csv.fbind('on_press', self.lercsv, layout_b)
        # button_start.fbind('on_press', self.startTeste)
        # # composicao
        # layout_c.add_widget(button,0)
        # layout_c.add_widget(input_ip,1)
        # layout_d.add_widget(button_csv,2)
        # layout_d.add_widget(button_start,2)
        # layout_a.add_widget(layout_c)
        # layout_a.add_widget(layout_d)
        # layout_p.add_widget(layout_a)
        layout_principal.add_widget(layout_menu)
        layout_principal.add_widget(layout_body)
        self.add_widget(layout_principal)
        # retorno
        return self
    def conectar(self, *args):
        print(args[0].text)
        self.obj = conexaoCLP(args[0].text)
    
    def lercsv(self, *args):
        print('Ler CSV: ',args)
        df = lerTagsCSV()
        print(df.values)
        print([len(name) for name in df.columns ])
        df['Valor Teste'] = 0
        size_colunas = [40,30,20,20,15,35,40]
        colunas = [(name[0],dp(name[1])) for name in zip(df.columns,size_colunas) ]
        # colunas.append(('Valor de teste',dp(40)))
        self.data_tables = MDDataTable(use_pagination=False,
                                       column_data = colunas,
                                       row_data = df.values,
                                       rows_num = 200)
        args[0].add_widget(self.data_tables)
        
    def startTeste(self,*args):
        enderecos = {
                        'Fase_AB': ['13599',random.randint(0, 380)],
                        'Fase_BC': ['13600',random.randint(0, 380)],
                        'Fase_CA': ['13601',random.randint(0, 380)],
                        'I_INST_A':['13605',random.randint(0, 100)],
                        'I_INST_B':['13606',random.randint(0, 100)],
                        'I_INST_C':['13607',random.randint(0, 100)],
                        'Frequencia':['13616',random.randint(0, 60)],
                        'PosDistribuidor':['13593',random.randint(0, 100)],
                    }
        if self.ug01 is None and self.ug02 is None:
            self.ug01 = conexaoCLP('192.168.10.2')
            self.ug02 = conexaoCLP('192.168.10.3')
            self.ug01.open()
            self.ug02.open()
            print('--------- Teste de leitura e escrita-------------')
            for key, value in enderecos.items():
                print(key,': ','escrito o valor: ',value[1],' mas aparece o valor: ')
                self.ug01.write_single_register(int(value[0])-1, value[1])
                time.sleep(.5)
                self.ug02.write_single_register(int(value[0])-1, value[1])
                time.sleep(.5)
                k = self.ug02.read_input_registers(int(value[0])-1, 10)
                time.sleep(.5)
                print(f'registro:{value[0]} value: {k}')
                print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            self.ug02.close()
            self.ug01.close()
            self.ug02 = None
            self.ug01 = None
            print('------------------------------------------')
        else:
            print('conexao não realizada')
        
    def argsFunction(self, classe):
        for s in dir(classe):
            print(s)
            print(getattr(classe,s))
            print('-----------------')
        

