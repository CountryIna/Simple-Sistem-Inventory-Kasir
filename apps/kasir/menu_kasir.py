from apps.kasir.transaksi import proses_transaksi
from core.koneksi import konek_db

def cari_barang(keyword):
    conn = konek_db()
    cursor = conn.cursor()
    cursor.execute("SELECT kode, nama, merek, harga, stok "
                   "FROM barang "
                   "WHERE nama LIKE %s OR merek LIKE %s ",
                   (f"%{keyword}%", f"%{keyword}%"))

    hasil = cursor.fetchall()
    conn.close()
    return hasil

def menu_kasir():
    list_barang = []

    print("========= KASIR =========")
    print("Ketik 'selesai' untuk checkout\n")

    while True:
        keyword = input("Cari barang (nama/merek) : ")
        if keyword.lower() == "selesai":
            break

        hasil = cari_barang(keyword)

        if not hasil:
            print("[!] Barang tidak ditemukan\n")
            continue

        print("\n Hasil Pencarian : ")
        print(f"{'Kode':^5} |  {'Nama':^10} | {'Merek':^10} | {'Harga':^12} | {'Stok':^5}")
        print("-" * 50)

        for h in hasil:
            print(f"{h[0]:<5} | {h[1]:<10} | {h[2]:<10} | {h[3]:<12} | {h[4]:^3}")

        try:
            kode = int(input("\nMasukkan kode barang : "))
            qty = int(input("Masukkan jumlah : "))

            if qty <= 0 :
                print("[!] Qty harus lebih dari 0\n")
                continue

            found = False
            for item in list_barang:
                if item['kode'] == kode:
                    item['qty'] += qty
                    found = True
                    break

            if not found:
                list_barang.append({
                    "kode" : kode,
                    "qty" : qty
                })

            print("[OK] Barang berhasil di simpan\n")

        except:
            print("[!] Input tidak valid \n")

    # Checkout
    if not list_barang:
        print("Tidak ada transaksi")
        return

    print("\n========= KERANJANG =========")
    print(f"{'kode':^5} | {'qty':^5}")
    print("-" * 20)

    for item in list_barang:
        print(f"{item['kode']:<5} | {item['qty']:<5}")

    hasil = proses_transaksi(list_barang)

    if not hasil:
        return

    total = hasil['total']
    print(f"\n Total : Rp {total:,}")

    # Pembayaran
    while True:
        try:
            uang = int(input("Masukkan jumlah uang : "))
            if uang < total:
                print("[!] Uang Kurang")
            else:
                kembalian = uang - total
                print(f"Kembalian: Rp {kembalian:,}")
                break
        except:
            print("[!] Input tidak valid")

if __name__ == "__main__":
    menu_kasir()