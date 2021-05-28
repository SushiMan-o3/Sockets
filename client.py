#!/usr/bin/python

import socket 
from threading import Thread
import tkinter


class main:
    def __init__(self):
        self.server = socket.socket()
        self.host = '192.168.86.78'

    def main(self):
        self.server.connect((self.host, 5050))
        print(self.server.recv(1024).decode())

        self.user = (input('Give your self a name: ')).replace(' ', '')

        (Thread(target = self.announce)).start()
        (Thread(target = self.recive)).start()
        
        interface().main()


    def recive(self):
        while True:
            print(self.server.recv(1024).decode())

    def announce(self):       
        while True:
            message = input(f'{self.user}: ')
            self.server.send(f'{self.user}: {message}'.encode())

class interface(main):
    def __init__(self):
        self.window = tkinter.Tk()

    def main(self):
        self.assets()
        self.other()
        self.window.mainloop()

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
    main().main()
