import socket
from threading import Thread

def thread():
        while True:
                data = conn.recv(1024)
                print('Client Request :' + data.decode())
                if data.decode() == 'quit' or not data:
                        print("Client Exiting")
                        answer = input('Do you want to continue?:')
                        if answer.lower().startswith("y"):
                                print("ok, carry on then")
                                
                        elif answer.lower().startswith("n"):
                                print("ok, sayonnara")
                                conn.close()
                                exit()
                data = input('Server Response:')
                if data == 'Shutdown' or not data:
                        conn.sendall(data.encode())
                        print("Server Exiting")
                        conn.close()
                        exit()
                conn.sendall(data.encode())  

host = socket.gethostname()
port = 3333
s = socket.socket()		
s.bind((host,port))
s.listen(5)

print("Waiting for clients...")
while True:
	conn,addr = s.accept()	        
	print("Connected by ", addr)
	pr = Thread(target=thread)
	pr.start()

conn.close()
