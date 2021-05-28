import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host=socket.gethostname()
port=1888
message= input("IP address: ")
s.sendto((message.encode("utf-8")),(host,port))
print("IP sent")
msgFromServ = s.recvfrom(1024)
msg = "MAC Address: {}".format(msgFromServ[0].decode())
print(msg)
s.close()
