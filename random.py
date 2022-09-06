import random

while True:
    print(random.randrange(1, 10)) #pseudo random -> menggunakan detik
    confirm = input("Acak y/n")
    if  confirm == "n":
        break
