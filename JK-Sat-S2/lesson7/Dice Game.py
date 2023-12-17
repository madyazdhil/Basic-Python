import random

dadu = [1,2,3,4,5,6]
rd = random.choice(dadu)

print("Welcome to the Unlimited dice Game")
print("Enjoy playing my game")

endNow = True

while endNow != False:

    print(f"Your dice is = {rd}")

    answer = input("Do you want to get another number? type 1 if yes, and if not, type 0 = ")

    if answer == "1":
        rd = random.choice(dadu)
    elif answer == "0":
        endNow = False

    else:
        print("your input is not 1 or 0!! Type the correct number")