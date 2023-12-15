def cal():
    s = int(input('Please input a int number:'))
    if s % 2 == 0:
        print(s // 2)
    else:
        print(2 * s)


try:
    cal()

except:
    print('Type Wrong!')
