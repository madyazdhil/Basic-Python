import random

var_random = random.randrange(1,50)

print("Welcome to guessing number")
print("We'll let you know if the random number is less than 25")
print(f"The random number is {var_random}")

if var_random < 25:
    print("Yes, that random number is less than 25")