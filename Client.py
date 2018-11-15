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
# print ('Ip address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip , port))
# print ('Socket connected to ' + host + ' on ip ' + remote_ip)
num = s.recv(1024).decode('ASCII')
# print(num)
intro = s.recv(1024)
intro = intro.decode('ASCII')
print(intro)
# print("intro")
print("\n")
# while True:
available_texts = []
for _ in range(int(num)):
    text = s.recv(1024)
    text = text.decode('ASCII')
    # if text == "done":
    #     break
    available_texts.append(text)
    print(text)

print("\n")

    # break
# print(text)
# print("here")
# text = text.decode('ASCII')
# # if not text:
# #     break
# print(text)
# print("done")
filename = str(input('Which file would you like to download?: '))
while not filename or filename not in available_texts:
    filename = str(input('Please enter a file name from the available list: '))

s.sendall(filename.encode('ASCII'))
filename = filename.split('.')
file = open(filename[0]+"-copy.txt",'w')
s.sendall("Y".encode('ASCII'))

load_bar = "["
while True:
    reply = s.recv(1024)
    reply = reply.decode('ASCII')
    if reply != 'fin':
        file.write(reply)
        s.sendall("Y".encode('ASCII'))
        os.system('cls' if os.name == 'nt' else 'clear')
        load_bar += "#"
        print(load_bar)
        # print('got new line')
        time.sleep(0.5)
    elif reply == 'fin':
        # print('ok finished')
        os.system('cls' if os.name == 'nt' else 'clear')
        load_bar += "]"
        print(load_bar)
        print("File download complete")
        break
    else:
        s.sendall("N".encode('ASCII'))
        print("didnt get it")
file.close()
s.close()
