#UDP Server
#Obaida Kamil

import socket
import time
from datetime import datetime, date, time
 
localIP = "127.0.0.1"
localPort = 5005
buffer  = 50

#currentdate function returns the current date and time as a string
def currentdate():
    currentDT = datetime.now()
    return "Current Date and Time - " + currentDT.strftime("%m/%d/%Y %H:%M:%S")


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

 
#Collecting incoming data
while(1):
    bytesAddressPair = UDPServerSocket.recvfrom(buffer)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    #checking if the response is valid or not for the correct time to be sent. If not we send an error message 
    if (message.decode() == "What is the current date and time?"):
        ToSend = str.encode(currentdate())

    else:
        ToSend = str.encode("Invalid Request")

    UDPServerSocket.sendto(ToSend, address)
