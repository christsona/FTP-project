import socket
import sys

def client(conn):
    filename = str(input('What file would you like to use?:'))
    file = open(filename,'r')
    conn.sendall(filename.encode('ASCII'))
    print("sent filename")
    while True:
        reply = conn.recv(1024)
        reply = reply.decode('ASCII')
        while reply == 'N':
            conn.sendall(line)
            print("sending again")
        read = file.readline()
        if not read:
            conn.sendall("fin".encode('ASCII'))
            print("finished sending file")
            break
        line = read.encode('ASCII','ignore')
        conn.sendall(line)
        print("sent new line")

    file.close()
    conn.close()

HOST, PORT = '', 8234

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
# print ('serving HTTP on port ', PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    # print ('server connected to ' + client_address[0] + ':' + str(client_address[1]))
    client(client_connection)
    break
listen_socket.close()
