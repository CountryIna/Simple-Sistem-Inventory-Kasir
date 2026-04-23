import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

def konek_db():
    try:
        conn = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )
        return conn

    except mysql.connector.Error as gagal:
        if gagal.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Gagal koneksi Database. Kesalahan mungkin pada username dan password")
        elif gagal.errno == errorcode.ER_BAD_DB_ERROR:
            print("Gagal koneksi Database. Nama Database tidak ditemukan")
        else:
            print(f"Gagal koneksi Database karena {gagal}")
        return None