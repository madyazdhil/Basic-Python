import random as rd
from art import logo

print(logo)

compNum = rd.randrange(1,10)
easy = 10
hard = 5

def setDifficulties():
    choize = input("Choose the level= 'Easy' or 'Hard' ...").lower()
    if choize == "easy":
        return easy
    elif choize == "hard":
        return hard
    else:
        print("You neither input 'hard' or 'easy'. I will take that as easy")
        return easy

def checkLives(lives):
    if lives > 0:
        print(f"Attempts remaining {lives}")
    else:
        return True

def compare(computer,player):
    if computer == player:
        print(f"You got it\nThe number i'm thinking of is {computer}")
    elif player > computer:
        print("Too High Bro, do it again!!")
    elif player < computer:
        print("Too Low Bro, do it again!!")


def main():
    print("Welcome to Guessing Game\nI'm thingking a number between 1 - 10. \nCan you Guess it.")
    turn = setDifficulties()
    guess = 0
    while turn > 0 and guess != compNum:
        checkLives(turn)
        guess = int(input("Make a guess =  "))
        turn -= 1

        compare(computer = compNum, player = guess)
        if turn == 0:
            print("You have run out of attempt")

main()
