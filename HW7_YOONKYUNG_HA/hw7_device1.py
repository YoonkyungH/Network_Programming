from socket import *
import sys
import random

BUF_SIZE = 1024
LENGTH = 50

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))
print('connect device1')

while True:
    msg = s.recv(BUF_SIZE)
    if not msg:
        s.close()
        sys.exit()
    elif msg == b'quit':
        print('quit')
        s.close()
        sys.exit()
    else:
        print('server: ', msg.decode())

    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    illum = random.randint(70, 150)

    s.send(b'%d %d %d' % (temp, humid, illum))
 
s.close()