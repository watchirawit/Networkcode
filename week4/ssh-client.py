from http import client
from pydoc import cli
from sys import stderr, stdin, stdout
import paramiko


hostname = '192.168.1.124'
port = 22
user = 'wachiraiwit'
passwd = 'password'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname,port=port, username=user, password=passwd)
    while True:
        try:
            cmd = input('$>: ')
            if cmd == 'exit': break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    client.close()

except Exception as err:
    print(str(err))

