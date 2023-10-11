import random as rr

e = ["Rock", "Paper" , "Scissor"]
d = rr.choice(e)

print("Welcome to ROCK PAPER SCISSOR GAME !!!!\nYou will be playing against AI.\nGoodluck for that!")

end = False
while end != True:
    print("ROCK , PAPER, SCISSOR, SHOOT")
    f = int(input("please input your answer. 0 = Rock, 1 = Paper, 2 = Scissors"))
    player = e[f]
    if player == d:
        print("TIE")
