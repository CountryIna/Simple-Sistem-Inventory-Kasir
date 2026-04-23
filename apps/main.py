import barang
import transaksi

def menu():
    while True:
        print("\n=== MANAJEMEN GUDANG CLI ===")
        print("1. Tambah Barang (Create)")
        print("2. Lihat Tabel Barang (Read)")
        print("3. Barang Masuk (Update)")
        print("4. Barang Keluar (Update)")
        print("5. Hapus Barang (Delete)")
        print("0. Keluar")

        pilihan = int(input("Pilih Menu : "))

        if pilihan == 1:
            nama = input("Masukkan Nama : ")
            merek = input("Masukka Merek : ")
            harga = float(input("Masukkan Harga : "))
            jml = int(input("Masukkan Jumlah : "))
            barang.tambah_barang(nama,merek,harga,jml)

        elif pilihan == 2:
            barang.baca_barang()

        elif pilihan == 3:
            barang.baca_barang() #Menampilkan data agar user bisa tau kodenya
            kode = int(input("Masukkan Kode Barang : "))
            jml = int(input("Jumlah Barang Masuk : "))
            transaksi.barang_masuk(kode, jml)

        elif pilihan == 4:
            barang.baca_barang() #Menampilkan data agar user bisa tau kodenya
            kode = int(input("Masukkan Kode Barang : "))
            jml = int(input("Jumlah Barang Keluar : "))
            transaksi.barang_keluar(kode, jml)

        elif pilihan == 5:
            barang.baca_barang() #Menampilkan data agar user bisa tau kodenya
            kode = int(input("Masukkan Kode Barang : "))
            tanya = input(f"Yakin Hapus Kode {kode}? (y/n) : ")
            if tanya.lower() == 'y':
                barang.hapus_barang(kode)

        elif pilihan == 0:
            print("=== SELESAI ===")
            break

        else:
            print("Pilihan Tidak Valid")

if __name__ == "__main__":
    menu()