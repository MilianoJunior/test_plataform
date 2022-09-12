# -*- coding: utf-8 -*-
#---
c = None

def centroMassa(size):
    return (round(size[0]/2),round(size[1]/2))

def openCLP(ip,q):
    from pyModbusTCP.client import ModbusClient
    print('Execuntado processo',ip)
    c = ModbusClient(host=ip, auto_open=True, auto_close=True)
    if c.open():
        print('Conexao completada')
        q.put(c)

def conexaoCLP(ip=''):
    print('Criando conexao')
    from pyModbusTCP.client import ModbusClient
    c = ModbusClient(host=ip, auto_open=False, auto_close=False)
    if c.open():
        print('Conexao realizada com sucesso!!')
        regs_list_1 = c.read_holding_registers(0, 10)
        regs_list_2 = c.read_holding_registers(55, 10)
        lerCLP(c, 10)
        # print(regs_list_1)
        # print(regs_list_2)
        c.close()
        return c
    return False
        
def lerCLP(obj, registro):
    import time
    # obj.debug = True
    for s in range(0,65535):
        k = obj.read_holding_registers(s, 10)
        time.sleep(.01)
        print(f'registro:{s} value: {k}')
    
def escreverCLP(obj, registro,value):
    if obj.open():
        obj.write_multiple_registers(registro, value)

    
def rastrearIP(HOST):
    import socket

    # HOST ='192.168.10' # Standard loopback interface address (localhost)
    # PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    for host_ in [f'{HOST}.{str(i)}' for i in range(1,255)]:
        print(host_)
        for port in range(1,65000):
            print(host_,':',port)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((str(host_).strip(), str(port).strip()))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    # while True:
                    #     data = conn.recv(1024)
                    #     if not data:
                    #         break
                    #     conn.sendall(data)