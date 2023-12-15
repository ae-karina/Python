import random
import keyboard

ag = 0
fq = 0
hx = 0
ys = 0
jy = 0
print('开始集福啦~~')

print('按下Enter键获取五福')

while True:
    keyboard.wait('enter')
    b = random.randint(1, 6)
    if b == 1:
        print('获取到：爱国福')
        ag += 1
        print('当前拥有的福：')
        print('爱国福：', ag, '富强福：', fq, '和谐福：', hx, '友善福：', ys, '敬业福：', jy)
        if ag >= 1 and fq >= 1 and hx >= 1 and ys >= 1 and jy >= 1:
            break
    elif b == 2:
        print('获取到：富强福')
        fq += 1
        print('当前拥有的福：')
        print('爱国福：', ag, '富强福：', fq, '和谐福：', hx, '友善福：', ys, '敬业福：', jy)
        if ag >= 1 and fq >= 1 and hx >= 1 and ys >= 1 and jy >= 1:
            break
    elif b == 3:
        print('获取到：和谐福')
        hx += 1
        print('当前拥有的福：')
        print('爱国福：', ag, '富强福：', fq, '和谐福：', hx, '友善福：', ys, '敬业福：', jy)
        if ag >= 1 and fq >= 1 and hx >= 1 and ys >= 1 and jy >= 1:
            break
    elif b == 4:
        print('获取到：友善福')
        ys += 1
        print('当前拥有的福：')
        print('爱国福：', ag, '富强福：', fq, '和谐福：', hx, '友善福：', ys, '敬业福：', jy)
        if ag >= 1 and fq >= 1 and hx >= 1 and ys >= 1 and jy >= 1:
            break
    elif b == 5:
        print('获取到：敬业福')
        jy += 1
        print('当前拥有的福：')
        print('爱国福：', ag, '富强福：', fq, '和谐福：', hx, '友善福：', ys, '敬业福：', jy)
        if ag >= 1 and fq >= 1 and hx >= 1 and ys >= 1 and jy >= 1:
            break
print('你已集齐了五福！')