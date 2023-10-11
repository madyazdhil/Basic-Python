import exc1

print(f"hasil nya adalah = {exc1.multiple(34, 23)}")
tampung = exc1.div(23, 3)
print(tampung)

#array with 5 values
age = [22,29,23,24,25, 77, 45, 102]
#display the first data
print(age[0])
#display the last data
print(age[4])
#using more advance example:
temp = len(age) #len is a function in python library to count the amount of value
print(temp) #checking the tempt values
last = temp - 1 #to be accessible as an index, we need to kurang 1
print(age[last]) #change the index into the final var

#adding a new data into an array
age.append(900)
print(age)

randomms = []
randomms.append(12)
print(randomms)
randomms.append(23)
print(randomms)

