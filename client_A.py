"""
For use by gamehost.py, works to holepunch to a device behind NAT

"""


import socket
import struct
import sys
import time
master = ("81.151.18.101",7070)     #home pc with port forwarding so no NAT traversal is necesary

def estCon():
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockfd.bind(("",0))
        msg1="testString".encode("ascii")
        sockfd.sendto(msg1, master)

    except socket.error:
        print("Failed to create  socket")
        sys.exit

    peer_data, addr = sockfd.recvfrom(1024)
    print(peer_data.decode("ascii"))

    peer_data=peer_data.decode("ascii")
    print("Trying to communicate with peer")
    peer_ip = peer_data.split(':')[0]
    peer_port = int(peer_data.split(':')[1])
    print(peer_port)
    msg = "connection established"
    for i in range(100):
        print("sending",i)
        msg=msg.encode("ascii")
        sockfd.sendto(msg, (peer_ip,peer_port))
        time.sleep(0.5)

def recvMsg(socket, message, targetIP):
    master = ("81.151.18.101",7070)     #add tuple of my pc address + a forwarded port
    me=("192.168.1.162",52527)           
    message = targetIP + ':' + message
    message = message.encode("ascii")
    socket.sendall(message)
    while True:
        retValue = socket.recvfrom(1024)
        retValue = retValue.decode("ascii")
        tag = retValue.split(':')[0]
        if tag == "forHost":
            retValue = retValue.split(':')[1]
            return retValue