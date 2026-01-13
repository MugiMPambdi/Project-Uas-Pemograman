class MahasiswaView:
    def tampilkan(self, mahasiswa, grade):
        print("\n===== DATA MAHASISWA =====")
        print("+----------------+--------+-------+")
        print("| Nama           | Nilai  | Grade |")
        print("+----------------+--------+-------+")
        print(f"| {mahasiswa.nama:<14} | {mahasiswa.nilai:<6} | {grade:<5} |")
        print("+----------------+--------+-------+")
