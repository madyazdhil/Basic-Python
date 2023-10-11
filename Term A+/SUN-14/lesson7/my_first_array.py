
# making an array
tinggi_badan = [173, 125, 180, 172, 32, 545, 6565, 656,6562, 434,]

# calling / showing all array
print(tinggi_badan)

# showing the first array
print(tinggi_badan[0])
print(tinggi_badan[3])

#counting the amount of values inside of an array
#len()
print(len(tinggi_badan))

#saving the values of the len() fuction
pouch = len(tinggi_badan)
#geting that last index
index1 = pouch - 1
print(tinggi_badan[index1])

showing = ["Avatar 2", "Mario Bros", "Guardian of Galaxy vol.3", "Buya hamka"]
print(showing[0])
print(showing[len(showing)-1])

#to add more data into the array
#append()
showing.append("Fast and Furious X")
print(showing)

#to delete the data on an array by its index
#del
del showing[0]
print(showing)

#to delete a data by it's name:
#remove
showing.remove("Mario Bros")
print(showing)



