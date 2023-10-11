# lampu = input("masukkan lampu lalu lintas = ")
#
# if lampu == "green" or lampu == "GREEN":
#     print(f"sudah hijau")
# elif lampu == "red" or lampu == "RED":
#     print(f" berhenti dulu bos")
# elif lampu == "yellow" :
#     print(f"hati - hati")
# else:
#     print(f" antara typo dan tidak ada lampu tersebut di lalulintas")

username = input("masukkan username anda =")
password = input("masukkan password anda = ")


if (username == "udin123" or username == "UDIN123") and (password == "vuio123" or password == "VUIO123"):
    print(f" selamat datang {username} di akun anda")
elif username != "udin123":
    print(f"username anda salah")
elif password != "vuio123":
    print(f"password salah")
else:
    print(f"ada yang salah")