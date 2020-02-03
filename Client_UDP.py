#UDP Client
#Obaida Kamil

import socket

serverAddressPort = ("127.0.0.1", 5005)
buffer = 50

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Getting the command so that it is sent to the server
command = input("Command to send to server: ")
toSend 	= str.encode(command)
UDPClientSocket.sendto(toSend , serverAddressPort)

#Getting the server's response to be printed
rsp = UDPClientSocket.recvfrom(buffer)
message = "Message from Server: " + rsp[0].decode()
print(message)
