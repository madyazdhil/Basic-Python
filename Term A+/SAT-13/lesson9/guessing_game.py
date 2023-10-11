import random
from art import logo

print(logo)

computerNumber = random.randrange(1,10)
easy = 10
hard = 5
medium = 7

def set_difficulties():
    lvl_input = input("Type 'Easy', 'Hard', or 'Medium': ").lower()

    if lvl_input == "easy":
        return easy
    elif lvl_input == "hard":
        return hard
    elif lvl_input == "medium":
        return medium
    else:
        print("Wrong input, I'll just assume thet you choose Easy")
        return easy

def check_nyawa(nyawa):
    if nyawa > 0:
        print(f"Your Attempt is {nyawa} left")
    else:
        return True

def compare(guess, komputer):
    if guess == komputer:
        print(f"\nCongratulations\nThe number you guessed is correct.\nI'm thingking of the number {komputer}")
    elif guess > komputer:
        print("Too High, Try again -- Lower it this time!")
    elif guess < komputer:
        print("Too Low, Try again -- Higher this time!")

def mainGame():
    print("Welcome to guessing game. \nI would like for you to guess the number i'm thingking right now, between 1 - 10")
    print("--- Choose the Level you'd prefer ---")

    turns = set_difficulties()
    guess = 0

    while turns > 0 and guess != computerNumber:
        check_nyawa(turns)
        guess = int(input("Insert your Guess .. "))
        turns -= 1

        compare(guess = guess, komputer= computerNumber)

        if turns == 0:
            print("Yoou ran out of attempt, try the game again")


mainGame()