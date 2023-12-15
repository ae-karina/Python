import sys
import play




def Sign():  # 登陆页面
    while 1:
        global ID, PW
        ID = input('请输入你的姓名：')
        if ID in play_inf:
            print('欢迎进入游戏！')
            play_inf[ID][PW] = play.total()
            Home()
        else:
            print('没有该账户，请先注册！')
            Login()


def lists():
    sli = dict(sorted(play_inf.items(), key=lambda x: sum(x[1].values()), reverse=True))
    lo = [list(i.values()) for i in sli.values()]

    lis = []
    for key in sli.keys():
        lis.append(key)

    for i in range(0, len(lis)):
        lo[i].append(lis[i])
        temp = lo[i][0]
        lo[i][0] = lis[i]
        lo[i][1] = temp

    print('          排行榜          ')
    print('帐号                 总分')
    for key, val in lo:
        print('%-12s        %3d' % (key, val))
    Home()


def Home():  # 主页面
    print("这是一个拯救你抑郁症盆友的游戏 !")
    print("$************************$")
    print("$         1、登录         $")
    print("$         2、注册         $")
    print("$         3、查看排行      $")
    print("$         4、退出游戏      $")
    print("$************************$")

    try:
        choice = int(input("请选择: "))
        if choice == 1:
            Sign()
        elif choice == 2:
            Login()
        elif choice == 3:
            lists()
        elif choice == 4:
            print("欢迎下次再来玩！")
            sys.exit()
        else:
            print('请输入正确的选择!')
            Home()
    except Exception:
        print('请输入正确的选择!')
        Home()


ID, PW = '', ''
play_inf = {}

Home()
