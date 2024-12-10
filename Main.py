# main.py
import sys
print("Current Python Path:")
for path in sys.path:
    print(path)

from data.Mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.Mahasiswa import TampilkanMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama_baru = input("Masukkan Nama Baru: ")
            jurusan_baru = input("Masukkan Jurusan Baru: ")
            data_mahasiswa.ubah_mahasiswa(nim, nama_baru, jurusan_baru)
        elif pilihan == "4":
            nim = input("Masukkan NIM yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            TampilkanMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            TampilkanMahasiswa.tampilkan_list(data_mahasiswa.list_mahasiswa)
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
