import random

c = random.randrange(1,7)

print("welcome to dice game \nwe will give you number from 1 to 6")

confirm = "yes"

while confirm != "no":
    print(c)
    confirm = input("you want to roll again?\nInput 'no' to stop")

    if confirm == 'no':
        print("thanks for playing")
        confirm = "no"
    c = random.randrange(1,7)
