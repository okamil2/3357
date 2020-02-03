#TCP Client
#Obaida Kamil

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#the information we are getting from the user will be sent to the server in ascii
print ("Connection to Server Established")
message = input("Please enter in the command you would like the server to respond to: ")
s.sendall(message.encode())

#we only continue when the response of the command is recieved and that's what we are using the while loop for below
rsp = ""
while (1):
	rsp = s.recv(50).decode()
	if (rsp != ""):
        	break

print(rsp)
s.close()
