import random
counts=3
answer=random.randint(1,10)

while counts>0:
    temp=input("what num you think")
    guess=int(temp)

    if guess == answer:
        print("you know what i think")
        print("no prize")
        break
    else:
        if guess <8 :
            print("small")
        else:
            print("big")
    counts=counts-1
    
print("over")
