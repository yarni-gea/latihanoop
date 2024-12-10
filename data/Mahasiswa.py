# data/mahasiswa.py
class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.list_mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.list_mahasiswa = [m for m in self.list_mahasiswa if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama_baru, jurusan_baru):
        for m in self.list_mahasiswa:
            if m.nim == nim:
                m.nama = nama_baru
                m.jurusan = jurusan_baru

    def cari_mahasiswa(self, nim):
        return next((m for m in self.list_mahasiswa if m.nim == nim), None)
