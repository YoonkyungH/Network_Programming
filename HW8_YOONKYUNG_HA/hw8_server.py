from socket import *

BUFF_SIZE = 1024000
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
dic = {}

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)

    msg = data.decode()
    temp = msg.split()
    message = temp[2:]
    message = " ".join(message)

    print(msg)
    if temp[0] == 'send':
        if temp[1] not in dic:
            dic[temp[1]] = [message]
        else:
            dic[temp[1]].append(message)

        sock.sendto(b'ok', addr)
        print(dic)
    elif temp[0] == 'receive':
        if temp[1] not in dic:
            sock.sendto(b"No messages", addr)
        else:
            sock.sendto(dic[temp[1]][0].encode(), addr)
            
            if len(dic[temp[1]])==1:
                del dic[temp[1]]
            elif len(dic[temp[1]])>1:
                del dic[temp[1]][0]
            else:
                sock.sendto(b"No messages", addr)

            print(dic)  # 확인용
    elif msg == 'quit':
        break

sock.close()