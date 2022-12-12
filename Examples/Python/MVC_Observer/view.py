import tkinter as tk

from Examples.Python.MVC_Observer.subject import Subject


class View(Subject):
    button_text = "foo"

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')

        self.button = tk.Button(self.root, text=self.button_text, command=self.button_handler)

        self.button.pack()

    def run(self):
        self.root.mainloop()

    def set_button_text(self, text):
        self.button_text = text
        self.button.config(text=text)

    def button_handler(self):
        self.notify()


