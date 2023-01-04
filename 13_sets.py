# ===== Python Sets ===== #
"""
- Tuple adalah salah satu built-in data type pada python yang bisa digunakan untuk menyimpan banyak item dalam satu variable
- Set memiliki sifat: unordered dan unchangeable
    * unordered -> item dalam set tak terurut (tak ber-index), item dalam set bisa muncul dalam urutan yang berbeda setiap digunakan, dan tidak dapat dirujuk dengan index ataupun key
    * uncangeable -> item dalam set tidak bisa dirubah setelah set dibuat, tetapi bisa dihapus atau ditambahkan
- Duplikat item pada set tidak diizinkan
- Set dapat dibuat dengan menggunakan kurung kurawal atau built-in function set()
"""
# create a set
print('create set')
set1 = {1,2,3,4}
print(f'set1: {set1}', type(set1))

# create a set with built-in function
print('create a set with built-in function')
set2 = set((4,5,6))
print(f'set2: {set2}', type(set2))

# add set item
print('add item 5 to set1')
set1.add(5)
print(set1)

# remove set item
print('remove item 5 from set1')
set1.remove(5)
print(set1)

# join set (update or union)
print('join set2 to set1 update')
set1.update(set2) # exclude any duplicate items
print(set1)

# intersection
print('intersection set1 and set2')
set3 = set1.intersection(set2) # return a new set
print(set3)
# set1.intersection_update(set2) # not return a new set (modify set1)
# print(set1)

# symetric difference (keep all elements, but not the duplicates)
print('symetric difference')
set4 = set1.symmetric_difference(set2) # return a new set
print(set4)
# set1.symmetric_difference_update(set2) # not return a new set (modify set1)
# print(set1)

# loop set
print('looping set')
for item in set1:
    print(item)