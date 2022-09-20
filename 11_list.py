# ===== Python List ===== #
"""
- list dalam python digunakan untuk menampung urutan dari data yang bervariasi
- konsep list mirip dengan string tetapi list mutable (dapat dirubah), yang artinya kita bisa memodifikasi item dalam list secara individual
- list dapat didefinisikan sebagai kumpulan nilai atau item dari tipe yang berbeda
- Item dalam daftar dipisahkan dengan koma (,) dan diapit dengan tanda kurung siku [].
- karateristik list
  1. list itu terurut, artinya setiap item memiliki urutannya masing-masing (index)
  2. setiap element pada list bisa diakses dengan index
  3. list adalah tipe data mutable (bisa dirubah)
  4. list bisa menampung banyak data dari tipe data yang berbeda-beda
- kedua list dianggap sama ketika memiliki data dan urutan data yang sama
- tetapi meskipun kedua list sama tetapi keduanya merupakan objek yang berbeda (tidak identik)
- konsep indexing dan splitting pada list sama dengan pada string
- konsep operator pada list sama dengan pada string
"""
L1 = ["John", 102, "USA"]    
L2 = [1, 2, 3, 4, 5, 6]   
print(type(L1))  
print(type(L2))

a = [1, 2, "Peter", 4.50, "Ricky", 5, 6]  
b = [1, 2, 5, "Peter", 4.50, "Ricky", 6]  
print(a == b)
print(a is b)
print(id(a))
print(id(b))
b = [1, 2, "Peter", 4.50, "Ricky", 5, 6]  
print(a == b)
print(a is b)
print(id(a))
print(id(b))

# updating list value
"""
- List adalah struktur data yang paling serbaguna di Python karena mereka mutable (bisa berubah), dan nilainya dapat diperbarui dengan menggunakan slice dan operator assignment.
- Python juga menyediakan method append() dan insert(), yang dapat digunakan untuk menambahkan nilai ke list.
"""
a = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
a[2] = "Rizki"
print(a)

a.append(10)
print(a)

a.remove("Ricky")
print(a)

a.insert(3, "Kadafi")
print(a)