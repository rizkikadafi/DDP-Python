print("=== Program Mencari Luas Trapesium ===")
while True:
    base_a = input("Masukkan panjang sisi atas trapesium: ")
    base_b = input("Masukkan panjang sisi bawah trapesium: ")
    height = input("Masukkan tinggi trapesium: ")
    luas = (int(base_a) + int(base_b)) * int(height) / 2
    print("\nLuas trapesium adalah:", luas, "m^2")
    confirm = input("\nCoba lagi? (y/n): ")
    if confirm == "n" or confirm == "N":
        break
