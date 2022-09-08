# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:11:21 2022

@author: jrmfi---
"""

tag = [
       {
        'id':'TS_O',
        'local': 26,
        'tipo':'Toglle',
        'size':[63,63],
        'position':[267,500],
        'assert': ['verificar no log do sistema se foi ativado o stop UG-01',
                   '1x-16388 == True'],
      },
       {
        'id':'BL_O',
        'local': 26,
        'tipo':'Bit Lamp',
        'size':[25,25],
        'position':[215,632],
        'assert': (106, 12, 6),
      },
       {
        'id':'BL_O',
        'local': 26,
        'tipo':'Bit Lamp',
        'size':[25,25],
        'position':[215,661],
        'assert': (106, 12, 6),
      },
       {
        'id':'BL_O',
        'local': 26,
        'tipo':'Bit Lamp',
        'size':[25,25],
        'position':[215,790],
        'assert': (15, 78, 25),
      },
       {
        'mult': 4,
        'id':'BL_O',
        'local': 26,
        'tipo':'Bit Lamp',
        'size':[25,25],
        'position':[215,790],
        'assert': (15, 78, 25),
      },
       
       
       ]
