import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
# 본인의 이름 문자열로 전송
sock.send(b'Yoonkyung Ha')
# 본인의 학번을 수신 후 출력
num = sock.recv(1028)
print(int.from_bytes(num, 'big'))
sock.close()
