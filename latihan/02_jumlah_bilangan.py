# Latihan 2: Jumlah Bilangan 1 sampai n
# Input: bilangan bulat n
# Proses: menjumlahkan bilangan dari 1 sampai n
# Output: jumlah seluruh bilangan

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")