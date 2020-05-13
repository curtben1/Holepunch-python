import socket
import struct
import sys

master = ()     #add tuple of my pc address + a forwarded port
me=()           # my ip and a random port as tuple, 3:37 in vid


try:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockfd.bind(("",0))
    sockfd.sendto("Hello", master)

except socket.error:
    print("Failed to create  socket")
    sys.exit

peer_data, addr = sockfd.recvfrom(1024)
print(peer_data)

print("trying to com with peer")
peer_ip = peer_data.split(':')[0]
peer_port = int(peer_data.split(':')[1])

sockfd.sendto("hello from your peer", (peer_ip, peer_port))

while True:
    datarec,sendaddr = sockfd.recvfrom(1024)
    print("data rec")
    