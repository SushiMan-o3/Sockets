#!/usr/bin/python

import socket
from threading import Thread
import time
import sqlite3


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

        try:
            user, message = _input_.split(':', 1)
        except:
            user = 'Server'
            message = _input_

        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        conn = sqlite3.connect('messageHistory.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                       (user TEXT, message TEXT, timestamp TEXT, server_ip TEXT)''')

        cursor.execute('INSERT INTO messages (user, message, timestamp, server_ip) VALUES (?, ?, ?, ?)',
                       (user, message, current_time, self.IPv4))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    Main().main()

