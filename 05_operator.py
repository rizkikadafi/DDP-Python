# ===== Python Operator ===== #
"""
- Operator bisa didefinisikan sebagai sebuah simbol yang dapat melakukan operasi tertentu antara dua operand
- Operand -> objek (integer, string, dll) yang dioperasikan
- Python menyediakan berbagai operator:
1. Arithmetic operator
2. Comparison operator
3. Assignment operator
4. Logical operator
5. Bitwise operator
6. Membership operator
7. Identity operator
"""

# Arithmetic operator
"""
- Operator aritmatika digunakan untuk melakukan operasi matematika
- Operator aritmatika terdiri dari: + (penjumlahan), - (pengurangan), * (perkalian), / (pembagian), % (modulus / sisa bagi), // (floor division), ** (eksponen)
"""
print("==== Arithmetic Operator")
a = 5
b = 2
# + (penjumlahan)
c = a + b
print(f"{a} + {b} = {c}")

# - (pengurangan)
c = a - b
print(f"{a} - {b} = {c}")

# * (perkalian)
c = a * b
print(f"{a} * {b} = {c}")

# / (pembagian)
c = a / b
print(f"{a} / {b} = {c}")

# % (modulus) -> mengembalikan sisa pembagian
c = a % b
print(f"{a} % {b} = {c}")

# // (floor division) -> mengembalikan nilai pembagian yang dibulatkan ke bawah
c = a // b
print(f"{a} // {b} = {c}")

# ** (eksponen)
c = a ** b
print(f"{a} ** {b} = {c}")

# Comparison Operator
"""
- Operator komparasi digunakan untuk membandingkan nilai dari dua operand dan akan mengembalikan boolean true atau false
= Operator komparasi terdiri dari: == (sama dengan), != (tidak sama dengan), < (kurang dari), > (lebih dari), <= (kurang dari atau sama dengan), >= (lebih dari atau sama dengan)
"""
print("===== Comparison Operator")
# == (sama dengan)
a = 5
b = 5
c = a == b
print(f"{a} == {b} -> {c}")
b = 6
c = a == b
print(f"{a} == {b} -> {c}")

# != (tidak sama dengan)
a = 5
b = 5
c = a != b
print(f"{a} != {b} -> {c}")
b = 6
c = a != b
print(f"{a} != {b} -> {c}")

# < (kurang dari)
a = 5
b = 5
c = a < b
print(f"{a} < {b} -> {c}")
b = 6
c = a < b
print(f"{a} < {b} -> {c}")
b = 4
c = a < b
print(f"{a} < {b} -> {c}")

# > (lebih dari)
a = 5
b = 5
c = a > b
print(f"{a} > {b} -> {c}")
b = 6
c = a > b
print(f"{a} > {b} -> {c}")
b = 4
c = a > b
print(f"{a} > {b} -> {c}")

# <= (kurang dari atau sama dengan)
a = 5
b = 5
c = a <= b
print(f"{a} <= {b} -> {c}")
b = 6
c = a <= b
print(f"{a} <= {b} -> {c}")
b = 4
c = a <= b
print(f"{a} <= {b} -> {c}")

# >= (lebih dari atau sama dengan)
a = 5
b = 5
c = a >= b
print(f"{a} >= {b} -> {c}")
b = 6
c = a >= b
print(f"{a} >= {b} -> {c}")
b = 4
c = a >= b
print(f"{a} >= {b} -> {c}")

# Assignment Operator
"""
- Assignment operator digunakan untuk menetapkan nilai dari ekspresi di ruas kanan ke operand di ruas kiri
- Assignment operator terdiri dari: =, +=, -=, *=, /=, %=, //=, **=
"""
print("===== Assignment Operator")
x = 10
y = 3
print(f"Jika x = {x} dan y = {y}, maka:")
# = -> menetapkan nilai dari ekspresi di ruas kanan ke operand di ruas kiri
x = 10
print(f"x = {x}")

# += -> menjumlahkan nilai dari operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x += y # x = x + y
print(f"x += y -> {x}")

# -= -> mengurangi nilai dari operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x -= y # x = x - y
print(f"x -= y -> {x}")

# *= -> mengalikan nilai dari operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x *= y # x = x * y
print(f"x *= y -> {x}")

# /= -> membagi nilai dari operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x /= y # x = x / y
print(f"x /= y -> {x}")

# %= -> mencari sisa bagi dari nilai operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x %= y # x = x % y
print(f"x %= y -> {x}")

# //= -> membagi nilai dari operand di ruas kiri dengan nilai di ruas kanan lalu dibulatkan kebawah dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x //= y # x = x // y
print(f"x //= y -> {x}")

# **= -> memangkatkan nilai dari operand di ruas kiri dengan nilai di ruas kanan dan menetapkan kembali nilai yang sudah dimodifikasi ke operand di ruas kiri
x = 10
x **= y # x = x ** y
print(f"x **= y -> {x}")

# Logical Operator
"""
- Operator logika digunakan terutama dalam evaluasi ekspresi untuk membuat keputusan.
- Operator logika antara lain: and, or, not
"""
print("===== Logical Operator")
# and -> mengembalikan true jika kedua ekspresi bernilai true, selainnya false
print("Logical and")
print(f"2 == 2 and 2 < 3 -> {(2 == 2) and (2 < 3)}")
print(f"2 == 2 and 2 > 3 -> {(2 != 2) and (2 < 3)}")
print(f"2 != 2 and 2 < 3 -> {(2 != 2) and (2 < 3)}")
print(f"2 != 2 and 2 > 3 -> {(2 != 2) and (2 > 3)}")
# or -> mengembalikan true jika setidaknya salah satu ekspresi bernilai true
print("Logical or")
print(f"2 == 2 or 2 < 3 -> {(2 == 2) or (2 < 3)}")
print(f"2 == 2 or 2 > 3 -> {(2 != 2) or (2 < 3)}")
print(f"2 != 2 or 2 < 3 -> {(2 != 2) or (2 < 3)}")
print(f"2 != 2 or 2 > 3 -> {(2 != 2) or (2 > 3)}")
# not -> membalikkan nilai kebenaran
print("Logical not")
print(f"not(2 == 2) -> {not(2 == 2)}")
print(f"not(2 != 2) -> {not(2 != 2)}")

# Membership Operator
"""
- Membership operator digunakan untuk mengecek apakah sebuah nilai ada pada struktur data tertentu
- Mebership operator terdiri dari: in, not in
"""
list_1 = ["apple", "orange", "banana"]
print(f"banana in list_1 -> {'banana' in list_1}")
print(f"banana not in list_1 -> {'banana' not in list_1}")
print(f"melon in list_1 -> {'melon' in list_1}")
print(f"melon not in list_1 -> {'melon' not in list_1}")

# Identity Operator
"""
- Operator identitas digunakan untuk mengecek apakah sebuah elemen merujuk pada objek yang sama atau tidak
- Operator identitas terdiri dari: is, is not
"""
x = 10
y = 10
print(x is y)
print(x is not y)
y  = 15
print(x is y)
print(x is not y)
