#buat script dengan menggunakan fungsi random
import random

temp = random.randrange(1,6)
print( "== selamat datang di dadu acak ==")

#menggunakan perulangan for, print temp sebanyak 6 kali
for j in range(0, 6):
    temp = random.randrange(1, 6)
    print(f" anda mendapatkan dadu nomor - {temp}")

for gayung in range (0,7):
    print(f"ini adalah perulangan")

for temp2 in range (0,3):
    print(f"{temp2 + 1}. icha suka sayur")

box = 0
while box < 5:
    print(temp)
    print(f" ini adalah perulangan ke - {box}")
    box += 1

temp5 = 0
while temp5 < 10:
    print("Ahmad")
    temp5 += 1

zo = 0
while zo<10:
    print(f"{zo+1}. ahmad")
    zo += 1

