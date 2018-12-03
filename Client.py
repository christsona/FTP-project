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
num = s.recv(1024).decode('ASCII')
intro = s.recv(1024)
intro = intro.decode('ASCII')
print(intro)
print("\n")
available_texts = []
for _ in range(int(num)):
    text = s.recv(1024)
    text = text.decode('ASCII')
    available_texts.append(text)
    print(text)

print("\n")

filename = str(input('Which file would you like to download?: '))
while not filename or filename not in available_texts:
    filename = str(input('Please enter a file name from the available list: '))

s.sendall(filename.encode('ASCII'))
num_lines = s.recv(1024).decode('ASCII')
num_lines = int(num_lines)
filename = filename.split('.')
file = open(filename[0]+"-copy.txt",'w')
s.sendall("Y".encode('ASCII'))

load_bar = "["
#for i in range(int(num_lines)):
    #load_bar += " "

z = 0
while True:
    reply = s.recv(1024)
    reply = reply.decode('ASCII')
    if reply != 'fin':
        file.write(reply)
        s.sendall("Y".encode('ASCII'))
        os.system('cls' if os.name == 'nt' else 'clear')
        load_bar += "#"
        perc = (z/num_lines)*100
        print(perc)
        print(load_bar,str(perc)+"%")
        #print(z)
        time.sleep(0.2)
        z += 1
    elif reply == 'fin':
        os.system('cls' if os.name == 'nt' else 'clear')
        load_bar += "]"
        perc = (z/num_lines)*100
        print(load_bar,str(perc)+"%")
        print(z)
        print("File download complete")
        break
    else:
        s.sendall("N".encode('ASCII'))
        print("didnt get it")
file.close()
s.close()
