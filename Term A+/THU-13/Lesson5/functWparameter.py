def perkalian(a , b):
    hasil = a*a*b
    print(f" hasil dari function ini adalah {hasil}")

def resep_roti(rasa):
    print(f" Siapkan alat dan bahan")
    print(f" Masukkan dan campur bahan bersama perasa {rasa}")
    print(f" Pangganga selama 30 - 60 menit")
    print(f" Roti siap dihidangkan")


angka1 = int(input("masukkan angka1 ="))
angka2 = int(input("masukkan angka1 ="))

c = input("mau coba bikin lagi? y/n = ")

while True:
    if c == "y" or c == "Y":

    else:
        rasa = input("masukkan rasa roti = ")
        resep_roti(rasa)

perkalian(angka1, angka2)
resep_roti("Strawberry")
resep_roti("vanilla")

