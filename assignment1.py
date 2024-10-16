
#input digunakan untuk memasukkan value/nilai, dan grade adalah variabel yang digunakan untuk menyimpan value yang sudah dimasukkan tadi
grade = input ("Nilai = ")

#Mengonversi nilai dari variabel grade menjadi integer dan menyimpannya dalam 'int_grade'
int_grade = int(grade)


'''
Memeriksa apakah nilai lebih besar atau sama dengan 90
Jika ya, cetak "Excelent" 
'''
if(int_grade >= 90):
    print("Excelent")
    
    '''
    Memeriksa apakah nilai lebih besar atau sama dengan 80
    Jika ya, cetak "very good"
    '''
elif(int_grade >=80):
    print("very good")

    """
    Memeriksa apakah nilai lebih besar atau sama dengan 70
    Jika ya, cetak "good"
    """
elif(int_grade >=70):
    print("good")

    """
    Memeriksa apakah nilai lebih besar atau sama dengan 60
    Jika ya, cetak "average"
    """
elif(int_grade >=60):
    print("average")

    """
     Memeriksa apakah nilai lebih besar atau sama dengan 50
    Jika ya, cetak "fool"
    """
elif(int_grade >=50):
    print("fool")