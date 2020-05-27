import socket
import struct
import sys
import time
master = ("86.137.149.100",7070)     #add tuple of my pc address + a forwarded port


try:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockfd.bind(("",0))
    msg1="Hello".encode("ascii")
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
for i in range(100):
    print("sending",i)
    msg="Hello from peer client A".encode("ascii")
    sockfd.sendto(msg, (peer_ip,peer_port))
    time.sleep(0.5)
    
