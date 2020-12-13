import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "192.168.0.4"
port = 6000             # Reserve a port for your service.

s.connect((host, port))
print ("... Connected!\n")

filename = input(str("Masukkan nama fail : "))
file = open(filename,'rb')
data = file.read(1024)
s.send(data)

print("{Penghantaran selesai")
file.close()
s.close()
print("Connection ditutup")
