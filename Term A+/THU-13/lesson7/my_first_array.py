tinggi_badan = [172, 165, 143, 126, 122, 145, 170]

print(tinggi_badan)
print(tinggi_badan[0])
print(tinggi_badan[3])
# python function to show or count the amount of value
#len()
print(len(tinggi_badan))
q = len(tinggi_badan)
print(tinggi_badan[q-1])

movieInMay = ["Guardian of Galaxy", "Super Mario Bros", "Elemntal"]
print(movieInMay[0])
print(movieInMay[len(movieInMay)-1])

#to addd data on the array -> append
movieInMay.append("Fast and Furios X")
print(movieInMay)
# j = input("Input your movie here = ")
# movieInMay.append(j)
# print(movieInMay)

#to delete an element in array
#1. using del
del movieInMay[1]
print(movieInMay)

#2. using remove
movieInMay.remove("Elemntal")
print(movieInMay)

print("Berikut merupakan data tinggi badan Siswa Koding Next")
for index in tinggi_badan:
    print(index)

print("\nBerikut merupakan Movie yang muncul di Bulan MAY 2023")
index2 = 0
while index2 < len(movieInMay):
    print(f"{index2+1}. {movieInMay[index2]}")
    index2 += 1



