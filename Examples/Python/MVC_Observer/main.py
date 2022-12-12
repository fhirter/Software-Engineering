from Examples.Python.MVC_Observer.controller import Controller
from Examples.Python.MVC_Observer.model import Model
from Examples.Python.MVC_Observer.view import View

if __name__ == '__main__':
    words = ["foo", "bar", "fubar", "bazl"]

    model = Model(words)
    view = View()
    controller = Controller(model, view)

    view.run()
