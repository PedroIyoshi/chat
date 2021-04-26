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
        self.enviar = Button(text="Enviar")

        self.chat.place(x=10, y=10, width=600, height=300)
        self.mensagem.place(x=10, y=320, width=540, height=50)
        self.enviar.place(x=560, y=320, width=50, height=50)

        # self.chat.grid(column=1, row=1, columnspan=2, padx=20, pady=20)
        # self.mensagem.grid(column=1, row=2, sticky="ew")
        # self.enviar.grid(column=2, row=2, sticky="e")



root = Tk()
root.title("Chat")
interface(root)
root.mainloop()