
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 5188               # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
while True:
	
	data = raw_input()
	s.send(data)
	print s.recv(1024)

s.close                     # Close the socket when done
