class fruit:
    name = ''
    color = 'green！'

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print('Fruit is:%s' % self.color)
        print("Fruit has been harvested...")
        print("The fruit turned out to be：%s" % fruit.color)


class apple(fruit):
    def __init__(self, name, color):
        fruit.__init__(self, name, color)


class orange(fruit):
    def __init__(self, name, color):
        fruit.__init__(self, name, color)


a = apple("apple", "red")
a.show()

b = orange("orange", "orange")
b.show()
