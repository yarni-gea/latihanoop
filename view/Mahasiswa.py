# view/mahasiswa.py
class TampilkanMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        for m in data_mahasiswa:
            print("+", "-" * 45, "+")
            print("|    NIM    |     NAMA     |       JURUSAN      |")
            print("-" * 49)
            print(f"| {m.nim} | {m.nama} | {m.jurusan} |")
            print("+", "-" * 45, "+")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(f"Detail Mahasiswa:\nNIM: {mahasiswa.nim}\nNama: {mahasiswa.nama}\nJurusan: {mahasiswa.jurusan}")
        else:
            print("Mahasiswa tidak ditemukan.")

