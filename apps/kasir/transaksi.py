from typing import final

from core.koneksi import konek_db

def proses_transaksi(list_barang):
    conn = konek_db()
    cursor = conn.cursor()
    try:
        # 1. Validasi Input
        if not list_barang :
            raise ValueError ("Daftar barang tidak boleh kosong")

        for item in list_barang:
            if 'kode' not in item or 'qty' not in item:
                raise Exception("Format item tidak valid")
            if item['qty'] <= 0:
                raise Exception("Barang tidak boleh 0 atau negatif")

        # Validasi DB & Hitung Total
        total = 0

        for item in list_barang:
            kode = item['kode']
            qty = item['qty']

            cursor.execute("SELECT harga, stok FROM barang WHERE kode = %s", (kode,))
            data = cursor.fetchone()

            if not data:
                raise Exception(f"Barang dengan kode {kode} tidak ditemukan")

            harga, stok = data

            if stok < qty:
                raise Exception(f"Stok barang {kode} tidak cukup")

            total += harga * qty

        # 3. Insert Transaksi
        cursor.execute("INSERT INTO transaksi (tgl, total) VALUES (NOW(), %s)", (total, ))
        id_transaksi = cursor.lastrowid

        # 4. Loop Detail + Update Stok
        for item in list_barang:
            kode = item['kode']
            qty = item['qty']
            cursor.execute("SELECT harga FROM barang WHERE kode = %s",(kode,))
            harga = cursor.fetchone()[0]

            # Insert Detail
            cursor.execute("INSERT INTO detail_transaksi (id_transaksi, kode_barang, qty, harga) VALUES (%s, %s, %s, %s)",
                           (id_transaksi, kode, qty, harga))

            # Update Stok
            cursor.execute("UPDATE barang SET stok = stok - %s WHERE kode = %s AND stok >= %s",
                           (qty, kode, qty))

            if cursor.rowcount == 0:
                raise Exception(f"Stok tidak cukup saat update untuk {kode}")

        conn.commit()
        print("Transaksi Berhasil!")
        print(f"ID Transaksi : {id_transaksi}")
        print(f"Total : {total}")

        return {
            "id_transaksi" : id_transaksi,
            "total" : total
        }

    except Exception as e:
        conn.rollback()
        print("Transaksi Gagal : ", e)
        return None

    finally:
        conn.close()