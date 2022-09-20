# ===== Python String ===== #
"""
- String Python adalah kumpulan karakter yang diapit oleh tanda kutip tunggal, kutip ganda, atau kutip tiga.
- Komputer tidak memahami karakter; secara internal, komputer menyimpan karakter yang dimanipulasi sebagai kombinasi dari 0 dan 1 (binary system).
- Dalam Python, string dapat dibuat dengan melampirkan karakter atau urutan karakter dalam tanda kutip. Python memungkinkan kita untuk menggunakan tanda kutip tunggal, tanda kutip ganda, atau tanda kutip tiga untuk membuat string.
- Dalam Python, string diperlakukan sebagai urutan karakter, yang berarti bahwa Python tidak mendukung tipe data karakter (char type); sebagai gantinya, satu karakter yang ditulis sebagai 'p' diperlakukan sebagai string dengan panjang (length) 1.
"""

# create string in Python
# 1. menggunakan kutip tunggal
# str1 = 'Hello, World!'
# print(str1)
# print(type(str1))

# 2. menggunakan kutip ganda
# str2 = "Hello, World!"
# print(str2)
# print(type(str2))

# 3. menggunakan kutip tiga -> biasa digunakan untuk multi-line string
# str3 = """Kutip tiga biasa
# digunakan untuk
# multi-line atau
# doc-string"""
# print(str3)
# print(type(str3))

# String idexing
"""
- karena string merupkan urutan karakter, maka setiap karakter pada string memiliki urutan tertentu yang disebut index
- index pada string dimulai dari 0
- negatif index dimulai dari -1 dan dari karakter yang paling belakang
"""
str1 = "HELLO"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[-1])
# print(str[5]) # IndexError: string index out of range

# string splitting
"""
- python memungkinkan kita untuk mengakses substring dari string yang ada
- sintaks
str[start:stop:step]
note: batas stop yang diberikan ekslusif (tidak termasuk)
- start ketika tidak diberi nilai defaultnya adalah 0
- stop ketika tidak diberi nilai defaultnya adalah sampai akhir karakter string
"""
str1 = "HELLO"
# mulai dari index ke-0 sampai akhir
print(str1[0:])
# mulai dari index ke-1 sampai ke-3
print(str1[1:4])
# mulai dari index ke-0 sampai ke-2
print(str1[:3])
# muali dari index ke-0 sampai akhir
print(str1[:])

# re-assigning string
"""
- objek string tidak mengizinkan untuk merubah item secara individual (karena string immutable)
- sebuah string hanya bisa diganti dengan string baru
"""
# str[0] = "S" # TypeError: 'str' object does not support item assignment
str1 = "Awesome"
print(str1)

# delelting string
"""
- Karena string immutable (tidak bisa dirubah), kita tidak bisa menhapus karakter pada string secara individual
- tapi kita bisa menghapus seluruh string menggunakan keyword del
"""
# del str[4] # TypeError: 'str' object doesn't support item deletion
del str1
# print(str1) # NameError: name 'str1' is not defined.

# String operator
# + penggabungan string (concatenate)
nama_depan = "Rizki"
nama_belakang = "Kadafi"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# * pengulangan string
print(nama_depan * 2)

# [] slice operator
print(nama_depan[3])

# [:] range slice operator
print(nama_depan[1:4])

# in dan not in (membership operator)
print("z" in nama_depan)
print("y" in nama_depan)
print("z" not in nama_depan)
print("y" not in nama_depan)