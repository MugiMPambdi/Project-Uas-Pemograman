from data import Mahasiswa
from process import MahasiswaProcess
from view import MahasiswaView

def main():
    try:
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai: "))

        mahasiswa = Mahasiswa(nama, nilai)
        process = MahasiswaProcess()
        view = MahasiswaView()

        grade = process.hitung_grade(nilai)
        view.tampilkan(mahasiswa, grade)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()