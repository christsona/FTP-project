import socket
import sys  # for exit

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

filename = s.recv(1024)
filename = filename.decode('ASCII')
s.sendall("Y".encode('ASCII'))
file = open(filename+"2",'w')
# file.write(filename)
while True:
    reply = s.recv(1024)
    reply = reply.decode('ASCII')
    if reply != 'fin':
        file.write(reply)
        s.sendall("Y".encode('ASCII'))
        print('Got it')
    elif reply == 'fin':
        print('ok finished')
        break
    else:
        s.sendall("N".encode('ASCII'))
        print("didnt get it")
file.close()
s.close()
