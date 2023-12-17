import random

item = ["rock", "paper", "scissor"]

player_choice = ""
ai_choice = random.choice(item)

print("Welcome to rock paper scissor game")
print("Please enjoy playing against the AI from the future")

player_choice = input(" Choose your answer: 1 = rock, 2 = paper, 3. scissor")

if (player_choice == "1" and ai_choice == "rock"):
    print("the computer chooses rock as well. It's a tie")

elif (player_choice == "1" and ai_choice == "scissor"):
    print(f"YOU WON. the computer choose {ai_choice}")

elif ((player_choice == "1" and ai_choice == "paper") or
      (player_choice == "2" and ai_choice == "scissor") or
      (player_choice == "3" and ai_choice == "rock")):
    print(f"You Lost!. The computer choose {ai_choice}")
