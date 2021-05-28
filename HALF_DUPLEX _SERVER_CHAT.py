import socket
port=int(1234)
print("Starting Half Duplex Chat Program(Server side)")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),port))
s.listen(5)
clt,adr=s.accept()
print(f"Connection to {adr}established")

print("Enter <quit> for for kicking out the client\nEnter <Shutdown> to close the connection and stop the program")
while True:
    
    
    data = clt.recv(1024)
    print('Client :' + data.decode())
    if data.decode() == 'quit' or not data:
        print("Client Exiting")
        answer = input('Do you want to continue?:')
        if answer.lower().startswith("y"):
            print("ok, carry on then")
            
        elif answer.lower().startswith("n"):
            print("ok, sayonnara")
            clt.close()
            exit()
    data = input('Server: ')
    if data == 'Shutdown' or not data:
        clt.sendall(data.encode())
        print("Server Exiting")
        clt.close()
        exit()
        clt.sendall(data.encode())
    else:
        clt.sendall(data.encode())
    
#clt.close()
exit()

