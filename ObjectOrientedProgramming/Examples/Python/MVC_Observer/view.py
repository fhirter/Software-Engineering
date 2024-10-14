import tkinter as tk

from ObjectOrientedProgramming.Examples.Python.MVC_Observer.subject import Subject


class View(Subject):
    button_text = "foo"

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')

        self.button = tk.Button(self.root, text=self.button_text, command=self.button_handler)

        self.button.pack()

    def update(self):
        self.root.update_idletasks()
        self.root.update()

    def set_button_text(self, text):
        self.button_text = text
        self.button.config(text=text)

    def button_handler(self):
        self.notify()


