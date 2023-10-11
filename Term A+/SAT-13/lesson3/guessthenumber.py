#mengambil file random
import random
# menyimpan angka random yang telah dipilih
simpanan = random.randrange(1 , 10)
#menyimpan hasil input user
masukan = int(input(f"masukkan angka dari 1-10 = "))

#membandingkan antara inoutan user dan angka random
print(simpanan == masukan)
#menampilkan nilai yang telah di random
print(f" nilai random yang dipilih adalah {simpanan}")