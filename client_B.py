import socket
import struct
import sys

master = ("81.151.18.101",7070)     #add tuple of my pc address + a forwarded port
me=("192.168.1.162",52527)           # my ip and a random port as tuple, 3:37 in vid


try:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockfd.bind(("",0))
    msg="Hello".encode("ascii")
    sockfd.sendto("Hello".encode("ascii"), master)

except socket.error:
    print("Failed to create  socket")
    sys.exit

peer_data, addr = sockfd.recvfrom(1024)
print(peer_data.decode("ascii"))

print("trying to com with peer")
peer_data=peer_data.decode("ascii")
peer_ip = peer_data.split(':')[0]
peer_port = int(peer_data.split(':')[1])
print(peer_ip,peer_port)
sockfd.sendto("hello from your peer".encode("ascii"), (peer_ip, peer_port))

while True:
    print("listening")

    datarec,sendaddr = sockfd.recvfrom(1024)
    datarec.decode("ascii")
    print("data rec",datarec)
    