import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = "Client Requests Server's local time"
s.send(msg.encode())
tm = s.recv(1024)                                     
s.close()
print("The time got from the server is %s" % tm.decode())
