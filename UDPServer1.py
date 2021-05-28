import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=4444
s.bind((socket.gethostname(), port))
print("Name: ",socket.gethostname())
#print("IP: ", socket.gethostbyname(socket.gethostname()))
print('starting up on %s, port: %s' %(socket.gethostname(),port))
while True:
    data, addr = s.recvfrom(1024)
    print ("Message: ", data.decode())
    s.sendto((data.decode()).encode(), addr)
    print("Message echoed...")
    
