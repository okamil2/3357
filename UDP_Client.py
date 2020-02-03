#Obaida Kamil
#250982002
import binascii
import socket
import struct
import sys
import hashlib

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

UDP = struct.Struct("I I 8s")
UDP_Packet_Data = struct.Struct("I I 8s 32s")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

data={"NCC-1701": 0,"NCC-1422": 1,"NCC-1017": 0}

for i in data:

    #over here we are building the checksum
    value = (0, data[i], str.encode(i))
    tempPack = UDP.pack(*value)
    checksum = bytes(hashlib.md5(tempPack).hexdigest(), encoding="UTF-8")

    #Build packet
    valuePack=(0, data[i], str.encode(i), checksum)
    packToSend = UDP_Packet_Data.pack(*valuePack)
    sock.settimeout(0.009)
    sock.sendto(packToSend, (UDP_IP, UDP_PORT))
    print("packet", i , "was sent")

    #Waiting for the acknowlefgment from the server to be received
    while(1):
        try:
            sock.settimeout(0.009)
            pack = sock.recv(1024)
            packRecv = UDP_Packet_Data.unpack(pack)

            check = (0, packRecv[1], packRecv[2])
            checkPacket = UDP.pack(*check)
            checksum = bytes(hashlib.md5(checkPacket).hexdigest(), encoding = "UTF-8")

            #now we are checking to see if the packet is corrupt or not!
            if(packRecv[0]==1 and packRecv[1]==data[i] and checksum==packRecv[3]):
                print("packet has been received", packToSend, "valid checksum")
                break

        except:
            print("Timeout")
            sock.sendto(packToSend, (UDP_IP, UDP_PORT))

sock.close()
