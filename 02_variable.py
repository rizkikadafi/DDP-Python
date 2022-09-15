# ===== Pyhton Variable ===== #
"""
- Variabel adalah sebuah nama yang digunakan untuk merujuk pada lokasi memori. variabel dalam python juga dikenal sebagai identifier dan digunakan untuk menampung value
"""

# Declaring and assigning variable
"""
- Dalam python, kita tidak perlu menspesifikasikan tipe dari variabel, karena interpreter akan memutuskan sendiri tipenya berdasarkan nilai yang di-assign
- dalam pyhton juga kita tidak perlu melakukan deklarasi/pendifinisian variabel, sebuah variabel otomatis dideklarasikan ketika kita meng-assign value
- operator sama dengan (=) digunakan untuk meng-assign value ke variabel
"""
a = 5 # a adalah sebuah identifier variabel yang merujuk pada lokasi memori dimana objek integer 5 berada
print(a)

# dalam bahasa pemrograman lain (c++)
# int a; -> pendefinisian / pendeklarasian variabel, proses ini ditunjukkan untuk menyiapkan slot memori untuk menampung nilai bertipe integer, dimana a merupakan identifier yang merujuk pada lokasi memori tersebut.
# a = 5; -> nilai 5 di-assign ke variabel a
# pendeklarasian dan assignment bisa dilakukan dalam satu statement -> int a = 5;

# Object references
"""
- Proses python dalam memperlakukan objek agak berbeda dengan bahasa pemrograman lain.
- Python adalah bahasa pemrograman yang sangat berorientasi objek; itu sebabnya setiap item data termasuk dalam tipe kelas (objek) tertentu.
"""
print("Python") # python akan membuat objek string dan menampilkannya ke console
# kita bisa memeriksa tipenya dengan fungsi built-in -> type()
print(type("Python")) # <class 'str'>

"""
- Dalam python, variabel adalah nama simbolik yang merujuk pada sebuah objek.
- Variabel digunakan untuk menunjukkan objek dengan nama tersebut
- Object identity -> Dalam pyhton, setiap identifier objek itu unik, pyhton menjamin bahwa tidak ada dua objek yang memiliki identifier yang sama
- untuk mengetahui identifier objek kita bisa menggukan built-in function -> id()
"""
a = 10 # a merujuk pada objek integer
b = a # b merujuk pada objek integer yang sama, karena python tidak membuat objek lain
print("id a     :", id(a))
print("id b     :", id(b))
b = 20 # sekaran b merujuk pada objek integer yang berbeda
print("id b baru:", id(b))


# Multiple assignment
# 1. assign nilai tunggal ke banyak variabel
x = y = z = 100
print(x)
print(y)
print(z)

# 2. assign banyak nilai ke banyak variabel
x, y, z = 100, 200, 300
print(x)
print(y)
print(z)


