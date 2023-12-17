#buat function yg dapat menghitung volume balok,kubus, dan tabung

import random

name = "Mr. ahmad" # var global
def Vol_kubus():
    s = 12
    vk = s * s * s
    print(vk)

Vol_kubus()

def Vol_balok(p,l,t):
    vb = p*l*t
    print(vb)

Vol_balok(12,3,4)

def Vol_tabung(r, t):



    phi = 3.14
    vt = phi * r * r * t
    return vt

vbb = Vol_tabung(14,7)
print(vbb)

name1 = input("Masukkan nama = ")
print(f"Hallo {name}")
