#!/usr/bin/python
import socket
HOST = '127.0.0.1'
PORT = 11102
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Sucesso'))
data = s.recv(1024)

print('Mensagem enviada: ', data.decode())
