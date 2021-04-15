from socket import *

port = 5555
BUFF_SIZE = 1024000

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("Enter the message(\"send mboxid message\" or \"receive\"): ")

    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'quit':
        break

    data, addr = sock.recvfrom(BUFF_SIZE)
    recmsg = data.decode()
    print(recmsg)

sock.close()