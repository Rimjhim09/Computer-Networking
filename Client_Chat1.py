import socket
s = socket.socket()
host = socket.gethostname()
port = 3333
s.connect((host,port))
s.send(bytes('Client 1 entered the chat','utf-8'))
while True:
    data = s.recv(1024)
    if data.decode() =='quit' or data.decode() =='Shutdown' or not data:
        print("Quiting")
        break
    else:
        print("Server: ",data.decode())
        msg = input("Client: ")
        s.send(msg.encode())
        if msg =='quit' or not data:
            print("Quiting")
            break
s.close()
