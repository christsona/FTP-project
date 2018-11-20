import socket
import sys
import time

def client(conn):
    texts = ["Asyoulikeit.txt","HenryV.txt","JuliusCaesar.txt","Macbeth.txt","Othello.txt"]
    num_texts = str(len(texts))
    conn.sendall(num_texts.encode('ASCII'))
    time.sleep(0.01)
    conn.sendall("Welcome to the Server. Here are the files that are available for download.".encode('ASCII'))
    time.sleep(0.01)
    for text in texts:
        time.sleep(0.01)
        conn.sendall(text.encode('ASCII'))

    filename = conn.recv(1024)
    filename = filename.decode('ASCII')
    while not filename:
        filename = conn.recv(1024).decode('ASCII')

    file = open(filename,'r')
    while True:
        reply = conn.recv(1024)
        reply = reply.decode('ASCII')
        while reply == 'N':
            conn.sendall(line)
            print("sending again")
        read = file.readline()
        if not read:
            conn.sendall("fin".encode('ASCII'))
            print("Download Complete")
            break
        line = read.encode('ASCII','ignore')
        conn.sendall(line)
        time.sleep(0.2)

    file.close()
    conn.close()

HOST, PORT = '', 8234

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

while True:
    client_connection, client_address = listen_socket.accept()
    client(client_connection)
    break
listen_socket.close()
