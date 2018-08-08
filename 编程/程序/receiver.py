import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',5002))
while True:
    date,addr = s.recvfrom(1024)
    print('received message:{0} from PORT {1} on {2}'.format(date.decode(),addr[1],addr[0]))
    if date.decode().lower() == 'bye':
        break
s.close()