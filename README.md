# Pertemuan 05 Perulangan Python

## Identitas Mahasiswa

- **Nama:** [khunaepi]
- **NIM:** [2225250053]
- **Kelas:** [3B]
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

---

## Tujuan

Menggunakan perulangan `for` dan `while` dalam Python untuk menyelesaikan masalah iteratif, memahami kondisi berhenti, menelusuri perubahan nilai variabel, serta menguji program di VS Code.

---

## Struktur Folder

```text
pertemuan-05-perulangan-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
└── kuis/
    └── kuis2_deret_aritmetika.py
```

---

## Materi yang Dipelajari

### 1. Perulangan for

Perulangan `for` digunakan ketika program perlu mengulang proses melalui urutan nilai atau ketika jumlah iterasi sudah diketahui.

Contoh:

```python
for i in range(1, 6):
    print(i)
```

### 2. Perulangan while

Perulangan `while` digunakan untuk menjalankan proses selama kondisi bernilai `True`. Variabel kontrol perlu diperbarui agar perulangan dapat berhenti.

Contoh:

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

### 3. Akumulasi

Akumulasi adalah proses menggabungkan nilai secara berulang ke dalam sebuah variabel total.

Contoh:

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Hasilnya adalah `15`.

### 4. Seleksi di dalam perulangan

Seleksi `if` dapat digunakan untuk memeriksa kondisi pada setiap iterasi, misalnya untuk menghitung bilangan genap.

---

## Daftar Latihan

### Latihan 1: Tabel Perkalian

**File:** `latihan/01_tabel_perkalian.py`

Program menerima satu bilangan bulat dan menampilkan tabel perkalian dari 1 sampai 10 menggunakan `for`.

### Latihan 2: Jumlah Bilangan 1 sampai n

**File:** `latihan/02_jumlah_bilangan.py`

Program menerima bilangan bulat `n` dan menghitung jumlah bilangan dari 1 sampai `n` menggunakan perulangan `for` dan variabel `total`.

### Latihan 3: Validasi Input

**File:** `latihan/03_validasi_input.py`

Program meminta nilai ujian dari 0 sampai 100. Jika nilai berada di luar rentang tersebut, program meminta input kembali menggunakan `while`.

### Latihan 4: Menghitung Bilangan Genap

**File:** `latihan/04_hitung_genap.py`

Program menerima bilangan bulat `n` dan menghitung banyak bilangan genap dari 1 sampai `n` menggunakan `for` dan `if`.

---

## Kuis 2: Deret Aritmetika

**File:** `kuis/kuis2_deret_aritmetika.py`

### Tujuan

Membuat program untuk menampilkan `n` suku pertama deret aritmetika dan menghitung jumlah seluruh sukunya menggunakan perulangan.

### Algoritma Kuis 2

1. Meminta input suku pertama `a` dan beda `d`.
2. Meminta input banyak suku `n`.
3. Memeriksa apakah `n` lebih besar dari 0.
4. Jika `n` tidak positif, meminta input kembali menggunakan `while`.
5. Menginisialisasi `total = 0` sebelum perulangan.
6. Menggunakan `for` untuk mengulang sebanyak `n` kali.
7. Menghitung suku dengan `suku = a + i * d`.
8. Menambahkan setiap suku ke variabel `total`.
9. Menampilkan nomor suku dan nilainya dengan dua angka di belakang koma.
10. Menampilkan jumlah seluruh suku setelah perulangan selesai.

### Cara Menjalankan

Jalankan perintah berikut pada terminal VS Code dari folder utama proyek:

```bash
python kuis/kuis2_deret_aritmetika.py
```

Jika menggunakan `python3`:

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

### Hasil Pengujian Kuis 2

| No. | a | d | n | Deret | Jumlah |
|---|---:|---:|---:|---|---:|
| 1 | 2 | 3 | 5 | 2, 5, 8, 11, 14 | 40 |
| 2 | 10 | -2 | 4 | 10, 8, 6, 4 | 28 |
| 3 | 1.5 | 0.5 | 3 | 1.5, 2.0, 2.5 | 6.0 |

---

## Cara Menjalankan Semua Program

Jalankan perintah berikut dari terminal VS Code pada folder utama proyek.

### Latihan 1

```bash
python latihan/01_tabel_perkalian.py
```

### Latihan 2

```bash
python latihan/02_jumlah_bilangan.py
```

### Latihan 3

```bash
python latihan/03_validasi_input.py
```

### Latihan 4

```bash
python latihan/04_hitung_genap.py
```

### Kuis 2

```bash
python kuis/kuis2_deret_aritmetika.py
```

Jika Python di komputer menggunakan perintah `python3`, ganti `python` menjadi `python3`.

---

## Hasil Pengujian

### Latihan 1: Tabel Perkalian

| Input | Hasil yang Diharapkan | Status |
|---|---|---|
| n = 4 | Tabel perkalian 4 dari 1 sampai 10 | Sesuai |
| n = -3 | Tabel perkalian -3 dari 1 sampai 10 | Sesuai |

### Latihan 2: Jumlah Bilangan

| Input | Hasil yang Diharapkan | Status |
|---|---:|---|
| n = 1 | 1 | Sesuai |
| n = 5 | 15 | Sesuai |
| n = 10 | 55 | Sesuai |

### Latihan 3: Validasi Input

| Input | Hasil yang Diharapkan | Status |
|---|---|---|
| 120 | Ditolak, meminta input kembali | Sesuai |
| -5 | Ditolak, meminta input kembali | Sesuai |
| 75 | Diterima | Sesuai |

### Latihan 4: Menghitung Bilangan Genap

| Input | Hasil yang Diharapkan | Status |
|---|---:|---|
| n = 1 | 0 | Sesuai |
| n = 2 | 1 | Sesuai |
| n = 5 | 2 | Sesuai |
| n = 10 | 5 | Sesuai |

**Catatan:** Status pengujian di atas merupakan hasil yang diharapkan berdasarkan test case dalam modul. Pastikan kamu benar-benar menjalankan setiap program sebelum menyerahkan tugas.

---

## Refleksi

Melalui praktik perulangan Python pada Pertemuan 05, saya mempelajari penggunaan `for` dan `while` untuk menyelesaikan masalah yang membutuhkan proses berulang.

Saya memahami bahwa `for` lebih sesuai digunakan ketika jumlah iterasi sudah diketahui, sedangkan `while` digunakan ketika proses bergantung pada suatu kondisi.

Saya juga mempelajari pentingnya menentukan nilai awal, kondisi berhenti, dan pembaruan variabel kontrol. Kesalahan dalam pembaruan variabel dapat menyebabkan infinite loop, sedangkan kesalahan dalam batas perulangan dapat membuat jumlah iterasi tidak sesuai.

Selain itu, saya memahami bahwa variabel akumulator harus diinisialisasi sebelum perulangan agar hasil penjumlahan tidak direset pada setiap iterasi.

Pada Kuis 2, saya menggunakan `while` untuk memvalidasi banyak suku dan `for` untuk menghasilkan deret aritmetika serta menghitung jumlah seluruh suku.

Praktik ini membantu saya memahami hubungan antara algoritma, implementasi program, pengujian, dan dokumentasi menggunakan GitHub.

---

## Kuis Formatif

### 1. Apa keluaran list(range(1, 6))?

Jawaban:

```python
[1, 2, 3, 4, 5]
```

### 2. Mengapa range(1, 10) tidak menghasilkan 10?

Karena nilai `stop` pada `range()` tidak ikut dimasukkan ke dalam urutan nilai yang dihasilkan. Jadi, `range(1, 10)` menghasilkan bilangan 1 sampai 9.

### 3. Kapan for lebih sesuai daripada while?

Ketika jumlah iterasi sudah diketahui atau ketika program perlu mengunjungi urutan nilai yang jelas.

### 4. Sebutkan tiga komponen utama yang harus diperiksa pada while.

Nilai awal, kondisi perulangan, dan pembaruan variabel kontrol.

### 5. Apa penyebab paling umum infinite loop?

Variabel kontrol tidak diperbarui dengan benar sehingga kondisi perulangan terus bernilai `True`.

### 6. Apa nilai akhir total setelah menjumlahkan 1 sampai 5 dengan loop?

Jawaban: `15`.

### 7. Mengapa total = 0 biasanya ditulis sebelum loop?

Agar nilai total diinisialisasi satu kali sebelum perulangan dan tidak direset pada setiap iterasi.

### 8. Bagaimana seleksi if dapat digunakan di dalam loop?

Dengan memeriksa kondisi pada setiap iterasi untuk menentukan apakah suatu nilai perlu diproses atau dihitung.

### 9. Apa fungsi git commit?

Merekam perubahan file sebagai sebuah versi dalam riwayat Git lokal.

### 10. Perintah apa yang mengirim commit terbaru ke GitHub setelah remote tersambung?

```bash
git push
```

---

## Refleksi Teknis

### 1. Bagian mana yang menentukan jumlah iterasi?

Nilai `n` yang digunakan dalam `range(n)` menentukan berapa kali perulangan `for` berjalan pada Kuis 2.

### 2. Mengapa total harus diinisialisasi sebelum loop?

Agar total dimulai dari 0 dan terus bertambah pada setiap iterasi.

### 3. Apa akibatnya jika total = 0 ditempatkan di dalam loop?

Nilai total akan direset menjadi 0 pada setiap iterasi sehingga hasil penjumlahan tidak terkumpul dengan benar.

### 4. Mengapa validasi n lebih sesuai menggunakan while?

Karena jumlah pengulangan untuk meminta input yang valid tidak diketahui sejak awal. Perulangan berhenti ketika `n` sudah positif.

### 5. Bagaimana membuktikan bahwa loop berhenti tepat?

Dengan menelusuri perubahan variabel, memeriksa kondisi berhenti, dan menguji program menggunakan beberapa test case.

---

## Kesimpulan

Pada Pertemuan 05, saya mempelajari perulangan `for` dan `while`, penggunaan `range()`, seleksi di dalam perulangan, akumulasi, pencacahan, serta validasi input berulang.

Saya juga mempraktikkan pengujian dan debugging di VS Code, menyelesaikan empat latihan Python dan Kuis 2 Deret Aritmetika, serta mempelajari penggunaan Git dan GitHub untuk menyimpan dan mengumpulkan hasil pekerjaan.

---

## Referensi

1. RPS Algoritma dan Pemrograman OBE Untirta. Dokumen Program Studi S1 Pendidikan Matematika, Tahun Ajaran 2026/2027 Ganjil.
2. Python Software Foundation. Python 3 Documentation: Control Flow Tools.
3. Visual Studio Code Documentation: Python in Visual Studio Code.
4. GitHub Docs: Creating a New Repository dan Adding Locally Hosted Code to GitHub.
5. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist*, 2nd edition.
6.