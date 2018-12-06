import socket
import sys  # for exit
import time
import os

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
    print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
# print ('Socket created')

host = 'localhost'
port = 8234

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print ('Hostname could not be resolved. Exiting ...')
    sys.exit()

s.connect((remote_ip , port))
num = s.recv(1024).decode('ASCII') # receives the number of texts from the server
intro = s.recv(1024)               # receives the intro message from the server
intro = intro.decode('ASCII')
print(intro)                       # prints the intro message
print("\n")
available_texts = []
for _ in range(int(num)):          # receives the texts that are in the server and prints it out for the client to see
    text = s.recv(1024)
    text = text.decode('ASCII')
    available_texts.append(text)
    print(text)

print("\n")

filename = str(input('Which file would you like to download?: '))   # asks the usesr what file they want to download
while not filename or filename not in available_texts:
    filename = str(input('Please enter a file name from the available list: '))  # if the file entered was not one of the files received from the server the user is asked to enter a new one

s.sendall(filename.encode('ASCII'))                 # sends the file chosen to the server
num_lines = s.recv(1024).decode('ASCII')            # receives the number of lines in the chosen file
num_lines = int(num_lines)                          # to calculate the percentage of the file that has been transfered
filename = filename.split('.')
file = open(filename[0]+"-copy.txt",'w')            # creates a new file to copy the file in the server
s.sendall("Y".encode('ASCII'))

load_bar = "["                                      # initiates the load bar
#for i in range(int(num_lines)):
    #load_bar += " "

z = 0
while True:
    reply = s.recv(1024)                                     # receives a line from the file that is being transferred
    reply = reply.decode('ASCII')                            # decodes the line
    if reply != 'fin':                                       # keeps writing to the file if the last line has not been received
        file.write(reply)                                    
        s.sendall("Y".encode('ASCII'))                       # sends a Y to the server to acknowledge the received line
        os.system('cls' if os.name == 'nt' else 'clear')     
        load_bar += "#"                                      # adds to the loadbar
        perc = (z/num_lines)*100                             # calculates the percentage of the file received
        print(load_bar,str(perc)+"%")
        time.sleep(0.2)
        z += 1
    elif reply == 'fin':
        os.system('cls' if os.name == 'nt' else 'clear')     # clears the console to show the animation for the load bar
        load_bar += "]"
        perc = (z/num_lines)*100
        print(load_bar,str(perc)+"%")                        # prints the percentage  
        print("File download complete")
        break
    else:
        s.sendall("N".encode('ASCII'))                       # sends an N to the server to tell the server that the line was not received
        print("didnt get it")
file.close()                                                 # closes the file 
s.close()                                                    # closes the connection
