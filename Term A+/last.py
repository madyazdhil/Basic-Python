import random

computerNum = random.randrange(1,10)

Easy = 10
hard = 5


def set_difficulties():
  difficulties_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulties_input == "easy":
    return Easy
  elif difficulties_input == "hard":
    return hard
  else:
    print("You neither input 'hard' or 'easy'. I will take that as easy")
    return Easy

def mainGame():
    print("welcome to guessing game \n guess the numer that i had between 1 - 10")

    turns = set_difficulties()
    guess = 0

    ###while turns > 0 and guess != computerNum:
