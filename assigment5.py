# memasukkan angka untuk menghasilkan pola
n = int(input("Masukkan angka untuk menghasilkan pola: "))

# Menggunakan loop untuk mencetak pola dari 1 hingga n
for i in range(1, n + 1):
    # Mencetak angka i sebanyak i kali, diikuti dengan spasi
    print((str(i) + ' ') * i)