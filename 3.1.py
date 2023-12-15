from shlex import join

ins = input("Please input you id number:")  # 7~14  6~13
ids = [ins[0:7], ins[6:14], ins[14:18]]
ids[1] = '********'
print('You id is:', "", join(ids))
x = ins[6:14]
print('Your birthday is:', x)

