print("Welcome!You can enter your birthday to view your horoscope. ")
yea = int(input("Please input the year of your birth:"))


def isRunyear(y):
    if y % 4 == 0 or y % 400 == 0:
        return True
    return False


def mon():
    while 1:
        mon = int(input("Please input the month of your birth:"))
        if mon < 1 or mon > 12:
            print("Worng!Please input the right month!")
            continue
        else:
            dat(mon)
            break


def dat(m):
    while 1:
        dat = int(input("Please input the date of your birth:"))
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and (dat < 1 or dat > 31):
            print("Worng!Please input the right date!")
        elif (m == 4 or m == 6 or m == 9 or m == 11) and (dat < 1 or dat > 30):
            print("Worng!Please input the right date!")
        elif isRunyear(yea) and m == 2 and (dat < 1 or dat > 29):
            print("Worng!Please input the right date!")
        elif not isRunyear(yea) and m == 2 and (dat < 1 or dat > 28):
            print("Worng!Please input the right date!")
        elif m == 1 and 20 <= dat <= 31 or m == 2 and 1 <= dat <= 18:
            print('You are Aquarius!')
            break
        elif m == 2 and 19 <= dat <= 29 or m == 3 and 1 <= dat <= 20:
            print('You are Pisces!')
            break
        elif m == 3 and 21 <= dat <= 31 or m == 4 and 1 <= dat <= 19:
            print('You are Aries!')
            break
        elif m == 4 and 20 <= dat <= 30 or m == 5 and 1 <= dat <= 20:
            print('You are Taurus!')
            break
        elif m == 5 and 21 <= dat <= 31 or m == 6 and 1 <= dat <= 21:
            print('You are Gemini!')
            break
        elif m == 6 and 22 <= dat <= 30 or m == 7 and 1 <= dat <= 22:
            print('You are Cancer!')
            break
        elif m == 7 and 23 <= dat <= 31 or m == 8 and 1 <= dat <= 22:
            print('You are Leo!')
            break
        elif m == 8 and 23 <= dat <= 31 or m == 9 and 1 <= dat <= 22:
            print('You are Virgo!')
            break
        elif m == 9 and 23 <= dat <= 30 or m == 10 and 1 <= dat <= 23:
            print('You are Libra!')
            break
        elif m == 10 and 24 <= dat <= 31 or m == 11 and 1 <= dat <= 22:
            print('You are Scorpio!')
            break
        elif m == 11 and 23 <= dat <= 30 or m == 12 and 1 <= dat <= 21:
            print('You are Sagittarius!')
            break
        elif m == 12 and 22 <= dat <= 31 or m == 1 and 1 <= dat <= 19:
            print('You are Capricorn!')
            break


mon()
print("Thank you for using!")
