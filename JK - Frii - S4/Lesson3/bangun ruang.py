print("Welcoe to geometry volume calculation\nFIrst we have kubus\n")

side = int(input("Insert the cube's side = "))

vol_cube = side * side * side
print(f"The result for the volume of the cube is {vol_cube}\n\n")


p = int(input("insert the panjang dari balok = "))
l = int(input("insert the lebar dari balok = "))
t = int(input("insert the tinggi dari balok = "))

vol_balok = p * l * t

print(f"The result for the volume of the cube is {vol_balok}\n\n")

phi = 3.14
r = int(input("please input the radius of the cylinder = "))
t = int(input("please input the tinggi of the cylinder = "))

vol_cyc = phi * r * r * t
print(f"the cylinder vol is {vol_cyc}")