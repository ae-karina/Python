import turtle as t

#t.bgpic("3.png")
t.pensize(15)  # 设置画笔的大小
t.colormode(255)  # 设置GBK颜色范围为0-255
t.color(185, 143, 99)
t.setup(684, 380)  # 设置主窗口的大小为684*380
t.speed(20)  # 设置画笔速度为10

'''
头顶
'''
t.pu()  # 提笔
t.goto(-174, 128)  # 画笔前往坐标(-100,100)
t.pd()  # 下笔
t.seth(38)
t.circle(-300, 80)

'''
右耳
'''
t.pu()
t.goto(180, 141)
t.pd()
t.seth(10)
t.circle(-188, 120)

t.pu()
t.goto(300, -59)
t.pd()
t.seth(300)
t.circle(65, 60)

'''
左耳
'''
t.pu()
t.goto(-130, 161)
t.pd()
t.seth(180)
t.forward(60)
a = 0.4
for i in range(60):
    if i <= 35:
        a = a + 0.08
        t.lt(1)  # 向左转1度
        t.fd(a)  # 向前走a的步长
    else:
        a = a + 0.08
        t.rt(1)  # 向右转1度
        t.fd(a)

t.pu()
t.goto(-271, -50)
t.pd()
t.seth(225)
t.circle(-200, 60)

'''
脸颊和下巴
'''
# 左边脸颊
t.pu()
t.goto(-221, 61)
t.pd()
t.seth(225)
t.circle(160, 50)
t.seth(290)
t.circle(160, 21)

# 下巴
t.pu()
t.goto(-121, -160)
t.pd()
t.seth(350)
a = 0.4
for i in range(76):
    if i <= 60:
        a = a + 0.08
        t.lt(0.1)  # 向左转1度
        t.fd(a)  # 向前走a的步长
    else:
        a = a + 0.08
        t.lt(0.6)
        t.fd(a)

# 右边脸颊
t.pu()
t.goto(253, -145)
t.pd()
t.seth(30)
t.circle(60, 30)
t.circle(160, 20)
t.seth(92)
t.circle(170, 40)

'''
腮红
'''
# 左腮红
t.pensize(10)
t.color((248, 221, 233), (248, 221, 233))
t.pu()
t.goto(-245, -77)
t.pd()
t.seth(90)
t.begin_fill()  # 外形填充的开始标志
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.rt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长

    else:
        a = a - 0.1
        t.rt(3)
        t.fd(a)

# 右腮红
t.pu()
t.goto(176, -103)
t.pd()
t.seth(90)

a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.rt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长

    else:
        a = a - 0.1
        t.rt(3)
        t.fd(a)
t.end_fill()  # 依据轮廓填充

'''
双手
'''
# 左手
# 手掌
t.pu()
t.color(185, 143, 99)
t.pensize(20)
t.goto(-227, -174)
t.pd()
t.seth(110)
a = 0.4
for i in range(55):
    if i <= 35:
        a = a + 0.08
        t.rt(1)
        t.fd(a)
    if 35 <= i <= 41:
        a = a + 0.08
        t.rt(10)
        t.fd(a)
    if 41 <= i <= 55:
        a = a + 0.08
        t.rt(4)
        t.fd(a)
# 小拇指
t.pu()
t.goto(-158, -150)
t.pd()
t.seth(110)
a = 0.4
for i in range(42):
    if i <= 18:
        a = a + 0.08
        t.rt(2)
        t.fd(a)
    if 18 <= i <= 31:
        a = a + 0.08
        t.rt(10)
        t.fd(a)
    if 31 <= i <= 42:
        a = a + 0.08
        t.rt(3)
        t.fd(a)

# 右手

# 小拇指
t.pu()
t.goto(145, -169)
t.pd()
t.seth(85)
a = 0.4
for i in range(29):
    if i <= 17:
        a = a + 0.08
        t.rt(2)
        t.fd(a)
    if 17 <= i <= 29:
        a = a + 0.08
        t.rt(10)
        t.fd(a)

# 手掌
t.pu()
t.goto(170, -145)
t.pd()
t.seth(45)
a = 0.4
for i in range(50):
    if i <= 28:
        a = a + 0.08
        t.rt(0.9)
        t.fd(a)
    if 28 <= i <= 36:
        a = a + 0.08
        t.rt(10)
        t.fd(a)
    if 36 <= i <= 50:
        a = a + 0.08
        t.rt(3)
        t.fd(a)

'''
眼睛
'''
# 左眼
t.pensize(10)
t.pu()
t.color((84, 194, 241), (84,194,241))
t.goto(-141, 23)
t.pd()
t.seth(345)
t.begin_fill()  # 依据轮廓填充
for i in range(33):
    if 0 <= i < 8:  # or 20 <= i < 30:
        a = a + 0.08
        t.rt(10)  # 向左转3度
        t.fd(a)  # 向前走a的步长

    if 8 <= i < 15:
        a = a + 0.08
        t.rt(5)
        t.fd(a)
    if 15 <= i < 25:
        a = a + 0.08
        t.rt(15)
        t.fd(a)
    if 25 <= i < 33:
        a = a + 0.08
        t.rt(7)
        t.fd(a)
t.end_fill()

# 右眼
t.pensize(10)
t.pu()
t.goto(180, 2)
t.pd()
t.seth(345)
t.begin_fill()
for i in range(33):
    if 0 <= i < 8:  # or 20 <= i < 30:
        a = a + 0.08
        t.rt(11)
        t.fd(a)

    if 8 <= i < 15:
        a = a + 0.08
        t.rt(16)
        t.fd(a)
    if 15 <= i < 20:
        a = a + 0.08
        t.rt(18)
        t.fd(a)
    if 20 <= i < 23:
        a = a + 0.08
        t.rt(5)
        t.fd(a)
t.end_fill()


# 嘴巴
t.pensize(10)
t.color(185, 143, 99)
t.fillcolor(248, 221, 233)
t.pu()
t.goto(-25, -65)
t.pd()
t.seth(270)
t.begin_fill()
a = 0.4
for i in range(48):
    if 0 <= i < 25:
        a = a + 0.1
        t.lt(1)
        t.fd(a)

    if 25 <= i < 40:
        a = a + 0.08
        t.lt(8)
        t.fd(a)

    if 40 <= i < 48:
        a = a + 0.08
        t.lt(4)
        t.fd(a)

t.up()
t.end_fill()
t.goto(-40, -50)
t.down()
t.seth(-60)
t.circle(20, 57)
t.forward(60)
t.circle(20, 57)


t.exitonclick()
