import random

c = random.randrange(1,3)
f = "yes"
while f != "no":
    if c == 1:
        print("Head")
    else:
        print("Tails")
    f = input("wanna Play again?? type 'no' to end =")
    c = random.randrange(1, 3)

print("thanks for playing")