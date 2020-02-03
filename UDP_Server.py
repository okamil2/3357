#Obaida Kamil
#250982002
import binascii
import socket
import struct
import sys
import hashlib
import random
import time


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
unpacker = struct.Struct('I I 8s 32s')



def Network_Delay():
    if False and random.choice([0,1,0]) == 1: # Set to False to disable Network Delay. Default is 33% packets are delayed
       time.sleep(.01)
       print("Packet Delayed")
    else:
        print("Packet Sent")

def Network_Loss():
    if False and random.choice([0,1,1,0]) == 1: # Set to False to disable Network Loss. Default is 50% packets are lost
        print("Packet Lost")
        return(1)
    else:
        return(0)

def Packet_Checksum_Corrupter(packetdata):
     if False and random.choice([0,1,0,1]) == 1: #  # Set to False to disable Packet Corruption. Default is 50% packets are corrupt
        return(b'Corrupt!')
     else:
        return(packetdata)



#Create the socket and listen
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:

    #Receive Data
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    UDP_Packet = unpacker.unpack(data)
    print("received from:", addr)
    print("received message:", UDP_Packet)

    #checking to see if no network loss happened then we go ahead and create the checksum for comparison
    if Network_Loss() == 0:
        #Create the Checksum for comparison
        values = (UDP_Packet[0],UDP_Packet[1], Packet_Checksum_Corrupter(UDP_Packet[2]))
        packer = struct.Struct('I I 8s')
        packed_data = packer.pack(*values)
        chksum =  bytes(hashlib.md5(packed_data).hexdigest(), encoding="UTF-8")

        #Compare Checksums to test for corrupt data
        if UDP_Packet[3] == chksum:
            print('CheckSums Match, Packet OK')
            valuePack=(1, UDP_Packet[1],UDP_Packet[2], UDP_Packet[3])

        else:
            print('Checksums Do Not Match, Packet Corrupt')
            valuePack=(1, UDP_Packet[1], b'', chksum)
        dataPacked = unpacker.pack(*valuePack)
        sock.sendto(dataPacked, addr)
        Network_Delay()
