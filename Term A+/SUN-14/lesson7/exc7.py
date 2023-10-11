print("This is an advance calculator")
print("we will add your number to the array and sums them all, if you're done, type 'done' ")

numbers = []
i = 0
i = input("add a number to the array = ")

while i != "done":
    print("your data has been saved successfully")
    j = int(i)
    numbers.append(j)
    print(numbers)

    i = input("add a number to the array = ")

total = 0
for f in numbers:
    total = total + f

print(f"the result of summing the array is {total}")