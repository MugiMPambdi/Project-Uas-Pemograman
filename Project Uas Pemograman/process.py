class MahasiswaProcess:
    def hitung_grade(self, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 - 100")

        if nilai >= 85:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        else:
            return "D"
