from tkinter import *
from tkinter import scrolledtext
from random import randint


class interface():
    def __init__(self, master=None):
        master.config(width=620, height=380)
        self.componentes()

    def componentes(self):
        self.chat = scrolledtext.ScrolledText()
        self.mensagem = scrolledtext.ScrolledText()
        self.mensagem.vbar.pack_forget()
        self.enviar = Button(text="Enviar", command= lambda: 
            self.sendText(str(self.mensagem.get(0.0, END))))

        self.chat.config(state=DISABLED)
        self.chat.place(x=10, y=10, width=600, height=300)
        self.mensagem.place(x=10, y=320, width=540, height=50)
        self.enviar.place(x=560, y=320, width=50, height=50)

    def printMessage(self, texto):
        self.chat.config(state=NORMAL)
        self.chat.insert(INSERT, "Você: " + texto)
        self.chat.config(state=DISABLED)

    def sendText(self, texto):
        self.printMessage(texto)

root = Tk()
root.title("Chat")
interface(root)
root.mainloop()
