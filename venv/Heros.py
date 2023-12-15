class Hero:
    def __init__(self,name ='player1',hp =100,atk =10):
        self.name =name
        self.hp =hp
        self.atk =atk
        print('英雄%s诞生！！'%self.name)

    def hit(self,name):
        name.hp-=self.atk

    def blood(self):
        pass

class Element:
        def __init__(self,name ='boss',hp =1000):
            self.name =name
            self.hp =hp
            print('BOSS%s诞生！！'%self.name)

        def hit(self):
            pass

