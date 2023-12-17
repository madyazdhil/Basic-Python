taste1 = "starwberry"
taste2 = "Chocolate"
taste3 = "Original"

taste = [ "starwberry", "Chocolate", "Original"]
print(taste)
print(taste[0])

## adding more data manually into thhe array
#append

taste.append("Kelapa Muda")
print(taste)

del taste[0]
print(taste)

print(taste[0])

taste.remove(taste[1])
print(taste)

#to know how many data that we have = length
jumlah_data_di_array = len(taste)

print(f"data sisa ={jumlah_data_di_array}")
