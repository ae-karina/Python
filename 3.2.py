num = input('Please enter the numbers separated by ",":')
b = [int(x) for x in num.split(',')]
print(sum(b))
