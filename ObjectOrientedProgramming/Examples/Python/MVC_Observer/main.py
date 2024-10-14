from ObjectOrientedProgramming.Examples.Python.MVC_Observer.controller import Controller
from ObjectOrientedProgramming.Examples.Python.MVC_Observer.model import Model
from ObjectOrientedProgramming.Examples.Python.MVC_Observer.view import View

if __name__ == '__main__':
    words = ["foo", "bar", "fubar", "bazl"]

    model = Model(words)
    view = View()
    controller = Controller(model, view)
    controller.run()
