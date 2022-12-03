# ===== Python Tuple ===== #
"""
- Tuple adalah salah satu built-in data type pada python yang bisa digunakan untuk menyimpan banyak item
- Tuple memiliki sifat: ordered dan unchangeable
    * ordered -> item dalam tuple terurut (menggunakan index)
    * unchangeable -> item dalam tuple tidak bisa dirubah, ditambah, dan dihapus setelah tuple dibuat
- Tuple memungkinkan duplikat item (memiliki item yang sama lebih dari satu)
- Item di dalam tuple bisa bertipe apapun
- Untuk membuat tuple bisa menggunakan tanda kurung () atau menggunakan built-in function tuple()
"""

# Membuat tuple dengan tanda kurung
tuple1 = (1,2,3)
print("Membuat tuple dengan tanda kurung: ")
print(tuple1)
print(type(tuple1))

# Membuat tuple dengan built-in function tuple()
tuple2 = tuple((4,5,6))
print("\nMembuat tuple dengan built-in function tuple(): ")
print(tuple2)
print(type(tuple2))

# Membuat tuple dengan tanda kurung yang berisi satu item harus menambahkan koma setelah item
tuple3 = ("item1",)
print(tuple3, type(tuple3))
tuple4 = ("item2")
print(tuple4, type(tuple4))

# nested tuple
print("\nNested tuple: ")
tuple5 = (tuple1, tuple2)
print(tuple5)

# Tuple Concatenation
tuple6 = tuple1 + tuple2
print("Tuple Concatenation: ")
print(f"tuple1 + tuple2: {tuple6}")

# accessing tuple
print("\nMengakses item dalam tuple: ")
print(f"Item tuple1 index ke-2: {tuple1[2]}")
print(f"Item tuple2 index ke-1: {tuple1[1]}")

# tuple unpacking
a, b, c = tuple1
print("\nTuple unpacking: ")
print(a)
print(b)
print(c)

# tuple bersifat immutable/uncangeable
# tuple1[0] = 10 # TypeError: 'tuple' object does not support item assignment

# Pada tuple juga berlaku slicing sama seperti pada list