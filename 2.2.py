print('Welcome to Bookshop!')
print("Activity rules: 40% off for all books, shipping fee is 6 yuan for one book, and shipping fee for each "
      "additional book is one yuan")
price = float(input('Please input the unit price of the book you want to buy :'))
su = int(input('Please input the number of books you want to purchase:'))

b = 6
a = 6
if su == 1:
    a
else:
    for x in range(su - 1):
        b = b + 1
        a = a + b

s = price * su + a

print('Book price:', price, '\n''Quantity purchased', su, '\n''Total price:', s)
