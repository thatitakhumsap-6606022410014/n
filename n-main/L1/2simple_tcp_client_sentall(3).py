import socket
import sys
host = 'localhost'
port = 50007
s = None
for res in socket.getaddrinfo(host,port,socket.AF_UNSPEC,socket.SOCK_STREAM):
    af , socketype , proto , canonname, sa = res
    try:
        s = socket.socket(af,socketype,proto)
    except OSError as msg :
        s = None
        continue
    try: 
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('Could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'hello Pakin')
    data = s.recv(1024)
print('Receivd',repr(data))