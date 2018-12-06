import socket
import sys
import time

def client(conn):
    texts = ["Asyoulikeit.txt","HenryV.txt","JuliusCaesar.txt","Macbeth.txt","Othello.txt"]    # the available texts for transfer
    num_texts = str(len(texts))                                             
    conn.sendall(num_texts.encode('ASCII'))                                                  # sends the number of texts to the client
    time.sleep(0.01)
    conn.sendall("Welcome to the Server. Here are the files that are available for download.".encode('ASCII'))  # sends the intro message
    time.sleep(0.01)
    for text in texts:                                            # sends the available texts to the client 
        time.sleep(0.01)
        conn.sendall(text.encode('ASCII'))

    filename = conn.recv(1024)                                    # receives the chosen filename
    filename = filename.decode('ASCII')
    while not filename:
        filename = conn.recv(1024).decode('ASCII')
    num_lines = sum(1 for line in open(filename))                 # counts the lines in the chosen file
    num_lines = str(num_lines)                   
    conn.sendall(num_lines.encode('ASCII'))                       # sends the number of lines to the client
    file = open(filename,'r')                                     # opens the file for reading
    while True:
        reply = conn.recv(1024)                                   # receives the Y or N from the client
        reply = reply.decode('ASCII')
        while reply == 'N':                                       # if an N is received then the line is sent again 
            conn.sendall(line)
            print("sending again")
        read = file.readline()                                    # if a Y is received then a new line is read 
        if not read:
            conn.sendall("fin".encode('ASCII'))                   # if there is no new line, then the download is complete and the code breaks
            print("Download Complete")
            break
        line = read.encode('ASCII','ignore')  
        conn.sendall(line)                                        # the line is sent to the client
        time.sleep(0.2)

    file.close()                                                  # the file is closed 
    conn.close()                                                  # the connection is closed

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
