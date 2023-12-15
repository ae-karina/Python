import tkinter as tk
import wsgiref.validate
from doctest import master
import tkinter.messagebox
import play


play_inf = {}

# 窗口
root = tk.Tk()
root.title('Login in Page')
root.geometry('500x300')
root.title('Login Page')

# 标签:姓名、账号、密码
tk.Label(root, text='快来拯救你的抑郁朋友吧!', font=('微软雅黑', 20)).place(x=100, y=20)
tk.Label(root, text='账号:',
         font=('微软雅黑', 12)).place(x=150, y=120)

canvas = tk.Canvas(root, height=14, width=12)
# id_pos = tk.PhotoImage(file='账号.png')
# image = canvas.create_image(0, 0, anchor='nw', image=id_pos)
canvas.place(x=130, y=125)

tk.Label(root, text='密码:',
         font=('微软雅黑', 12)).place(x=150, y=160)

canvas = tk.Canvas(root, height=14, width=12)
# ps_pos = tk.PhotoImage(file='密码.png')
# image = canvas.create_image(0, 0, anchor='nw', image=ps_pos)
canvas.place(x=130, y=165)

# 两个输入框框
input_un = tk.Entry(master)
input_un.place(x=210, y=125)

input_pw = tk.Entry(master, show='*')
input_pw.place(x=210, y=165)


def register():
    ID = input_un.get()
    PW = input_pw.get()
    if ID == '' or PW == '':
        tk.messagebox.showinfo(title='提示', message='用户名或密码不能为空！')
    elif ID in play_inf:
        tk.messagebox.showinfo(title='提示', message='您已注册！请点击登录')
    elif ID not in play_inf:
        f = open('Game log.txt', 'a', encoding='utf-8')
        f.write('\n玩家ID：' + ID)
        f.close()
        sc_inf = {PW: 0}
        play_inf[ID] = sc_inf
        tk.messagebox.showinfo(title='提示', message='注册成功！')


def login_in():
    ID = input_un.get()
    PW = input_pw.get()
    print(ID)
    print(play_inf)
    if ID == '' or PW == '':
        tk.messagebox.showinfo(title='提示', message='用户名或密码不能为空！')
    elif ID in play_inf:
        play_inf[ID][PW] = play.total()
        root.destroy()
    elif ID not in play_inf:
        tk.messagebox.showinfo(title='提示', message='请您先完成注册！')


def bye():
    if tk.messagebox.askokcancel(title='提示', message='确定退出游戏？'):
        root.destroy()


# 按钮
tk.Button(master, text='注册', font=('微软雅黑', 10), width=7, height=1,
          activeforeground='purple', command=register).place(x=120, y=220)
tk.Button(master, text='登录', font=('微软雅黑', 10), width=7, height=1,
          activeforeground='purple', command=login_in).place(x=230, y=220)
tk.Button(master, text='退出', font=('微软雅黑', 10), width=7, height=1,
          activeforeground='purple', command=bye).place(x=340, y=220)

root.mainloop()


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
    # 写入日志
    f = open("Game log.txt", 'a', encoding='utf-8')
    f.write('\n          排行榜          \n')
    f.write('帐号                 总分\n')
    for key, val in lo:
        f.write('%-12s        %3d' % (key, val))


lists()
