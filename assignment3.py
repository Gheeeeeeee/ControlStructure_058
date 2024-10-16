n = int(input("Masukkan angka untuk mencetak deret Fibonacci hingga angka tersebut: "))

# Inisialisasi dua angka pertama dalam deret Fibonacci
fib1, fib2 = 0, 1

# Memeriksa apakah angka yang dimasukkan kurang dari atau sama dengan 0
if n <= 0:
    print("Masukkan bilangan positif.")
# Jika angka yang dimasukkan adalah 1, cetak angka pertama dalam deret
elif n == 1:
    print("Deret Fibonacci hingga", n, ":")
    print(fib1)
else:
     # Jika angka lebih besar dari 1, cetak deret Fibonacci hingga angka tersebut
    print("Deret Fibonacci hingga", n, ":")
    while fib1 < n:
        print(fib1, end=' ')# Mencetak angka Fibonacci
        # Menghitung angka Fibonacci berikutnya
        nth = fib1 + fib2
        fib1 = fib2 # Memperbarui fib1 dengan fib2
        fib2 = nth  # Memperbarui fib2 dengan angka berikutny