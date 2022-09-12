# -*- coding: utf-8 -*-
#---
def centroMassa(size):
    return (round(size[0]/2),round(size[1]/2))


def conexaoCLP(ip=''):
    try:
        print('Buscando conexao: ',ip)
        from pyModbusTCP.client import ModbusClient
        c = ModbusClient(host=ip, auto_open=True, auto_close=True)
        if c.open():
            return c
        return False
    except Exception as e:
        return e
    
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