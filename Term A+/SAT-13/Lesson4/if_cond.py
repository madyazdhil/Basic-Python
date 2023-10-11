import random
# importing the random module to the file

#calling the function to randomise on the random modules from 1 - 100
penampungan = random.randrange(1, 100)
#save the randomised value into a variable

#printing the choosen random values into the console
print(f"nomor yang dipilih adalah: {penampungan}")

#condition -> if the randomized value more than or is 50, the program will print spesific words to the console.
if penampungan >= 50:
    print(f" ternyata {penampungan} lebih dari atau sama dengan 50")
else:
    print(f"gawat, ternyata {penampungan} kurang dari 50")