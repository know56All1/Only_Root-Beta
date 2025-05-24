import os
import time
import socket
import platform

class server_socket():
    def __init__(self):
        self.plataforma = platform.system()
        self.host = "0.0.0.0"
        self.port = 5555
        self.client = 1
        self.buffer = 10000  

        self.ascii = """
 $$$$$$\\            $$\\                 $$$$$$$\\                       $$\\     
$$  __$$\\           $$ |                $$  __$$\\                      $$ |    
$$ /  $$ |$$$$$$$\\  $$ |$$\\   $$\\       $$ |  $$ | $$$$$$\\   $$$$$$\\ $$$$$$\\   
$$ |  $$ |$$  __$$\\ $$ |$$ |  $$ |      $$$$$$$  |$$  __$$\\ $$  __$$\\\\_$$  _|  
$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |      $$  __$$< $$ /  $$ |$$ /  $$ | $$ |    
$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\\ 
 $$$$$$  |$$ |  $$ |$$ |\\$$$$$$$ |      $$ |  $$ |\\$$$$$$  |\\$$$$$$  | \\$$$$  |
 \\______/ \\__|  \\__|\\__| \\____$$ |      \\__|  \\__| \\______/  \\______/   \\____/ 
                        $$\\   $$ |                                             
                        \\$$$$$$  |                                             
                         \\______/           
------------------------------------------------------------------------
1- Server
2- Credits
3- Exit       
------------------------------------------------------------------------             
"""
        self.creador = "----Know56----" 
        self.wallet = "lnbc1p5rzv8spp5r65xuwg9yst7l4602kev6rm5gv6majey0wpm292kk3u3mst8tfhqdqqcqzzsxqzjcsp5lm45pgmq5plzvq64wnzs8sx704dy6r08g70u3j39ftwagxfy996s9qxpqysgqrecpz5k07jqu4fnaarr9mapcskn9u9k4dqruu2ayxqm9lg64evlpcudf73amncye99g785ly54k3njzgvq3en4f70tc90dy8xrhyz5sqkrevfz"

    def conexion(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host1, self.port1))
        self.sock.listen(self.client)
        
        if self.plataforma == "Windows":
                os.system("cls")
        elif self.plataforma == "Linux":
                os.system("clear")

        print(f"--- Server mounted on:{self.port1} ---")
        print("--- waiting for a client ---")

        try:
            self.conn, self.addr = self.sock.accept()
            print(f"--- Client connected from:{self.addr} ---")
            print(f"--- Date and time: {time.ctime()} ---")

            self.message = self.conn.recv(self.buffer)
            print("--- ¡Information received from the client! ---") 
            print(self.message.decode())

            while True:
                comando = input("Command to send> ").strip()
                if not comando:
                    continue

                if comando.lower() in ['exit', 'salir']:
                    print("[*] closing connection")
                    self.conn.close()
                    self.sock.close()
                    time.sleep(2)
                    break

                try:
                    self.conn.sendall(comando.encode())
                    mensaje_result = self.conn.recv(self.buffer)
                    print(f"--- ¡Information received! --- \n{mensaje_result.decode()}")

                except BrokenPipeError:
                    print("[*] the client has been disconnected")
                    time.sleep(2)
                    break

        except Exception as e:
            print(f"[!] Server and/or client error: {e}")
            try:
                self.sock.close()
            except:
                pass

    def credits(self):
        print(f"Creator: {self.creador}")
        print(f"Donations: {self.wallet}")

    def Option(self):
        while True:
            if self.plataforma == "Windows":
                os.system("cls")
            elif self.plataforma == "Linux":
                os.system("clear")

            print(self.ascii)

            try:
                opcion = int(input("OnlyRoot> "))
                if opcion == 1:
                    port_input = input("Input the port (default 5555)> ")
                    if port_input.strip() == "":
                        self.port1 = self.port
                    else:
                        self.port1 = int(port_input)

                    host_input = input("Input the interface (default 0.0.0.0)> ")
                    if host_input.strip() == "":
                        self.host1 = self.host
                    else:
                        self.host1 = host_input

                    self.conexion()

                elif opcion == 2:
                    self.credits()
                    input("Press 'enter' to return...")
                elif opcion == 3:
                    print("¡Bye, Bye!")
                    break
                else:
                    print("Invalid option.")
                    input("Press 'enter' to continue...")
            except ValueError:
                print("Enter a valid number")
                input("Press 'enter' to continue...")


if __name__ == "__main__":
    app = server_socket()
    app.Option()
