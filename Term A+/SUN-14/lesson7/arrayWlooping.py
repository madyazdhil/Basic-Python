student = ["Bobby", "Andrea" , "Lucas", "Andrew", "Alex"]
age = [12, 13,11,12,11, 21, 21]

index = 0
print("Here are the student of Koding Next: ")
while index < len(student):
    print(f"{index+1}. {student[index]}")
    index += 1
a = 1
print("this is the age of the student in Koding Next")
for index2 in age:
    print(f"{a}, {index2}")
    a += 1

j = 0
k = 0
while j < len(student) and k < len(age):
    print(f"{student[j]} has the age of {age[k]}")
    j += 1
    k += 1