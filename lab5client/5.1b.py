import socket

s = socket.socket()

port = 8888

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(('192.168.0.4', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()

