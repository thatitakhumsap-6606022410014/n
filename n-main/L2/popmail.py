import poplib
from email.message import EmailMessage

server = "192.168.153.131"
user = "pakin"
passwd =  'Excarrin2545M'


server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msg = len(server.list()[1])

for i in range(msg):
    for ms in server.retr(i+1)[1]:
        print(ms.decode())