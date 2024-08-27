import paramiko

hostname = '192.168.153.131'
username = "pakin"
passwd = "Excarrin2545M"
port = 22

try: 
    p = paramiko.Transport((hostname, port))
    p.connect(username=username, password=passwd)
    print("[*] Connected to " + hostname + " via SSH")
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Starting file download")
    sftp.get("/home/pakin/Desktop/test.txt","/Users/Pakin/OneDrive - kmutnb.ac.th/Desktop/pakin.txt")
    print("[*] File downloaded complete")
    print("[*] Starting file upload")
    sftp.put("/Users/Pakin/OneDrive - kmutnb.ac.th/Desktop/pakin.txt","/home/pakin/Desktop/fromwin.txt")
    print("[*] File upload complete")
    p.close()
    print("[*] Disconnected from ")

except Exception as err:
    print("[!] "+str(err))