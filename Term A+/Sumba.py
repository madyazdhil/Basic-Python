"""McFlurry1 = "Oreo"
McFlurry2 = "Choco"
McFlurry3 = "Strawberry"

McFlurry = ["oreo" , "Choco", "Strawberry"]

print(McFlurry[0])
print(McFlurry[1])
print(McFlurry[2])
"""
a = [1,2,3,4,5,6]

banyak = len(a)

#print(a[banyak-1])

for i in a:
    print(i)

# j = 0
# while j < banyak:
#     print(a[j])
#     j += 1
add = int(input("number to add= "))
a.append(add)
print(a[banyak])
print(a)
a.remove(4)
print(a)
