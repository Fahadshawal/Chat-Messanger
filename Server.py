'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5160# Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
	#loop = len(arr)
	#conn.send(str(loop)) #send only takes string 
	
    #infinite loop so that function do not terminate and thread do not end.
	while 1:
         
        #Receiving from client
		data = conn.recv(1024)
		if conn == arr[0]['con']:
			conn = arr[1]['con']
			conn.send(data)
			conn = arr[0]['con']
		elif conn == arr[1]['con']:
			conn = arr[0]['con']
			conn.send(data)
			conn = arr[1]['con']
    #came out of loop
	conn.close()

#-------------------------------------------------------
#This Function will show the list of all connected users
def ShowAllUser(conn):
	conn.send("\n---------------Connected User With The Serve Are---------------\n")
	loop = len(arr)
	while loop:
		loop -= 1
		conn.send(arr[loop]['nam']+"\n")
	conn.send("---------------------------------------------------------------\n")
	return
	
#------------------------------------------------------
#This Function WIll Show to All User About New Connection
def ShowToAll(temp):
	loop = len(arr)
	while loop:
		loop -= 1
		arr[loop]['con'].send("--------------------------------------")
		arr[loop]['con'].send("\n" + temp['nam'] + " is Now Connected\n")
		arr[loop]['con'].send("--------------------------------------")
	return

arr =[] # this is to keep track of users
i = 0
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    temp = {}
    temp['con'] = conn
    temp['adr'] = addr
    temp['nam'] = conn.recv(200)
    ShowToAll(temp)
    arr += [temp]
    ShowAllUser(conn)
    #print arr
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    i += 1
 
s.close()
