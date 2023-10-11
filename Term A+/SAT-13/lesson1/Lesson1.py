# untuk print
print("Hello World")

#cara mebuat variable
#1. declarasi
#2. initate

nama = "ahmad"
print(nama)

#aturan dalam membuat variable
#1. tidak oleh angka didepan
#2. tidak bole mengunakan spasi
#3. tdk boleh sama dalm penamaan

#tipe data

#1. string - karakter - bisa masuk simbol
name = "Yazid@yahoo.co.id     6321873%^&%&^%^"
print(name)

#2. integer - bilang bulat
age = "21"
print(age)

#3. float - bilangan desimal
height = 172.76
print(height)

#boolean
boolean = True
boolean2 = False

##########################
# arithmetics operators - hanya dapat dilakukan oleh integer
# +
# -
# /
# *

# num1 = "76"
# num2 = 87
#
# num5 = int(num1)
#
# addition = num5 + num2
# print(addition)
#
# substract = num5-num2
# print(substract)
#
#
# num3 = int(input("masukkan angka pertama :"))
# num4 = int(input("masukkan angka kedua :"))
#
# pertambahan = num3 + num4
# print(pertambahan)

# height = float(input("masukkaan tinggi badan :"))
# curang = height - 2
# print(curang)

############################################
# round = pembulatan

# round(76.83203)
# phi = 3.1428571428571428571428571428571
# print(round(phi,2))


#####################
#untuk menambahkan data harus menggunakan fungsi input. cara menulis:
#input()
#bisa menambahkan text atau string didalam kurung input. contoh dibawah:

print("selamat datang di restoran kami")
name = input("masukkan nama pelanggan disini: ")
# print("hallo selamat datang, ")
# print(name)

######################################################
# kalimat halo dan isi variabel nama terpisah kalau digabung harus menggunakan concatenation

#concatenation - penggabungan text dengan isi variable
# ada dua cara, dengan simbol (+) dan menggunakan format string / f-string

#1. cara +
# menambahkan simbol (+) SETELAH KUTIP STRING / Diluar petik.

print ("selamat datang kedpada " +name + " semoa kenyang")
makanan = input("MAKANAN FAVORITE :")

#2. cara format string

print (f"ternyata makanan favorite {name} adalah {makanan}")
harga = int(input("masukkan harga yang kamu mau :"))

#=================================================================
#

print(f"harga {makanan} adalah sevbesar {harga} rupiah")
harga_akhir = harga*2
print(f"total yang harus dibayar oleh {name} adalah sebesar {harga_akhir}")

# harga harus dikali 2
# print harga yangsudah dikali dua


