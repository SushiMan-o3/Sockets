#!/usr/bin/python

import socket
from threading import Thread
import json


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

            connection.send("You are now connected to the server!".encode())

            self.user = connection.recv(1024).decode()
            self.broadcast(f"{self.user} has joined the Chat Room! [{ip_address}]")

            Thread(target=self.check_message, args=(connection,)).start()

    def check_message(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message)
            except:
                self.clients.remove(client)
                client.close()
                break

    def broadcast(self, _input_):
        print(_input_)
        for client in self.clients:
            client.send(_input_.encode())

        with open('Assets/messages.json') as f:
            messages = json.load(f)

        try:
            message = _input_.split(':', 1)
            messages[message[0]] = message[1]
        except IndexError:
            messages["Announcer"] = _input_

        with open('Assets/messages.json', 'w') as f:
            json.dump(messages, f, indent = 4)


if __name__ == '__main__':
    Main().main()

