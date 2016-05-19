from socket import *
from threading import Thread
import sys

HOST = 'localhost'
PORT = 5189
BUFSIZE = 1024
ADDR = (HOST, PORT)

Sock = socket(AF_INET, SOCK_STREAM)
Sock.connect(ADDR)

def recv():
    while True:
        data = Sock.recv(BUFSIZE)
        if not data: sys.exit(0)
        print data

Thread(target=recv).start()
while True:
    data = raw_input('> ')
    Sock.send(data)

Sock.close()
