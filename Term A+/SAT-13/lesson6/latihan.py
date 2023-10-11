print("==== Welcome to advance Calculator ====")
print("input a number and then press enter.")
print("when you're done, please input 'done' if you wish to sum it")

masuk = 0
number = [] #making an empty array
masuk = input("enter your number ==>") #inputting the number or done input
ds = "done"
while masuk != ds : #will check if the input is not the word done, because if it is then it will not started to do the looping
        convers = int(masuk) #converting the string input into integer
        print("your input has been added to the array")
        number.append(convers) #adding the converted number into the array
        print(number) # displaying the array

        masuk = input("enter your number ==>")

hasil = 0
for counting in number:
    hasil = int(hasil) + counting

print("Thank you for using the advance calc")
print(f"the result of the calculation is = {hasil}")


