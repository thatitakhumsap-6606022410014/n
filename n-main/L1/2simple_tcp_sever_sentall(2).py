import socket
import sys
host = None
port = 50007
s = None
for res in socket.getaddrinfo(host,port,socket.AF_UNSPEC,socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af , socketype , proto , canonname, sa = res
    try:
        s = socket.socket(af,socketype,proto)
    except OSError as msg :
        s = None
        continue
    try: 
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('Could not open socket')
    sys.exit(1)

conn , addr = s.accept()
with conn:
    print('Conneted by',addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)