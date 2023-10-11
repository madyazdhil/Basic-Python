from art import logo
import random as rd

print(logo)

computer_number = rd.randrange(1,10)

easy = 10
hard = 5

def setDifficulties():
    level = input("Choose difficulties. Type either 'Easy' or 'Hard' = ")
    if level == "easy":
        return easy
    elif level == "hard":
        return hard
    else:
        print("wrong input, but i would just assume that you choose easy")
        return easy

def check_lives(lives):
    if lives > 0:
        print(f"You have {lives} attempt left, do better!")
    else:
        return True

def compare(human, computer):
    if human == computer:
        print(f"\nYou Genius Human, you guessed the number I thingking which is {computer}")
    elif human > computer:
        print("Too High bro, Try again!")
    elif human < computer:
        print("Too Low Bro, try Again!")


def mainGame():
    print("welcome to guessing game. \n guess the numer that i had between 1 - 10")

    attempt = setDifficulties()
    guess = 0

    while attempt >0 and guess != computer_number:
        check_lives(attempt)
        guess = int(input("Insert your guess ... "))
        attempt -= 1

        compare(human = guess, computer = computer_number)

        if attempt == 0:
            print("You're ran out of attempt")

mainGame()


