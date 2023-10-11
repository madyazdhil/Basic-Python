print("Welcome to advance calculator \nEnter the numbers that you wanted to sum\nPlease type 'done' if you are finished")
number = []
i = input("Enter your number here = ").lower()

while i != "done":
    print("Your input has been added")
    j = int(i)
    number.append(j)
    print(number)

    i = input("Enter your number here = ").lower()

total = 0
for k in number:
    total = total + k

print(f"Thanks for using this very well advance Calculator\nThe sums of your number is {total}")


