# ===== Variable Type ===== #
"""
- Ada dua tipe variabel dalam python: Local variabel dan Global variabel
"""

# Local Variable
"""
- Variabel lokal -> variabel yang didefinisikan di dalam sebuah fungsi dan mempunyai scope di di dalam fungsi tersebut.
- Scope -> daerah dimana sebuah variabel dapat digunkan
"""
# Deklarasi fungsi  
def add():  
  # Mendefinisikan variabel lokal -> mempunyai scope di dalam fungsi ini saja
  # Variabel a, b, dan c hanya bisa digunakan di dalam fungsi ini  
  a = 20  
  b = 30  
  c = a + b  
  print("The sum is:", c)  
  
# Memanggil fungsi
add() 

# variabel a, b, c tidak bisa digunakan di sini (di luar fungsi dimana variabel didefinisikan)
# print(a) # error: a is not defined -> a tidak terdefinisi


# Global Variabel
"""
- Variabel global -> variabel yang didefinisikan di luar fungsi dan memiliki scope di seluruh program
- kita bisa mengakses variabel global di dalam maupun di dalam sebuah fungsi
- Variabel yang didefinisikan di luar fungsi secara default adalah variabel global
- python menyediakan keyword "global" untuk menggunakan variabel global di dalam sebuah fungsi
- jika di dalam sebuah fungsi tidak menggukana keyword "global", maka fungsi akan menganggapnya sebgai variabel lokal
"""
# Mendefinisikan variabel global dan memberikan nilai awal (inisialisasi)
x = 5 # x adalah variabel global yang bisa diakses di seluruh program
print(id(x))

# variabel global dalam fungsi
def myFunc():
  # x = "Rizki" # diperlakukan sebagai variabel lokal
  global x # x merupakan variabel global, dimana x mengacu pada objek yang sama dengan global variabel
  print(x)
  print(id(x))

  x = "Python" # ketiak nilai x dirubah maka variabel di luar fungsi juga ikut berubah
  print(x)

myFunc()
print(x)

# Delete Variabel
"""
- Untuk menghapus variabel kita bisa menggukana keyword "del"
"""
x = 1
print(x)

del x
print(x) # error: x is not defined
