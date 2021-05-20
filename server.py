#!/usr/bin/python

import socket
from threading import Thread
import time


class Main:
    def __init__(self):
        self.IPv4 = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def main(self):
        self.server.bind((self.IPv4, 5050))
        self.server.listen()

        print(f'Servers local ip: {self.IPv4}')

        self.check_connections()

    def check_connections(self):
        while True: 
            connection, ip_address = self.server.accept()
            self.clients.append(connection)

            print(f"Connection was gotten from {ip_address}")
            connection.send("You are now connected to the server!".encode())

            Thread(target=self.check_message, args=(connection,)).start()
    
    def check_message(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                Tools().announce(message)
                print(message)
            except:
                self.clients.remove(client)
                client.close()
                break

class Tools(Main):
    def __init__(self):
        ...

    def announce(self, _input_):
        for client in Main().clients:
            client.send(_input_.encode())

if __name__ == '__main__':
    Main().main()
