import socket

# port = int(input("Port No: "))
address = ("localhost", 5000)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Input computation: ")
    if msg == 'q':  # q입력시 프로그램 종료
        break
    else:
        try:
            bytesSent = s.send(msg.encode())    # 입력받은 수식을 서버로 전송
        except:
            print('connection closed')
            break
        # else:
        #     print("{} bytes send".format(bytesSent))

        try:
            data = s.recv(BUFSIZE)
        except:
            print('connection closed')
            break
        else:
            if not data:
                break
            ans = data.decode()
            ans = '{:.1f}'.format(float(ans))
            print(ans)
    

s.close()