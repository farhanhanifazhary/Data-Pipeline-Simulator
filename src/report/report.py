from collections.abc import Mapping

from function.report_function import (
    get_revenue_by_category,
    get_revenue_by_item,
    get_revenue_by_transaction,
    get_revenue_by_user,
    get_total_items,
    get_total_items_by_category,
    get_total_items_by_item,
    get_total_items_by_transaction,
    get_total_items_by_user,
    get_total_revenue,
    get_total_transactions,
    get_total_transactions_by_category,
    get_total_transactions_by_item,
    get_total_transactions_by_transaction,
    get_total_transactions_by_user,
)


def _format_number(value: int | float, currency: bool = False) -> str:
    if currency:
        return f"Rp{value:,.0f}".replace(",", ".")
    return f"{value:,.0f}".replace(",", ".")


def _print_table(title: str, data: Mapping[str, int | float], value_label: str, currency: bool = False) -> None:
    """Mencetak tabel sederhana tanpa library eksternal."""
    rows = [(key, _format_number(value, currency)) for key, value in sorted(data.items())]
    key_width = max(len("Kelompok"), *(len(key) for key, _ in rows))
    value_width = max(len(value_label), *(len(value) for _, value in rows))
    border = f"+-{'-' * key_width}-+-{'-' * value_width}-+"

    print(f"\n{title}")
    print(border)
    print(f"| {'Kelompok':<{key_width}} | {value_label:>{value_width}} |")
    print(border)
    for key, value in rows:
        print(f"| {key:<{key_width}} | {value:>{value_width}} |")
    print(border)


def display_report(records: list[dict]) -> None:
    """Menampilkan seluruh agregasi laporan transaksi ke terminal."""
    print("=" * 52)
    print("                 LAPORAN TRANSAKSI")
    print("=" * 52)
    print(f"Total transaksi : {_format_number(get_total_transactions(records))}")
    print(f"Total item      : {_format_number(get_total_items(records))}")
    print(f"Total revenue   : {_format_number(get_total_revenue(records), currency=True)}")

    aggregations = (
        ("Revenue per Transaksi", get_revenue_by_transaction(records), "Revenue", True),
        ("Revenue per User", get_revenue_by_user(records), "Revenue", True),
        ("Revenue per Kategori", get_revenue_by_category(records), "Revenue", True),
        ("Revenue per Item", get_revenue_by_item(records), "Revenue", True),
        ("Total Transaksi per Transaksi", get_total_transactions_by_transaction(records), "Transaksi", False),
        ("Total Transaksi per User", get_total_transactions_by_user(records), "Transaksi", False),
        ("Total Transaksi per Kategori", get_total_transactions_by_category(records), "Transaksi", False),
        ("Total Transaksi per Item", get_total_transactions_by_item(records), "Transaksi", False),
        ("Total Item per Transaksi", get_total_items_by_transaction(records), "Item", False),
        ("Total Item per User", get_total_items_by_user(records), "Item", False),
        ("Total Item per Kategori", get_total_items_by_category(records), "Item", False),
        ("Total Item per Item", get_total_items_by_item(records), "Item", False),
    )

    for title, data, value_label, currency in aggregations:
        _print_table(title, data, value_label, currency)
