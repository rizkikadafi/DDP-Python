# ====== Python if-else Statement ====== #
"""
- Pengambilan keputusan adalah aspek terpenting dari hampir semua bahasa pemrograman.
- pengambilan keputusan memungkinkan kita untuk menjalankan blok kode tertentu untuk keputusan tertentu.
- Dalam python, pengambilan keputusan dilakukan oleh statement berikut:
  1. if statement -> if statement digunakan untuk menguji kondisi tertentu, jika kondisi benar (true), blok kode (if-block) akan dieksekusi
  2. if-else statement -> if-else statement mirip dengan if statement, tetapi statement ini menyediakan blok kode untuk false case (blok kode yang akan dijalankan ketika kondisi di if statement tidak terpenuhi)
  3. elif statement -> elif statement memungkinkan kita untuk mengecek banyak kondisi dan menjalankan blok kode yang spesifik berdasarkan kondisi yang bernilai true
  note: 
  - jika ada banyak elif statement, yang akan dijalankan adalah blok kode elif statement yang memiliki kondisi true dan yang pertama, jika elif statement kedua bernilai true juga tetap tidak dijalankan
  - elif statement digunakan setelah if statement
"""

# Python Indentation
"""
- dalam python sebuah blok kode tertentu ditandai dengan adanya indentasi
- Ketika kumpulan statement memiliki level indentasi yang sama, maka kumpulan statement tersebut berada dalam satu blok yang sama
"""

# if statement
"""
Sintaks:
if ekspresi:
  statement
"""
# num = int(input("Masukkan angka: ")) # mengambil input user dan di konversi menjadi int lalu di masukkan ke variable num
# if num % 2 == 0: #mengecek apakah num dibagi dua memiliki sisa bagi 0
#   print(f"angka {num} merupakan bilangan genap.") # jika ekspresi diatas bernilai true maka statement ini akan dijalankan, jika tidak blok ini tidak akan dijalankan dan langsung keluar dari blok

# if-else statement
"""
Sintaks:
if ekspresi:
  statement 1
else:
  statement 2

- blok else statement akan dijalankan ketika eksperesi di if statement bernilai false
"""
# num = int(input("Masukkan angka: ")) # mengambil input user dan di konversi menjadi int lalu di masukkan ke variable num
# if num % 2 == 0: #mengecek apakah num dibagi dua memiliki sisa bagi 0
#   print(f"angka {num} merupakan bilangan genap.") # jika ekspresi diatas bernilai true maka statement ini akan dijalankan, jika tidak maka blok else yang akan dijalankan
# else:
#   print(f"angka {num} merupakan bilangan ganjil.") # blok ini akan dijalankan ketika ekspresi pada if statement bernilai false

# elif statement
"""
Sintaks:
if ekspresi 1:
  statement 1
elif ekspresi 2:
  statement 2
elif ekspresi 3:
  statement 3
  .
  .
else:
  statement n

- blok else optional, boleh ada boleh tidak
- jika blok if bernilai true, maka blok dibawahnya tidak akan dijalankan, begitu juga jika blok elif 1 bernilai true, maka blok di bawahnya tidak dijalankan.
"""
# contoh kasus, mengecek nilai 
nilai = int(input("Masukkan nilai anda: "))
if nilai > 85 and nilai <= 100:
  print("Skor nilai anda A")
elif nilai > 60 and nilai <= 85:
  print("Skor nilai anda B")
elif nilai > 40 and nilai <=60:
  print("Skor nilai anda C")
elif nilai >= 0 and nilai <= 40:
  print("Skor nilai anda D")
else:
  print("Nilai yang anda masukkan tidak valid!!")




