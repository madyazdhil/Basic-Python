import random

rdm = random.randrange(1,3)

print("Head or Tail\nWe will act as a coin")

answer = "yes"

while answer != "done":

    if rdm == 1:
        print(" You Got Head ")
    else:
        print(" You got tail ")

    answer = input("Hit Enter to do another round, Type 'Done' if you're done playing")
    if answer == "done":
        print("Thanks for using our service")
        answer = "done"
    rdm = random.randrange(1,3)