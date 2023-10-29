#membuat function untung menghitung volume bangun ruang

#vol balok
def Vol_Balok(panjang, lebar, tinggi):
    v1 = panjang * lebar * tinggi
    print(f" Hasil perhitungan volume Balok adalah {v1}")

#vol kubus
def Vol_Kubus(sisi):
    v2 = sisi * sisi * sisi
    print(f" Hasil perhitungan volume Kubus adalah {v2}")

#volume tabung
def Vol_Tabung(phi, r, t):
    v3 = phi * r * r * t
    print(f" Hasil perhitungan volume tabung adalah {v3}")




Vol_Balok(12,10,3)
Vol_Kubus(12)
Vol_Tabung(3.14, 7, 14)
