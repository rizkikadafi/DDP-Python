import math

print("=== Program Menentukan Akar-Akar Persamaan Kuadrat ===")
print("""
- Persamaan kuadrat dianggap sama dengan 0
- Masukkan persamaan kuadrat sesuai dengan format (ex: 2x^2 - 2x - 12)
""")

while True:
    # mengambil input user
    pers = input("Masukkan Persamaan Kuadrat: ")

    # split string persamaan kuadrat
    component = pers.split()

    # cek jika persamaan yang dimasukkan tidak sesuai format
    if len(component) != 5 or component[0].find("x^2") == -1 or component[2].find("x") == -1:
        print("Persamaan kuadrat yang anda masukkan tidak sesuai dengan format!!\n")
        continue
    else:
        #mengambil nilai a 
        str_a = component[0].replace("x^2", "")
        if str_a == "":
            a = int(1)
        elif str_a == "-":
            a = int(-1)
        else:
            a = int(str_a)

        #mengambil nilai b
        str_b = component[2].replace("x", "")
        if str_b == "":
            b = int(1)
            if x[1] == "-":
                b = -b
        else:
            b = int(str_b)
            if component[1] == "-":
                b = -b

        #mengambil nilai c
        if component[3] == "-":
            c = -int(component[4])
        else:
            c = int(component[4])

        #Nilai Diskriminan
        D = b**2 - 4 * a * c

        if D < 0:
            print("Persmaan kuadrat ini tidak memiliki akar (nilai diskriminan < 0)")
        elif D == 0:
            x1 = (-((b + math.sqrt(D)) / (2 * a)))
            print("x1 = x2 =", x1)
        else:
            x1 = (-((b + math.sqrt(D)) / (2 * a)))
            x2 = (-((b - math.sqrt(D)) / (2 * a)))
            print("x1 =", x1, "dan x2 =", x2)
    confirm = input("\nCoba lagi? (y/n): ")
    if confirm == "n" or confirm == "N":
        break
