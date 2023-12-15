import random

while 1:
    print('############')
    print('Welcome to Guess the word game!')
    print('1、begin 2、exit')
    action = int(input('please chose your choice:'))
    if action == 1:
        print('Welcome!')
        a = int(input('Guess what number I think,Please enter a number from 1 to 2:'))
        b = random.randint(1, 3)
        if a < 1 or a > 2:
            print('Illegal input, please re-enter')
            continue
        elif a == b:
            print('Bingo!')
        else:
            print('Wong!')
    elif action == 2:
        break
