nama = input("Masukkan nama kamu = ")
umur = int(input("Masukkan umur kamu = "))

print(f"Hallo, nama kamu adalah {nama} dan umur kamu {umur + 1}")

#membuat function menghitung luas lingkaran
def luas_lingkaran(r):
    phi = 3.14
    luas = phi * r * r
    return luas

jari = int(input("\n\nMasukkan jari - jari lingkaran untuk dihitung luasnya = "))
l = luas_lingkaran(jari)
print(f"\nLuas dari lingkaran dengan jari-jari = {jari} adalah sebesar {int(l)}")