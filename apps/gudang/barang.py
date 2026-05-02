from core.koneksi import konek_db

# CREATE
def tambah_barang(nama,merek,harga,stok):
    conn = konek_db()
    cursor = conn.cursor()
    # %s diibaratkan sebagai tempat kosong dari kolom yg nantinya akan diisi
    sql = "INSERT INTO barang (nama,merek,harga,stok) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql,(nama, merek, harga, stok))
    conn.commit() # data benar-benar tersimpan
    print(f"\n [OK] Barang {nama} Berhasil Disimpan!")
    conn.close()

# READ
def baca_barang():
    conn = konek_db()
    cursor = conn.cursor()
    cursor.execute("SELECT kode, nama, merek, harga, stok, tgl_masuk FROM barang")
    results = cursor.fetchall() #mengambil semua query dari database. WAJIB ada untuk select

    # TAMPILAN CLI
    print("=" *90)
    # Catatan format f-string yaitu (< : rata kiri) (> : rata kanan) (^ : rata tengah)
    print(f"{'KODE':^3} | {'NAMA':^15} | {'MEREK':^15} | {'HARGA':^10} | {'STOK':^3} | {'TGL_MASUK'}") # HEADER TABLE
    print("-" *90)

    # for ini mengulang setiap data dari hasil fetchall(), sehingga semua data ditampilkan satu per satu sampai habis.
    for i in results: # ambil 1 baris data dan simpan ke variabel 'i' ulang sampai habis
        print(f"{i[0]:^3} | {i[1]:^15} | {i[2]:^15} | {i[3]:^10,.0f} | {i[4]:^3} | {i[5]}") #Bentuk barisnya agar sesuai dengan header table
    print("=" *90)
    conn.close()

# UPDATE
def barang_masuk(kode, stok):
    conn = konek_db()
    cursor = conn.cursor()
    sql = "UPDATE barang SET stok = stok + %s WHERE kode = %s"
    cursor.execute(sql, (stok, kode))
    conn.commit()
    print("\n [OK] Stok Berhasil Ditambahkan")
    conn.close()

# DELETE
def hapus_barang(kode):
    conn = konek_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM barang WHERE kode = %s", (kode,))
    conn.commit()
    print(f"\n [OK] Data Kode {kode} Berhasil Dihapus!")
    conn.close()