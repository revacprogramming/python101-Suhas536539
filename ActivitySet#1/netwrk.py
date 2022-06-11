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
