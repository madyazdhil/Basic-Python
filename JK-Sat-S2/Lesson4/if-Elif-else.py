
usia = int(input("Masukkan usia orang tersebut = "))

### cara pertama  if - dengan 3 kondisi = nested IF


# #jika usia 1 - 16
# if usia > 1 and usia <= 16:
#     print("Individual tsb merupakan anak - anak")
# else:
#     if usia >=17 and usia <=25:
#         print("Individual tsb merupakan remaja")
#     else:
#         if usia >=26:
#             print("Individual tsb merupakan dewasa")
#         else:
#             print("Anda salah memasukkan format")
#

### cara kedua -- ELIF

if usia > 1 and usia <= 16:
    print("Individual tsb merupakan anak - anak")
elif usia >=17 and usia <=25:
    print("Individual tsb merupakan remaja")
elif usia >=26:
    print("Individual tsb merupakan dewasa")
else:
    print("Anda salah memasukkan format")
