def lingkaran(jari):
    phi = 3.14
    luas = phi * jari * jari
    return luas

masuk = int(input("Masukkan jari-jari :"))
hasil = lingkaran(masuk)
print(f"luas lingkaran dengan jari-jari {masuk} adalah sebesar {int(hasil)}")