import random

wadah = random.randrange(1, 100)

#conditional statement with more than 2 condition -- Using 'elif'

if wadah >= 80:
    print(f"ternyata nilai dari random diatas atau sama dengan 80")
elif wadah >= 50 and wadah <=80:
    print(f"ternyata nilai random berada diantara 50 - 80")
else:
    print(f"nilai nya ada dibawah 50")

print(wadah)