#declare the function
def addition(num1, num2):
    result = num1 + num2
    return result
    #returning the value to the place where the function got called --> which is in line 9 and 14

#call the function
tampung1 = addition(7,7)
#string the value inside of a variable

print("The result is " + tampung1)
#displaying the result into the console

print(tampung1)
tampung2 = addition(5,12)
print("The result is " + tampung2)
