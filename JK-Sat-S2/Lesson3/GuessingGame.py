#untuk mengacak kita perlu memanngil modul RANDOM == menggunakan perintah IMPORT

import random

#menyimpan kedalam variable
acak_komputer = random.randrange(1,10) #memanggil fungsi random untuk memilih acak berdasarkan range 1-10

print("Selamat datang di Tebak angka")
print("Aku mempunyai angka 1 - 10, dan kamu harus coba untuk menebak.")

#buat variabel yang menampung tebakan pemain
tebakan_user = int(input("Masukkan tebakanmu = "))

print("Oke mari kita cek")
#cek kebenaran tebakan

hasil = acak_komputer == tebakan_user


print(f"tebakan mu {hasil}")
print(f"Angka yang aku pikirkan adalah {acak_komputer}")

