# Latihan 3: Validasi Input Nilai Ujian
# Input: nilai ujian
# Proses: mengulang input selama nilai di luar rentang 0 sampai 100
# Output: nilai yang sudah diterima

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")