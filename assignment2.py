

#memasukkan tiga angka dan mengonversinya menjadi integer
num1 = int(input("angka pertama = "))
num2 = int(input("angka kedua = "))
num3 = int(input("angka ketiga = "))


# Menentukan angka terbesar di antara ketiga angka yang dimasukkan
if (num1 >= num2) and (num1>= num3):
    largest = num1 #Jika num1 adalah yang terbesar
elif (num2 >= num1) and (num2 >= num3):
    largest = num2 #Jika num2 adalah yang terbesar
else:
    largest = num3 ## Jika num3 adalah yang terbesar


## Menampilkan angka terbesar yang ditemukan
print("angka yang terbesar dari ketiga angka tersebut adalah angka : ", largest)