# #defining an array + save datas to array
# brand_HP = ["iPhone" , "samsung" , "Vivo"]
#
# print(f"berikut merupakan merk HP di pasaran Indo : ")
# # calling an array based on it's index
# print(brand_HP[2])

tgl_lahir_XII = [29 , 5 , 7, 18 , 30, 24, 7, 22, 31, 1]
print(f"tanggal lahir siswa absen 1 adalah {tgl_lahir_XII[0]}")

#length ==> mengetahui panjang atau banyak nya data pada suatu value

panjang = len(tgl_lahir_XII)
print(panjang) #melihat berapa banyak data yang ada dalam array
print(f"tanggal lahir siswa terakhir adalah {tgl_lahir_XII[panjang - 1]}")

tayang_bulan_ini = ["Avatar", "Mario Bros" , "Guardian of Galaxy Vol.3" , "Mermaid"]
print(f"film baru tayang adalah {tayang_bulan_ini[len(tayang_bulan_ini)-1]}")

uk_sepatu = [23, 29, 43, 38, 40]
c = len(uk_sepatu)
print(f"ukuran sepatu yang tersedia adalah {uk_sepatu[c-1]}")

#adding data into array (momentarily)
#append()
uk_sepatu.append(41)
print(uk_sepatu)

tayang_bulan_ini.append("Buya Hamka")
print(tayang_bulan_ini)

#delete an array --> Based on the name
#remove
tayang_bulan_ini.remove("Avatar")
print(tayang_bulan_ini)

#delete an array with index
#del
del tayang_bulan_ini[0]
print(tayang_bulan_ini)
