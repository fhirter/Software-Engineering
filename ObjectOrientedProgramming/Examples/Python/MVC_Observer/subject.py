from ObjectOrientedProgramming.Examples.Python.MVC_Observer.observer import Observer


class Subject:
    observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        pass

    def notify(self):
        for observer in self.observers:
            observer.update()
