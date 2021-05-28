import socket
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
 
while True:
    clt,adr=s.accept()
    print(f"Connection to {adr}established")
    data = clt.recv(1024)
    print('Client :' + data.decode())
    currentTime = time.ctime(time.time())
    clt.send(currentTime.encode())
    clt.close()
