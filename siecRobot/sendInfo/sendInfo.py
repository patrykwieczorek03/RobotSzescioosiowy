import socket

s=socket.socket()
port=80
ip="192.168.1.151"

s.connect((ip,port))
r="0"
s.send(r.encode())
