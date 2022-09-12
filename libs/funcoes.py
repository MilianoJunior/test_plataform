# -*- coding: utf-8 -*-
#---
def centroMassa(size):
    return (round(size[0]/2),round(size[1]/2))


def conexaoCLP(ip=''):
    try:
        from pyModbusTCP.client import ModbusClient
        c = ModbusClient(host=ip, auto_open=True, auto_close=True)
        if c.open():
            return c
        return False
    except Exception as e:
        return e
    