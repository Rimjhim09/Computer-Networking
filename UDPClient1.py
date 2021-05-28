import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=int(4444)
print("Sending to: ", socket.gethostname())
print("Port used: ",port)
while True:
    msg = input("client:")
    s.sendto(msg.encode(), (socket.gethostname(), port))
    print("Message sent...")
    msgFromServ = s.recvfrom(1024)
    msg = "Server: {}".format(msgFromServ[0].decode())
    print(msg)
