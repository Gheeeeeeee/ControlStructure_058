# Meminta pengguna memasukkan angka untuk mencetak angka ganjil
n = int(input("Masukkan angka untuk mencetak angka ganjil hingga angka tersebut: "))

# Menampilkan pesan untuk angka ganjil yang akan dicetak
print("Angka ganjil hingga", n, ":")
# Menggunakan loop untuk memeriksa setiap angka dari 1 hingga n
for num in range(1, n + 1):
    if num % 2 != 0:  # Memeriksa apakah angka tersebut ganjil
        print(num, end=' ') # Mencetak angka ganjil
