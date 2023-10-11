import random

dice = random.randrange(1,6)

print("Welcome to Dice Game, \nWe will choose a number that could represent the dice's Number")

guess = "yes"

while guess != "no":
    print(dice)
    guess = input("Please hit enter. if you're done, type no")

    if guess == "no":
        print("Thanks for playing")
        answer = "no"
    dice = random.randrange(1, 6)