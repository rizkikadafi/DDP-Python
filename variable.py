#variable digunakan untuk store value
x = 5
print(x)

#tipe data variable
x = 4 #x now type int
x = "Rizki" #x now type str

#mendapatkan tipe data variable (type())
x = 5
y = "Rizki"
print(type(x))
print(type(y))

#assign multiple variable
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#one value to multiple variable
a = b = c = "Rizki"
print(a)
print(b)
print(c)

#unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
