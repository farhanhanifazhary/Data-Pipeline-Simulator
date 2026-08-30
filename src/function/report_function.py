from collections import Counter
from collections.abc import Iterable, Mapping


Record = Mapping[str, object]


def _sum_by(records: Iterable[Record], key: str, value_key: str) -> dict[str, int | float]:
    """Menjumlahkan ``value_key`` untuk setiap nilai ``key``."""
    result = Counter()
    for record in records:
        result[str(record[key])] += record[value_key]
    return dict(result)


def _count_by(records: Iterable[Record], key: str) -> dict[str, int]:
    """Menghitung banyaknya baris transaksi untuk setiap nilai ``key``."""
    return dict(Counter(str(record[key]) for record in records))


def get_total_revenue(records: Iterable[Record]) -> int | float:
    """Menghitung total revenue dari seluruh transaksi."""
    return sum(record["revenue"] for record in records)


def get_revenue_by_transaction(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "transaction_id", "revenue")


def get_revenue_by_user(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "user_id", "revenue")


def get_revenue_by_category(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "category", "revenue")


def get_revenue_by_item(records: Iterable[Record]) -> dict[str, int | float]:
    """Menghitung revenue berdasarkan nama produk."""
    return _sum_by(records, "product", "revenue")


def get_total_transactions(records: Iterable[Record]) -> int:
    """Menghitung jumlah seluruh transaksi (baris record)."""
    return sum(1 for _ in records)


def get_total_transactions_by_transaction(records: Iterable[Record]) -> dict[str, int]:
    return _count_by(records, "transaction_id")


def get_total_transactions_by_user(records: Iterable[Record]) -> dict[str, int]:
    return _count_by(records, "user_id")


def get_total_transactions_by_category(records: Iterable[Record]) -> dict[str, int]:
    return _count_by(records, "category")


def get_total_transactions_by_item(records: Iterable[Record]) -> dict[str, int]:
    return _count_by(records, "product")


def get_total_items(records: Iterable[Record]) -> int | float:
    """Menghitung total unit item dari seluruh transaksi."""
    return sum(record["quantity"] for record in records)


def get_total_items_by_transaction(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "transaction_id", "quantity")


def get_total_items_by_user(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "user_id", "quantity")


def get_total_items_by_category(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "category", "quantity")


def get_total_items_by_item(records: Iterable[Record]) -> dict[str, int | float]:
    return _sum_by(records, "product", "quantity")
