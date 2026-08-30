# Data Pipeline Transaction Report

Proyek ini adalah simulasi pipeline pemrosesan transaksi menggunakan Python murni, tanpa library pihak ketiga. Data transaksi divalidasi, dihitung nilai *revenue*-nya, lalu disajikan sebagai laporan agregasi tabel di terminal.

## Fitur

- Mengambil data transaksi dummy dari `src/data/dataset.py`.
- Memvalidasi field wajib, format ID transaksi dan user, harga, kuantitas, serta status transaksi.
- Memisahkan transaksi valid dan tidak valid; transaksi tidak valid disertai daftar error.
- Menambahkan field `revenue` dengan rumus `price × quantity` pada transaksi valid.
- Menghitung revenue, jumlah transaksi, dan jumlah item secara keseluruhan maupun per transaksi, user, kategori, dan produk.
- Menampilkan laporan tabel yang rapi di terminal dengan Python murni.

## Alur Pipeline

```text
Dataset → Extract → Validation → Revenue Transformation → Aggregation → Report
```

| Tahap | Modul | Hasil |
| --- | --- | --- |
| Dataset | `data/dataset.py` | Daftar transaksi dummy. |
| Extract | `extract/extract.py` | Stream data transaksi dari sumber. |
| Validation | `transform/validation.py` | Transaksi valid dan tidak valid. |
| Transformation | `transform/revenue.py` | Transaksi valid dengan field `revenue`. |
| Aggregation | `function/report_function.py` | Nilai-nilai agregasi laporan. |
| Reporting | `report/report.py` | Tampilan ringkasan dan tabel di terminal. |

## Struktur Proyek

```text
.
├── README.md
└── src/
    ├── main.py
    ├── data/
    │   ├── dataset.py
    │   └── schema.py
    ├── extract/
    │   └── extract.py
    ├── function/
    │   ├── report_function.py
    │   └── validation_rules.py
    ├── transform/
    │   ├── revenue.py
    │   └── validation.py
    └── report/
        └── report.py
```

## Struktur Data Transaksi

Setiap transaksi memiliki field berikut.

| Field | Keterangan |
| --- | --- |
| `transaction_id` | ID transaksi dengan format `TRX...`. |
| `user_id` | ID pengguna dengan format `USR...`. |
| `product` | Nama produk atau item. |
| `category` | Kategori produk. |
| `price` | Harga satuan berupa integer positif. |
| `quantity` | Jumlah item yang dibeli, harus bernilai positif. |
| `status` | Salah satu dari `completed`, `pending`, atau `cancelled`. |
| `revenue` | Ditambahkan setelah transformasi: `price × quantity`. |

Dataset juga sengaja memuat record tidak valid untuk menguji proses validasi, seperti harga negatif, kuantitas nol atau negatif, status tidak dikenal, dan tipe data yang salah.

## Cara Menjalankan

Pastikan Python 3.10 atau lebih baru telah terpasang, kemudian jalankan dari root proyek:

```bash
python src/main.py
```

Program akan memproses data valid dan menampilkan laporan pada terminal. Tidak ada instalasi dependensi tambahan.

## Agregasi yang Tersedia

Seluruh fungsi perhitungan berada di `src/function/report_function.py`.

| Metrik | Total | Pengelompokan |
| --- | --- | --- |
| Revenue | `get_total_revenue()` | transaksi, user, kategori, item/produk |
| Jumlah transaksi | `get_total_transactions()` | transaksi, user, kategori, item/produk |
| Jumlah item | `get_total_items()` | transaksi, user, kategori, item/produk |

Definisi metrik:

- **Jumlah transaksi** adalah jumlah record transaksi.
- **Jumlah item** adalah total nilai field `quantity`.
- **Item** pada pengelompokan berarti nama produk (`product`).
- **Revenue** dihitung dari `price × quantity`.

Fungsi pengelompokan mengikuti pola berikut:

```python
get_revenue_by_transaction(records)
get_revenue_by_user(records)
get_revenue_by_category(records)
get_revenue_by_item(records)

get_total_transactions_by_transaction(records)
get_total_transactions_by_user(records)
get_total_transactions_by_category(records)
get_total_transactions_by_item(records)

get_total_items_by_transaction(records)
get_total_items_by_user(records)
get_total_items_by_category(records)
get_total_items_by_item(records)
```

## Tampilan Laporan

`display_report()` di `src/report/report.py` hanya menangani presentasi. Fungsi ini menampilkan:

1. Ringkasan total transaksi, total item, dan total revenue.
2. Tabel revenue per transaksi, user, kategori, dan item.
3. Tabel jumlah transaksi per transaksi, user, kategori, dan item.
4. Tabel jumlah item per transaksi, user, kategori, dan item.

Nilai revenue ditampilkan dalam format Rupiah, misalnya `Rp1.700.000`.
