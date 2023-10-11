import random
from logo import art

print(art)

rand = random.randint(1,50)

def compare(target, guess):
    if guess > target:
        print("The number you guess is too HIGH.")
    elif guess < target:
        print("The number you guess is too LOW.")
    elif guess == target:
        print(f"Congratulations!!!. Your Guess is correct. The number I'm Thinking is {target}")

def check_lives(turn):
    if turn > 0:
        print(f"Attempts remaining is {turn}")
    else:
        return True

def main():
    print("Welcome to Guessing Game. Made By: mr. Ahmad")
    print("I Have a number between 1 to 50.")
    print("Your job is to Guess what number I have. Good Luck")

    turns = 10
    guess = 0

    while turns > 0 and guess != rand:
        check_lives(turns)
        guess = int(input("Make a guess = "))
        turns -= 1
        compare(target=rand,guess=guess)

        if turns == 0:
            print("You Run out of Attempts. Try again Next time")



main()
