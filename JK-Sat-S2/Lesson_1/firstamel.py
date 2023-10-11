# menampilkan kata pertama dalam bahasa pemrograman
print("Hello World")
print("Mr. Ahmad")

#variable = tempat menyimpan data
alamat = "Jalan Imam Bonjol No.02 Kel. Pelabuhan"
print(alamat) #ini untuk menampilkan isi variable

ukuranSepatu1 = 211
ukuranSepatu2 = 222222

print(ukuranSepatu1)
print(ukuranSepatu2)

## TIPE DATA ##

#1. String
print("Ini adalah contoh string")
#harus ada petik (") & terdiri dari teks,angka, dan simbol
print("yazid123@kodingnext.com")
print("2121")

#2. Integer
# bilangan Bulat
ukuranBaju = 34
print(ukuranBaju)

#3. Float
# bilangan Desimal - harus menggunakan titik sebagai koma
print(2.2)
print(2.1 + 2.7)

#4. Boolean
male = True
female = False


## Arithmatics Operation

print(211 + 321)
print(87.7 - 21)
print(87.7 / 21)
print(87.7 * 21)

x1 = 22
y1 = 3

plus = x1+y1
minus = x1-y1
division = x1/y1
multiply = x1*y1



print(plus)
print(minus)
print(division)
print(multiply)


a = 22
b = 2
c = 4
d = 8

x = b * (a - c)
y = (d+a) * b
z = x / y

print(z)

#ada dua cara untuk melakukan konversi tipe data
#1. variable
z_int = int(z)
print(z_int)

div_int = int(division)
print(div_int)


#2. langsung
print(float(multiply))



# concatenation

name = "Mr. Ahmad"
age = 21
print("Selamat datang, saya adalah ")
print(name)

#1. menggunakan Simbol "+"
print("Guru saya adalah "+ name +" dengan umur " + str(age))

#2. dengan Format-string
print(f"my name is {name} and my age is {age}")
print(f"")
