from Examples.Python.MVC_Observer.model import Model
from Examples.Python.MVC_Observer.observer import Observer
from Examples.Python.MVC_Observer.view import View


class Controller(Observer):
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        self.view.attach(self)

    def update(self):
        word = self.model.get_random_word()
        self.view.set_button_text(word)



