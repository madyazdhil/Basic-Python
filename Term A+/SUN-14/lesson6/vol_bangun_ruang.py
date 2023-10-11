def vol_balok(p, l, t):
    z = p * l * t
    print(f" Volume balok nya adalah {z}")
def vol_tabung(r, t2):
    phi = 3.14
    z = phi * r * r * t2
    print(z)

q = int(input("Anda mau pilih yang mana 1. Vol balok 2. vol kubus = "))

if q == 1:
    vol_balok(21, 4, 2)
elif q == 2:
    vol_tabung(21, 66)
else:
    print(f" maaf angka angka yang anda masukkan tidak valid")


