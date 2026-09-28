# Latihan 1: Tabel Perkalian
# Input: satu bilangan bulat n
# Proses: mengalikan n dengan bilangan 1 sampai 10
# Output: tabel perkalian n

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    