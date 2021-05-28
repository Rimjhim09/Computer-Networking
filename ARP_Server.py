import socket
import getmac
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
h=socket.gethostbyname(host)
h=str(h)
print(h," : ",host)
port=1888
s.bind((host,port))
while True:
    print("Waiting for client...")
    conn,addr=s.recvfrom(1024)
    conn=conn.decode()
    data=str(conn)
    if(h==data):
        print("Request :",data)
        print(getmac.get_mac_address())
        msg4Cl=getmac.get_mac_address()
        s.sendto(msg4Cl.encode(), addr)
    elif (h!=data):
        print("Invalid IP")
    break
