# ===== Python Dictionary ===== #
"""
- Dictionary adalah salah satu data type pada python yang digunakan untuk menampung data dalam bentuk pasangan key:value
- Dictionary bersifat ordered, changeable, dan tidak memungkinkan penduplikatan item
- value pada dictionary bisa diakses dengan mengacu pada nama key
- membuat dictionary bisa menggunakan kurung kurawal atau dict() constructor
- setiap element pada dictionary dipisahkan dengan koma
- key pada dictionary bisa bertipe apapun asalkan bukan tipe yang bersifat changeable/mutable (seperti list dan set)
""" 
# membuat dict dengan kurung kurawal
print('create dictonary')
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(f'dict1: {dict1}', type(dict1))

# membuat dict dengan dict() constructor
print('create dictionary')
dict2 = dict(name = "John", age = 36, country = "Norway")
print(f'dict2: {dict2}', type(dict2))

# accessing items
print('accessing items')
print(f'dict1 with key brand: {dict1["model"]}')
print(f'dict2 with key name: {dict2["name"]}')

# get keys in dictionary
print('get keys in dictionary')
dict1_keys = dict1.keys()
print(f'keys in dict1: {dict1_keys}', type(dict1_keys))

# get values in
print('get values in dictionary')
dict1_values = dict1.values()
print(f'values in dict1: {dict1_values}', type(dict1_values))

# change item in dictionary
print('change value in dict1 with key year')
dict1['year'] = 1965
print(dict1)

# add item
print('add item in dict1')
dict1['color'] = 'red'
print(dict1)

# remove item
print('remove item with specified key name')
dict1.pop('color')
print(f'pop color: {dict1}')
del dict1['year']
print(f'del year: {dict1}')

# remove dictionary
print('remove a whole dictionary')
# del dict1 # dict1 is no longer exist
dict1.clear() # empties the dict1
print(f'empty dict1: {dict1}')

# loop dictionary
print('looping dict2')
for key, value in dict2.items():
    print(key, value)

# copy dictionary
print('copy dict2 to dict3')
dict3 = dict2.copy()
print(f'dict2: {dict2}')
print(f'dict3: {dict3}')


