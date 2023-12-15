from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        @abstractmethod
        def intro(self):
            pass

        @abstractmethod
        def say(self):
            pass
        
class Cat:   
    def intro(self):
        print(f"我是一只沙雕猫咪，我叫{self.name}，今年{self.age}岁~")
        
    def say(self):
        print("mua~")


class Dog:   
    def intro(self):
        print(f"我是一只小狗，我叫{self.name}，今年{self.age}岁~")
        
    def say_hi(self):
        print("哟吼~")

      
class Pig:   
    def intro(self):
        print(f"我是一只小猪，我叫{self.name}，今年{self.age}岁~")
        
    def say(self):
        print("oink~")

        


c = Cat("web", 4)
d = Dog("布布", 7)
p = Pig("大肠", 5)



def animal(x):
    x.intro()
    x.say()


