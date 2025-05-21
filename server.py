import os
import time
import socket
import platform

class server_socket():
    def __init__(self):
        self.plataforma = platform.system()
        self.tiempo = time.ctime()
        self.host = "0.0.0.0"
        self.port = 5555
        self.client = 1  
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
        self.wallet = "lnbc1p5zea34pp5ddwla6lths0ydmjda89wdkdwa04uv2lxzzgu355v8qnh4klh2ayqdqqcqzzsxqzjcsp5q4apljrzmkx4a8j6c8j4vumcevtdlzkew5c8vtc84rq5ege7lslq9qxpqysgqlu8za4rjpehqmxzptfh6c04q28vvvnmz5mmls0e0vekn4y5tuel4m3tm5d9qs3dap8dwuyle75s3vtt28vapx44nvdmqx8d8fvqtl0cpgzwsla"

    def conexion(self):  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.client)

        print("--- Esperando cliente ---")
        try:
            self.conn, self.addr = self.sock.accept()
            print(f"--- Cliente conectado desde {self.addr} ---\n"
                  f"--- Date time: {self.tiempo}")

            self.mesage = self.conn.recv(1080)
            print("--- ¡Info recibida! ---") 
            print(self.mesage.decode())

            while True:
                comando = input("Command to send> ").strip()
                if comando.lower() in ['exit', 'salir']:
                    break
                try:
                    self.conn.sendall(comando.encode())
                    mensaje_result = self.conn.recv(1080)
                    print(f"--- Info recibida --- \n"
                          f"{mensaje_result.decode()}")
                
                except BrokenPipeError:
                    print("El cliente se ha desconectado.")
                    break

        except Exception as e:
            print(f"Error en el servidor y/o cliente: {e}")

    def credits(self):
        print(f"Creador: {self.creador}")
        print(f"Donaciones: {self.wallet}")

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
                    self.conexion()
                elif opcion == 2:
                    self.credits()
                    input("Presiona Enter para volver...")
                elif opcion == 3:
                    print("¡Bye, Bye!")
                    break
                else:
                    print("Opción no válida.")
                    input("Presiona Enter para continuar...")
            except ValueError:
                print("Ingresa un número válido.")
                input("Presiona Enter para continuar...")


if __name__ == "__main__":
    app = server_socket()
    app.Option()

 

        
    
    
        