import paramiko
hostname="192.168.1.124"
username="watcharachai"
passwd="password"
port=22
try:
    p=paramiko.Transport((hostname,port))
    p.connect(username =username,password=passwd)
    print("[*]Connected to" +hostname+"via SSH")
    sftp=paramiko.SFTPClient.from_transport(p)
    print("[*]Starting file download")
    sftp.get("/home/watcharachai/test.txt","/Users/watcharachai/Downloads/d.txt")
    print("[*]File download complete")
    print("[*]Starting file upload")
    sftp.put("/Users/watcharachai/Downloads/d.txt","/home/watcharachai/u.txt")
    print("[*]File upload complete")
    p.close()
    print("[*]Disconnected from server")
except Exception as err:
    print("[!]"+str(err))