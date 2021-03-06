#!/usr/bin/python

import socket
from threading import Thread


class Main:
    def __init__(self):
        self.server = socket.socket()
        self.host = "192.168.86.78"

    def main(self):
        self.server.connect((self.host, 5050))
        print(self.server.recv(1024).decode())

        self.user = (input("Give your self a name: ")).replace(' ', '')
        self.server.send(self.user.encode())
        
        (Thread(target = self.announce)).start()
        (Thread(target = self.recive)).start()

    def recive(self):
        while True:
            print(self.server.recv(1024).decode())

    def announce(self):
        while True:
            message = input()
            self.server.send(f"{self.user}: {message}".encode())


if __name__ == "__main__":
    Main().main()
