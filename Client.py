from socket import *
from threading import Thread
import sys

HOST = 'localhost'
PORT = 5100
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
data = raw_input('Please Enter Your User Name : ')
Sock.send(data)
data = raw_input('Enter The Name of user you want to Talk : ')
Sock.send(data)
while True:
    data = raw_input('Me: ')
    Sock.send(data)

Sock.close()
