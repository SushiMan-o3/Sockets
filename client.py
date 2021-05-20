#!/usr/bin/python

import socket 
from threading import Thread

class main:
    def __init__(self):
        self.server = socket.socket()
        self.host = "192.168.86.62"

    def main(self):
        self.server.connect((self.host, 5050))
        print(self.server.recv(1024).decode())

        self.user = (input("Give your self a name: ")).replace(' ', '')

        (Thread(target = self.recive)).start()
        (Thread(target = self.announce)).start()


    def recive(self):
        print(self.server.recv(1024).decode())

    def announce(self):       
        while True:
            message = input(f"{self.user}: ")
            self.server.send(f"{self.user}: {message}".encode())



if __name__ == "__main__":
    main().main()
