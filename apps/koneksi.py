import mysql.connector
from mysql.connector import errorcode

def konek_db():
    try:
      conn = mysql.connector.connect(user="root", password="000888rafa",host="localhost",database="manajemen_gudang"
                                          ,port=3307)
      return conn

    except mysql.connector.Error as gagal:
        if gagal.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Gagal koneksi Database. Kesalahan mungkin pada username dan password")
        elif gagal.errno == errorcode.ER_BAD_DB_ERROR:
            print("Gagal koneksi Database. Nama Database tidak ditemukan")
        else:
            print(f"Gagal koneksi Database karena {gagal}")
        return None