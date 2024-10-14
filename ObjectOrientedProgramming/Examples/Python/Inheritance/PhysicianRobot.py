from ObjectOrientedProgramming.Examples.Python.Inheritance.Robot import Robot


class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " takes care of you!")