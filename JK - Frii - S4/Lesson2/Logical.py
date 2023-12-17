
print("Yang bisa mengisi form usia 12 - 24")
input_usia = int(input("masukkan umur anda = "))

cek_umur = (input_usia>=12) and (input_usia<=24)
print(cek_umur)

print("masukkan useram e dan password untuk masuk kedalam akun anda")
user_username = input(" Masukkan username anda disini = ")
user_password = input(" Masukkan password anda disini = ")

username = "ahmadkodingnext"
password = "kn123"

hasilPencocokan = (user_username == username) and user_password == password
print(f"apakah user ini bisa masuk = {not(hasilPencocokan)}")

