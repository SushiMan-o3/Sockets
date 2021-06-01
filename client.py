#!/usr/bin/python

import socket
from threading import Thread
import tkinter


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



class Interface(Main):
    def __init__(self):
        super().__init__()

    def main(self):
        func = ['assets', 'other']
        for func in func:
            eval(f'self.{func}()')
        (Thread(target = self.message_send)).start()
        self.window.mainloop()

    def message_send(self):
        while True:
            message = tkinter.Entry(self.window)
            message.pack()
            self.server.send(f'{Main().user}: {message}'.encode())

    def other(self):
        (tkinter.Label(
            text="Malla Family | Chat Room",
            foreground="white",
            background="#86c232",
            padx = 1000,
            pady = 5,
            font = 7
        )).pack()

    def assets(self):
        self.window.title('Chat Room')
        self.window.geometry('1000x600')
        self.window['background'] = '#222629'
        self.window.iconbitmap('Assets/chat-logo.ico')

if __name__ == "__main__":
    Main().main()
