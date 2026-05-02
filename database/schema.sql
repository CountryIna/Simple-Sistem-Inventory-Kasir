CREATE DATABASE IF NOT EXISTS gudang_db;
USE gudang_db;

CREATE TABLE barang (
    kode INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    merek VARCHAR(50),
    harga INT DEFAULT 0,
    stok INT DEFAULT 0,
    tgl_masuk DATE DEFAULT CURRENT_DATE
);

CREATE TABLE transaksi (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    tgl DATE DEFAULT CURRENT_DATE,
    total INT DEFAULT 0
);

CREATE TABLE detail_transaksi (
    id_detail INT AUTO_INCREMENT PRIMARY KEY,
    id_transaksi INT,
    kode_barang INT,
    harga INT DEFAULT 0,
    qty INT DEFAULT 0,

    FOREIGN KEY (id_transaksi) REFERENCES transaksi(id_transaksi),
    FOREIGN KEY (kode_barang) REFERENCES barang(kode)
);