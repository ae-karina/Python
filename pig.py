class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我叫{self.name}，今年{self.age}岁。")
        
class FlyMixin:
    def fly(self):
        print("哦豁，我还会飞~")

class Pig(FlyMixin, Animal):
    def special(self):
        print("我的技能是拱大白菜~")

p = Pig("大肠", 5)
p.say()
p.special()
p.fly()
