CREATE DATABASE IF NOT EXISTS gudang_db;
USE gudang_db;

CREATE TABLE barang (
    kode INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    merek VARCHAR(50),
    harga DECIMAL(15,2),
    jml INT DEFAULT 0,
    tgl_masuk DATE DEFAULT (CURRENT_DATE),
    tgl_keluar DATE
);