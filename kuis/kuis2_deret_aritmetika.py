# Kuis 2: Deret Aritmetika
# Input: suku pertama a, beda d, dan banyak suku n
# Proses: menghasilkan n suku dan menjumlahkannya
# Output: setiap suku dan jumlah seluruh suku

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi banyak suku
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# Inisialisasi total sebelum perulangan
total = 0

# Menghasilkan suku dan menghitung jumlahnya
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# Menampilkan jumlah akhir
print(f"Jumlah = {total:.2f}")