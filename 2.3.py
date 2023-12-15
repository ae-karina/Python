# _*_ coding:UTF-8 _*_ #
while 1:
    print('############')
    print('欢迎进入史莱姆战记！')
    print('1、开始游戏 2、退出游戏')
    action = int(input('请输入编号：'))
    if action == 1:
        print('欢迎进入游戏')
        print('这里是游戏内容，游戏内容结束')
        print('遇到一只史莱姆，你要做什么呢？')
        print('1、攻击 2、逃跑')

        action = int(input('请输入编号：'))
        if action == 1:
            print('史莱姆逃跑了！')
        elif action == 2:
            print('你在逃跑过程中摔死了！')
        else:
            print('你选的什么？不想玩就别继续了！')
    elif action == 2:
        break