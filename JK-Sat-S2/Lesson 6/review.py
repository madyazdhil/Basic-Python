#if input = kanan : print-> tangan kanan digunakan untuk makan
#if input = kiri : print-> tangan kiri digunakan untuk membersihkan sisa makanan\
#else: salah masukkan input


pilihan = input("Pilih antara kanan atau kiri: ")

if pilihan == "kanan":
    print("Tangan Kanan digunakan untuk makan")
elif pilihan == "kiri":
    print("Tangan Kiri digunakan untuk membersihkan makanan")
else:
    print("Input tidak dikenali")

##2. random
#random angka 1 - 100

import random

acak = random.randrange(1 , 100)

print(acak)

#function untuk menghitung rumus berikut
# A * (B - C) / A

def rumus1():
    a = 12
    b = 3
    c = 6

    r1 = a * (b - c) / a
    print(r1)


rumus1()

#buatkan function dgn parameter untuk menghitung rumus berikut
#(a * b)/(a - b)

def rumus2(a, b):
    r2 = (a * b) / (a - b)
    print(r2)

rumus2(4, 6)
