import threading
from socket import *

k = 1
i = 0


def sen(client_socket):
    global k, i
    while k:
        sentence = input()
        if (sentence == "exit"):
            k = 0
        client_socket.send(sentence.encode())

    i = i+1


def rev(client_socket):
    global k, i
    while k:
        message = client_socket.recv(2048)
        if (message.decode == "exit"):
            k = 0
        print(message.decode())
    i = i+1


def main():
    global i
    server_name = 'localhost'
    server_port = 5000
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    ts = threading.Thread(target=sen, args=(client_socket,))
    tr = threading.Thread(target=rev, args=(client_socket,))
    ts.start()
    tr.start()
    while (1):
        if(i == 2):
            break
    client_socket.close()
    print("connection closed")


if __name__ == '__main__':
    main()
