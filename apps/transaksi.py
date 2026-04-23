from koneksi import konek_db

def barang_masuk(kode, jml):
    conn = konek_db()
    cursor = conn.cursor()
    sql = "UPDATE barang SET jml = jml + %s WHERE kode = %s"
    cursor.execute(sql, (jml, kode))
    conn.commit()
    print("\n [OK] Stok Berhasil Ditambahkan")
    conn.close()

def barang_keluar(kode, jml):
    conn = konek_db()
    cursor = conn.cursor()
    # Cek Stok Saat Ini
    cursor.execute("SELECT nama, jml FROM barang WHERE kode = %s", (kode,))
    data = cursor.fetchone() #Mengambil 1 baris data saja dari hasil query

    if data:
        nama, jml_skrg = data
        if jml_skrg < jml:
            print(f"\n [!] GAGAL: Jumlah {nama} tidak cukup. Sisa {jml_skrg}")
        else:
            # Update jumlah dan tgl_keluar
            sql="UPDATE barang SET jml = jml - %s, tgl_keluar = CURDATE() WHERE kode = %s"
            cursor.execute(sql, (jml, kode))
            conn.commit()

            jml_akhir = jml_skrg - jml
            print(f"\n [OK] Berhasil Transaksi {jml} {nama}")

            # Peringatan Stok Menipis
            if jml_akhir < 10:
                print(f"\n [!] Jumlah {nama} menipis!. Sisa {jml_akhir}")

    else:
        print("\n [!] Kode Barang Tidak Ditemukan")
    conn.close()