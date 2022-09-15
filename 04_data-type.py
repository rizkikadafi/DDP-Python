# ====== Python Data Type ===== #
"""
- Variabel bisa menampung value (nilai), dan setiap nilai mempunyai tipe data.
- python adalah tipe bahasa yang dinamis, karenanya kita tidak perlu mendefinisikan tipe ketika mendeklarasikan variabel.
- Interpreter secara implisit menentukan tipenya berdasarkan nilai yang di-assign
- untuk mengetahui tipe dari sebuah objek, kita bisa menggunakan built-in function -> type()
"""
a = 10
b = "Python"
c = 2.5
print(type(a))
print(type(b))
print(type(c))

# Standard data types (in python)
"""
1. Numeric / Numbers
    - Integer
    - Float
    - Complex number
2. Sequence Type
    - String
    - List
    - Tuple
3. Boolean
4. Set
5. Dictionary
"""

# 1. Numbers
"""
- Numbers menyimpan nilai numerik.
- integer, float, dan complex number adalah bagian dari tipe data numbers python
- selain function type() kita juga bisa menggunakan function isinstance() untuk mengetahui apakah sebuah objek merupakan bagian dari class tertentu.
- int -> int adalah tipe bilangan bulat. Python tidak memiliki batasan panjang bilangan bulat yang bisa ditampung
- float -> float digunakan untuk menampung bilangan decimal dengan koma (floating-point number), hanya akurat sampai 15 poin desimal
- Bilangan kompleks berisi pasangan terurut, yaitu x + iy di mana x dan y masing-masing menyatakan bagian real dan imajiner. Bilangan kompleks seperti 2.14j, 2.0 + 2.3j, dll.
"""
a = 5
print("Tipe data a adalah", type(a))

b = 20.5
b = 20.5555555555555
print(b)
b = 20.55555555555555
print(b)
print("Tipe data b adalah", type(b))

c = 1 + 3j
print("Tipe data c adalah", type(c))
print("Apakan c adalah complex number:", isinstance(c, complex))

# Sequence Type (tipe terurut(ordered set), ditandai dengan adanya peng-index-an)
"""
1. String
- string bisa didefinisikan sebagai urutan karakter yang diwakili dengan tanda kutip
- Dalam python kita bisa menggunakan kutip tunggal, kutip ganda, atau kutip tiga untuk mendefinisikan string
- python menyediakan fungsi dan operator bawaan untuk melakukan operasi dalam string
- dalam kasus string operator + digunakan untuk menggabungkan (concatenate) dua atau lebih string
- dalam python juga operator * digunakan untuk pengulangan string
- untuk menuliskan multi-line string kita bisa menggukan kutip tiga
- ketika menuliskan multi-line string format dalam string sangat diperhatikan
"""
str_1 = 'Hello, World!!' # string menggunakan kutip tunggal
print(str_1)
str_2 = "Welcome to Python!" # string menggunakan kutip ganda
print(str_2)

# multi-line string
str_3 = """Ini adalah 
multi     -        line
string""" # ketika di print ke console format string akan mengikuti penulisan di dalam kutip tiga 
print(str_3)

# Concatenate string
str_4 = str_1 + ", " + str_2
print(str_4)

# Repeating string
str_5 = str_1 * 2
print(str_5)

"""
List
- List adalah sebuah tipe data yang bisa menampung banyak data
- List pada python mirip dengan array di bahasa C, tetapi list bisa berisi bisa berisi data dengan tipe data yang berbeda
- item yang disimpan dalam list dipisahkan dengan koma (,) dan berada di dalam kurung siku([])
- kita bisa mengakses item yang ada dalam list dengan mengacu pada index posisinya (index posisi dimualai dari 0)
"""
list_1 = [1, "hi", 2.5, "python"]
print(list_1) # mencetak list_1
print(list_1[3]) # mencetak item list_1 di posisi index 3 -> "python"

# memodifikasi item pada list_1
list_1[2] = 3
print(list_1)

# Concatenate list
list_2 = list_1 + list_1
print(list_2)

# Repeating list
list_3 = list_1 * 3
print(list_3)

"""
Tuple
- Tuple mirip dengan list 
- Perbedaannya tuple read-only dan didefinisikan menggunakan tanda kurung
- Karena read-only kita tidak bisa memodifikasi nilai dan juga nilai dari item yang ada pada tuple
- dalam tuple berlaku juga concatenate dan repeating
"""
tuple_1 = ("tes", 1, 3, "waw")
# print tipe
print(type(tuple_1))
# print tuple_1
print(tuple_1)
# akses item pada tuple
print(tuple_1[0])

# tuple_1[2] = 5 # error: 'tuple' object does not support item assignment


# Dictionary
"""
- Dictionary adalah unordered set (item tak terurut) dari pasangan key dan value
- key dapat menampung tipe data primitif apa pun, sedangkan value adalah objek Python yang berubah-ubah.
- Item dalam dictionary dipisahkan dengan koma (,) dan berada dalam kurung kurawal {}.
"""

# dictionary dengan key berupa string
dict_1 = {
  "nama": "Rizki",
  "umur": 19
}
# print dict_1
print(dict_1)
# akses item dict_1
print(dict_1["nama"])
print("Nama saya adalah " + dict_1["nama"] + ", umur saya " + str(dict_1["umur"]) + " tahun.")

# mengetahui keys dan value dalam sebuah dictionary
print(dict_1.keys())
print(dict_1.values())

# Boolean
"""
- Tipe boolean menyediakan dua built-in value yaitu True atau False
- Nilai ini digunakan untuk menentukan apakan sebuah statement itu benar atau salah
- kebanyakan nilai bernilai true, kecuali 0 dan objek kosong
"""
print(type(True))
print(type(False))
print(bool("test"))
print(bool(""))

# Set
"""
- Set adalah tipe data pada python yang merupakan kumpulan data tak terurut (unordered-set)
"""


