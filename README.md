# Mini Project: Data Pipeline Simulator

Simulasi sederhana *data pipeline* untuk memproses data transaksi menggunakan **pure Python**. Proyek ini memakai data dummy sebagai sumber data dan dirancang untuk menggambarkan alur pemrosesan data dari pengambilan hingga pelaporan.

## Alur Pipeline

```text
Ingestion → Validation → Cleaning → Transformation → Aggregation → Reporting
```

| Tahap | Tujuan |
| --- | --- |
| **Ingestion** | Mengambil data transaksi dari sumber data. |
| **Validation** | Memastikan data tidak kosong dan struktur kolomnya sesuai. |
| **Cleaning** | Menangani data yang tidak valid atau tidak konsisten. |
| **Transformation** | Menyiapkan data agar siap digunakan untuk kebutuhan analisis. |
| **Aggregation** | Menghitung ringkasan data, misalnya berdasarkan kategori atau status. |
| **Reporting** | Menyajikan hasil akhir pemrosesan data. |

## Struktur Proyek

```text
.
├── README.md
└── src/
    ├── data/
    │   └── raw_data.json
    ├── main.py
    └── extract/
        └── extract.py
```

## Data Input

Data transaksi dummy disimpan dalam format JSON di [`src/data/raw_data.json`](src/data/raw_data.json), lalu dimuat oleh [`src/extract/extract.py`](src/extract/extract.py). Setiap transaksi memiliki kolom berikut:

| Kolom | Keterangan |
| --- | --- |
| `transaction_id` | ID unik transaksi. |
| `user_id` | ID pengguna yang melakukan transaksi. |
| `product` | Nama produk. |
| `category` | Kategori produk. |
| `price` | Harga satuan produk. |
| `quantity` | Jumlah produk yang dibeli. |
| `status` | Status transaksi, misalnya `completed`, `pending`, atau `cancelled`. |

> Data dummy juga mencakup beberapa data tidak valid, seperti harga atau jumlah negatif, untuk kebutuhan pengujian tahap validasi dan pembersihan data.

## Tahapan Implementasi

### 1. Extract

Membaca data dari `raw_data.json` menggunakan modul bawaan `json`, lalu memastikan data berupa daftar dan tidak kosong. Data yang berhasil dimuat tersedia melalui variabel `raw_transactions` atau fungsi `load_raw_transactions()`.

### 2. Transform

Melakukan validasi, pembersihan data, transformasi, serta agregasi hingga data siap disimpan atau digunakan untuk pelaporan.

### 3. Load

Menyimpan data hasil pemrosesan ke *data warehouse* atau media penyimpanan tujuan.

## Teknologi

- Python
- Tanpa *library* eksternal (*pure Python*)
