#TCP Server
#Obaida Kamil

import socket
import time
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

#currentdate function returns the current date and time as a string
def currentdate():
    currentDT = datetime.now()
    return "Current Date and Time - " + currentDT.strftime("%m/%d/%Y %H:%M:%S")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#connections search
while(1):
    (conn, addr) = s.accept()

    #checking if the response is valid or not for the correct time to be sent. If not we send an error message 
    while(1):
        rsp = conn.recv(50).decode('UTF-8')
        if (rsp == "What is the current date and time?"):
            message = currentdate()
        else:
            message = "Not a valid request"
        conn.send(message.encode())
        break

s.close()
