from koneksi import konek_db

# CREATE
def tambah_barang(nama,merek,harga,jml):
    conn = konek_db()
    cursor = conn.cursor()
    # %s diibaratkan sebagai tempat kosong dari kolom yg nantinya akan diisi
    sql = "INSERT INTO barang (nama,merek,harga,jml) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql,(nama, merek, harga, jml))
    conn.commit() # data benar-benar tersimpan
    print(f"\n [OK] Barang {nama} Berhasil Disimpan!")
    conn.close()

# READ
def baca_barang():
    conn = konek_db()
    cursor = conn.cursor()
    cursor.execute("SELECT kode, nama, merek, harga, jml, tgl_masuk, tgl_keluar FROM barang")
    results = cursor.fetchall() #mengambil semua query dari database. WAJIB ada untuk select

    # TAMPILAN CLI
    print("=" *90)
    # Catatan format f-string yaitu (< : rata kiri) (> : rata kanan) (^ : rata tengah)
    print(f"{'KODE':^3} | {'NAMA':^15} | {'MEREK':^15} | {'HARGA':^10} | {'JML':^3} | {'TGL_MASUK'} | {'TGL_KELUAR'}") # HEADER TABLE
    print("-" *90)

    # for ini mengulang setiap data dari hasil fetchall(), sehingga semua data ditampilkan satu per satu sampai habis.
    for i in results: # ambil 1 baris data dan simpan ke variabel 'i' ulang sampai habis
        tgl_k = i[6] if i[6] else "-" # i[6] = kolom ke 7 karena dihitung mulai dari 0. Artinya jika kolom tgl_keluar kosong isi dengan '-'
        print(f"{i[0]:^3} | {i[1]:^15} | {i[2]:^15} | {i[3]:^10,.0f} | {i[4]:^3} | {i[5]} | {tgl_k}") #Bentuk barisnya agar sesuai dengan header table
    print("=" *90)
    conn.close()

# DELETE
def hapus_barang(kode):
    conn = konek_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM barang WHERE kode = %s", (kode,))
    conn.commit()
    print(f"\n [OK] Data Kode {kode} Berhasil Dihapus!")
    conn.close()