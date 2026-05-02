from apps.gudang.menu_gudang import menu_gudang
from apps.kasir.menu_kasir import menu_kasir

def main():
    while True:
        print("\n===== SISTEM =====")
        print("1. Gudang")
        print("2. Kasir")
        print("3. Keluar")

        pilihan = input("Pilih Role : ")

        if pilihan == "1":
            menu_gudang()
        elif pilihan == "2":
            menu_kasir()
        elif pilihan == "3":
            print("Terimakasih Telah Menggunakan Sistem Ini")
            break
        else:
            print("Tidak Valid")

if __name__ == "__main__":
    main()