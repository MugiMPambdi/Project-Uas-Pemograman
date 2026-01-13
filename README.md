# NAMA : MUGI MULIYO PAMBUDI
# NIM  : 312510376
# MATA KULIAH : PEMOGRAMAN

# Jenis Project UAS : OOP (Object Oriented Programming)
Deskripsi Program

Program ini merupakan aplikasi pengolahan nilai mahasiswa berbasis Python yang menerapkan konsep Object Oriented Programming (OOP) dan modular programming. Program meminta input dari pengguna, melakukan validasi input, menghitung grade nilai, dan menampilkan hasil dalam bentuk tabel (kotak) di terminal.

Program dibuat untuk memenuhi Project UAS Pemrograman Python.


---

Konsep yang Digunakan

Object Oriented Programming (OOP)

Modular Programming (pemisahan file)

Validasi input menggunakan try-except

Output berbentuk tabel (table view)



---

Struktur Folder
PROJEK-UAS-PYTHON/
├── main.py        # Program utama
├── data.py        # Class Mahasiswa
├── process.py     # Proses perhitungan grade
├── view.py        # Tampilan output tabel
├── img/           # Folder gambar dokumentasi
│   └── output.png
└── README.md


---
## Output Program

Hasil Program (img/output.png)
Penjelasan File
1. data.py

Berisi class Mahasiswa yang berfungsi untuk menyimpan data mahasiswa seperti nama, NIM, dan nilai.
<img  />

2. process.py

Berisi class NilaiProcess yang digunakan untuk menghitung grade berdasarkan nilai mahasiswa.

Kriteria grade:

Nilai ≥ 85 → A

Nilai ≥ 70 → B

Nilai ≥ 60 → C

Nilai < 60 → D
<img  />

3. view.py

Berisi class View yang bertugas menampilkan data mahasiswa dan grade dalam bentuk tabel (kotak) di terminal.
<img  />

4. main.py

Merupakan file utama yang menghubungkan semua modul (data, process, view).

Fungsi utama:

Meminta input dari pengguna

Melakukan validasi input

Menghitung grade

Menampilkan hasil
<img width="624" height="481" alt="Screenshot 2026-01-12 013518" src="https://github.com/user-attachments/assets/1559f4bc-33ad-4151-8c2a-87cf37e9800d" />

Validasi Input

Validasi input dilakukan menggunakan try-except untuk memastikan nilai yang dimasukkan berupa angka. Jika input bukan angka, program akan menampilkan pesan kesalahan.


---

Cara Menjalankan Program

1. Pastikan Python sudah terinstall


2. Buka terminal / command prompt


3. Masuk ke folder project


4. Jalankan perintah:



python main.py


---

Video Dokumentasi & Demo

Link video dokumentasi dan demo program:
-

Kesimpulan

Program ini berhasil menerapkan konsep OOP dan modular programming dengan baik. Program mampu menerima input, memvalidasi data, memproses nilai, dan menampilkan hasil dalam bentuk tabel yang rapi di terminal.


---

Repository ini dibuat untuk memenuhi tugas Project UAS Pemrograman.









