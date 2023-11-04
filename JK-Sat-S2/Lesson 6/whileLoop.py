#buat variable awal
penghitung = 0

while penghitung < 10:
    print(f"{penghitung+1}) Ini percobaan While Loop")
    penghitung += 1

counter = True
while counter == True:
    cek = input("masih main? ")

    if cek == "ya":
        print ("ayo bermain")
    elif cek == "tidak":
        print("bye :)")
        counter = False
    else:
        print("input tidak dikenali")