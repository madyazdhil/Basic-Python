def func(x):
    if x % 2 == 0:
        print(f"{x} is Even number")
    else:
        print(f"{x} is Odd number")

x = int(input("Enter a number "))
func(x)