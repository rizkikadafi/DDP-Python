# ===== Python for loop ===== #
"""
- Dalam python for loop biasa digunakan untuk melakukan pengulangan terhadap iterable objek seperti list, tuple, atau string
- pengulangan yang dilakukan berdasarkan item/member yang ada dalam objek tersebut
- python for statement akan menulusuri satu per satu element yang ada dalam objek secara terurut dan menjalankan blok kode pada setiap penulusuran
- sintaks:
for item in sequence:
  loop body (blok kode)
"""
from calendar import c


numbers = [1,2,3,4,5]
for number in numbers: # number merepresentasikan setiap element di dalam numbers
  print(number ** 2) # setiap number di pangkatkan 2

# range() function
"""
- range() adalah built-in function dalam python yang menyediakan urutan angka yang mengikuti pola tertentu
- sintaks:
range(start, stop)
- jika hanya diberikan satu nilai maka default start bernilai 0
"""
for i in range(0, 10):
  print(i) # print 1 - 9
