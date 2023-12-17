import random

computer_guess = random.randrange(1,2)

print("Hi, welcome to Guessing Number Game\nI'm thinking of a number between 1 - 20\nDo you think you can guess what is my number I'm thinking off?\n")

user_guess = int(input("Enter your guess : .."))

print("The answer is ...\n")
print(computer_guess == user_guess)
print(f"the number I'm thinking is {computer_guess}")