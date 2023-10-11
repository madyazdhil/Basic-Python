panas = input("apakah panas? ya/tidak = ")
hujan = input("apakah hujan? ya/tidak = ")
mendung = input("apakah mendung? ya/tidak = ")

if panas == "ya":
    print(f"bawa topi jangan lupa")
elif hujan == "ya":
    print(f"jangan lupa bawa payung")
elif mendung == "ya":
    print(f"hati -hati, antara ujan dan panas terik")

else:
    print(f"yaudah dirumah aja")