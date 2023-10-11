# -> comment / komentar

#Perintah print untuk menampilkan text
print("Hello World") #Selamat datang di program
print("mr. ahmad")

#variable -> ttempat menyiman data secara lokal
# 2 cara menulis variable
#1. Declare -> buat nama variable
#2. Initialize -> isi variable yg sudah dibuat

score = 90
alamat = "Jalan Imam Bonjol"
name1 = "Ahmad Yazid Hilmi"
name2 = "Alexander"

print(alamat)
print(score)
print(name1)

#Data Types

#1. String -> CARAKTER = HURUF, ANGKA, SIMBOL, SPASI , DLL

print("Selamat datang di restaurant saya.")
print("umur saya adalah 21 tahun")
print("yazid@kodingnext.com / ahmad@kodingnext.com")

#2. INTEGER -> bilangan BULAT 0-infinity

age = 21
kelas = 12
angka_favorite = 400000

#3. Float -> bilangan DECIMAL = ada koma

ukuran_sepatu = 42.56 #harus menggunakan (.) bukan koma
print(ukuran_sepatu)

#4. Boolean -> hanya memiliki 2 nilai saja True/False

male = True #capital first Letter
Lulus = False

print(male)

## Operasi Aritmatika
angka1 = 23
angka2 = 333

#cara pertama - menggunakan variable
hasil_penjumlahan = angka1+angka2
hasil_pengurangan = angka1-angka2
hasil_perkalian = angka1*angka2
hasil_pembagian = angka1/angka2
ubah = int(hasil_pembagian)

print(f"Hasil penjumlahan antara {angka1} dan {angka2} adalaha {hasil_penjumlahan}")
print(hasil_pengurangan)
print(hasil_perkalian)
print(ubah)

#cara kedua - langsung print
print(angka1+angka2)
print(angka1-angka2)
print(int(angka1/angka2))
print(angka1*angka2)


## Konversi  Data
a = "21"
b = 3

f = float(b)
converted_a = int(a)
print(f*converted_a)

bagi = converted_a/b
z=int(bagi)
print(str(z))

print(int(bagi))


##CONCATENATION = menggabungkan text dan variable
print("Hello, my name is ")
print(name1)

#cara pertama == simbol +
print("Halo nama saya "+ name1 +"dan umur saya adalah "+ str(age) + " tahun")

#cara kedua === mengubah semuanya menjadi format string
print(f"Hola my name is {name1} dan my age is {age} years old")