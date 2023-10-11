students = ["Maria", "anthony", "jacob" , "william"]
age = [12, 11, 12, 13]

print("berikut merupakan nama student kelas 5:")

jk = 0
while jk < len(students):
    print(f"{jk+1}. {students[jk]}")
    jk += 1

print("berikut umur siswa kelas 5= ")
for jk1 in age:
    print(jk1)