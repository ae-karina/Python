print("Welcome to Basketball Score System!")
inf = []
while 1:
    name = input("Please input the player's name OR input 'game over' to check the result:")

    if name in inf:  # 如果函数里有名字已经在列表里
        score = int(input("Please input the player's score(The value range is an integer from 1 to 3):"))
        if 1 <= score <= 3:                           # 判断分值输入是否合法
            inf[inf.index(name) + 1] += score
        else:
            print("Illegal input!")
            continue

    elif name == 'game over':
        b = 2
        adList = [inf[i:i + b] for i in range(0, len(inf), b)]    # 把列表按照姓名分数分为若干子列表

        cou = []
        for i in range(1, len(adList) + 1):
            cou.append(adList[i - 1][1])
        print(cou)

        e = cou.index(max(cou))
        print("The player with the highest score and the result is:", '\n' "name:", adList[e][0], '\t' "score:",
              adList[e][1])
        break
    else:
        inf.append(name)
        inf.append(0)
        score = int(input("Please input the player's score(The value range is an integer from 1 to 3):"))
        if 1 <= score <= 3:
            inf[inf.index(name) + 1] += score
        else:
            print("Illegal input!")
            continue




