from socket import *
import sys
import random

BUF_SIZE = 1024
LENGTH = 50

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7778))
print('connect device2')

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

    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)

    s.send(b'%d %d %d' % (heartbeat, steps, cal))
 
s.close()