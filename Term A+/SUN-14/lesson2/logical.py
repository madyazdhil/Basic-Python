num1 = 21
num2 = 54
# harsunya menghasilkan False
comp1 = num1 > num2
# harsunya menghasilkan True
comp2 = num1 != num2

#AND --> Only displaying or returning the value of "True" if BOTH STATEMENT ARE TRUE
print(21 >= 21 and 34 != 21)

#if a variable is storing "TRUE" or "FALSE" we can use logica; operator in this way:
logical = comp1 and comp2
print(logical)

#OR --> will displaying or returning "TRUE" if ONE OF THE STATEMENT IS "TRUE"
logical = comp1 or comp2
print(logical)

#NOT --> Reversing the value
balik = not(logical)
print(balik)
