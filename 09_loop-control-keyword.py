# ===== Python loop control keyword ===== #
"""
- loop control keyword adalah keyword dalam python yang digunakan untuk mengatur alur dari looping
- adapun loop control keyword antara lain: break, continue, pass
"""

# break keyword
"""
- keyword break dalam python digunakan untuk membawa kontrol program keluar dari loop
- dengan kata lain keyword break digunakan untuk membatalkan eksekusi program saat ini dan akan lanjut ke baris berikutnya setelah loop
"""
# list1 = [1,2,3,4,5]
# for i in list1:
#   if i == 3:
#     break
#   print(i)
# print('selesai')

# continue keyword
"""
- continue keyword akan mengembalikan control loop ke awal dari pengulangan
- Semua baris yang tersisa dalam iterasi loop yang berlaku dilewati oleh kata kunci continue, yang mengembalikan eksekusi ke awal iterasi loop berikutnya.
- dengan kata lain ketika dalam iterasi tertentu terdapat keyword continue, maka iterasi akan di skip
"""
# list1 = [1,2,3,4,5]
# for i in list1:
#   if i == 3:
#     continue
#   print(i)
# print('selesai')

#  pass keyword
"""
- Kata kunci pass digunakan ketika sebuah frase secara sintaksis diperlukan untuk ditempatkan tetapi tidak untuk dieksekusi
"""
list1 = [1,2,3,4,5]
for i in list1:
  if i == 3:
    pass
  print(i)
print('selesai')