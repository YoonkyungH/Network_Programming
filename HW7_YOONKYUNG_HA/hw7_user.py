from socket import *
import os
import time

BUF_SIZE = 1024
LENGTH = 50

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
sock2 = socket(AF_INET, SOCK_STREAM)
sock2.bind(('', 7778))
sock2.listen(10)

print('File server is running...')
conn, addr = sock.accept()
conn2, addr2 = sock2.accept()

while True:  
    device = input('Enter a device num: ')

    if device == '1':
        conn.send('Request'.encode())
        msg = conn.recv(BUF_SIZE).decode().split()
        if not msg:
            conn.close()
            continue
        else:
            f = open('data.txt', 'a')
            t = time.asctime()
            msg[0] = int(msg[0])
            msg[1] = int(msg[1])
            msg[2] = int(msg[2])

            print("%s: Device1: Temp=%d, Humid=%d, Illum=%d" % (t, msg[0], msg[1], msg[2]))
            f.write("%s: Device1: Temp=%d, Humid=%d, Illum=%d\n" % (t, msg[0], msg[1], msg[2]))
    elif device == '2':
        conn2.send(b'Request')
        msg2 = conn2.recv(BUF_SIZE).decode().split()
        if not msg:
            conn.close()
            continue
        else:
            f = open('data.txt', 'a')
            t = time.asctime()
            msg2[0] = int(msg2[0])
            msg2[1] = int(msg2[1])
            msg2[2] = int(msg2[2])

            print("%s: Device2: Heartbeat=%d, Steps=%d, Cal=%d" % (t, msg2[0], msg2[1], msg2[2]))
            f.write("%s: Device2: Heartbeat=%d, Steps=%d, Cal=%d\n" % (t, msg2[0], msg2[1], msg2[2]))
    elif device == 'quit':
        print('quit')
        conn.send(b'quit')
        conn2.send(b'quit')
        # conn.close()
        # conn2.close()
        break
    else:
        print('Error')
        conn.close()
        conn2.close()
        continue
    

f.close()
conn.close()