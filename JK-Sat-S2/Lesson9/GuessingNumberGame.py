import random

from art import logo

easy_mode = 10
hard_mode = 5
tebakan_komputer = random.randrange(1, 50)

print(logo)

def checkDifficulties():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return easy_mode
    elif difficulty == "hard":
        return hard_mode

def cek_nyawa(nyawa):
    if nyawa > 0:
        print(f"Your attempt is {nyawa}")

def membandingkan(tebakan_player, tebakan_komp):
    if tebakan_player > tebakan_komp:
        print("Too High! Lower your guess")
    elif tebakan_player < tebakan_komp:
        print("Too Low! Guess Higher")
    elif tebakan_player == tebakan_komp:
        print(f"That's correct. the number AI guessing is {tebakan_komp}")

def main():
    print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 50, can you guess what number it is? ")
    urutan = checkDifficulties()
    tebakan = 0

    while urutan > 0 and tebakan != tebakan_komputer:
        cek_nyawa(urutan)
        urutan -= 1

        tebakan = int(input("Make your guess: "))

        membandingkan(tebakan_player=tebakan, tebakan_komp=tebakan_komputer)

        if urutan == 0:
            print("Your running out of attempt!!\nThanks for Playing")

main()

