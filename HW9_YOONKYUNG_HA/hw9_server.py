from socket import *
import random
import time

port = 5555
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    # 수신
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print("[수신]", data.decode())
            break
        
    # 송신
    msg = input("[송신] ")
    reTx = 0 # 몇번째 보내는건지 체크

    while reTx <= 3:    # 총 4번까지만 보낼 것
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx >= 4:
        print("Timeout")

sock.close()