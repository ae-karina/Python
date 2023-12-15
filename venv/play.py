from Heros import *


msg = "欢迎来到英雄无敌的世界....！"
if __name__ =="__main__":
    print(msg)
    milo = Hero('milo')
    boss = Element('boss')
    print("boss hp:",boss.hp)
    print("英雄发起攻击！")
    milo.hit(boss)
    print("boss hp:",boss.hp)