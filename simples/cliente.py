from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from tkinter import *
from sys import exit
from gui import interface


def mensagem(text):
    send.put(text)


def desconecta():
    root.destroy()
    tcp.close()
    exit(-1)


root = Tk()
root.protocol("WM_DELETE_WINDOW", desconecta)
gui = interface(root, mensagem)


class Send:
    def __init__(self):
        self.__msg = ''
        self.new = True
        self.con = None

    def put(self, texto):
        self.__msg = texto
        if self.con is not None:
            self.con.send(str.encode(self.__msg))

    def get(self):
        return self.__msg

    def loop(self):
        return self.new


def esperar(tcp, send, host='localhost', port=5000):
    tcp.connect((host, port))
    while send.loop():
        gui.printMessage('Conectado a ' + host + '.')
        send.con = tcp
        while send.loop():
            msg = tcp.recv(1024)
            if not msg:
                break
            gui.printMessage('Outro: ' + str(msg, 'utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    tcp = socket(AF_INET, SOCK_STREAM)
    send = Send()
    processo = Thread(target=esperar, args=(tcp, send, host))
    processo.start()
    root.mainloop()
