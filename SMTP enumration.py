import socket
from time import sleep
ip='10.0.0.14'
port=25
name=[]
try:
    with open('names.txt','r') as names:
        names=names.readlines()
        for i in names:
            name.append(str.strip(i))
except FileNotFoundError as e:
    print(e,'Please put Valid file')
    exit()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    s.close()
    print('[+]successfully connected')
except socket.error as er:
    print(er)
    exit()
for n in names:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.sendall(f'VRFY {n}'.encode())
    sleep(1)
    result = s.recv(2048).decode()
    s.send(b'QUIT')
    if '252' in result:
        print(f'[+]User exists:{n}')
    else:
        print(f'[-]User doesnt exist:{n}')