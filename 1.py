import turtle as d
#d.bgpic("1.png")
d.pensize(20)  # 设置画笔的大小
d.colormode(255)  # 设置GBK颜色范围为0-255
d.color(138, 37, 115)  # 设置画笔颜色和填充颜色(pink)
d.setup(840, 500)  # 设置主窗口的大小为840*500
d.speed(15)  # 设置画笔速度为10

#底部
d.pu()  # 提笔
d.goto(-150, 140)  # 画笔前往坐标(-100,100)
d.pd()  # 下笔
d.seth(-120)  # 笔的角度为-30°
d.right(20)
d.circle(180,140)
d.circle(40,150)
d.seth(130)
d.forward(70)
d.seth(-70)
d.circle(40,-130)
d.seth(-40)
d.forward(20)
d.forward(120)
d.seth(20)
d.circle(120,30)
d.circle(140,90)
d.seth(-90)
d.forward(100)
d.circle(-30,180)

d.forward(100)
d.circle(30,180)
d.forward(70)
d.circle(-20,180)
d.forward(70)
d.circle(30,180)
d.forward(100)
d.circle(-20,180)
d.forward(100)
d.seth(-900)
d.circle(90,10)

d.exitonclick()