import socket
import decrypt

sock = socket.socket()
host = "127.0.0.1"
port = 5555

sock.connect((host,port))   #connecting to sender
print("Successfully connected to sender!")

while True:
    data = sock.recv(1024).decode("utf-8")
    print("Received text is: " + data)
    print("Decrypted text is: " + decrypt.decrypt(data))
