from socket import *

port = 5000
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print("connected by", remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE)   # client로부터 계산식을 받음
    except:
        break
    else:
        if not data:
            break
        computation = data.decode()
        computation = computation.split()
        if computation[1] == '+':
            ans = int(computation[0]) + int(computation[2])
        elif computation[1] == '-':
            ans = int(computation[0]) - int(computation[2])
        elif computation[1] == '*':
            ans = int(computation[0]) * int(computation[2])
        elif computation[1] == '/':
            ans = int(computation[0]) / int(computation[2])

    try:
        conn.send(str(ans).encode())
    except:
        conn.send(b'ERROR')
        break

conn.close()