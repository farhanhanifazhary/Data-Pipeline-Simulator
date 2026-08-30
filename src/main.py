from data.dataset import raw_transactions
from extract.extract import extract_data
from transform.validation import get_validation_result
from transform.revenue import calculate_revenue
from report.report import display_report


def main():
    if not isinstance(raw_transactions, list):
        raise TypeError("Tipe data bukan list")

    result = list(extract_data(raw_transactions))
    valid_records, invalid_records = get_validation_result(result)

    transformed_data = calculate_revenue(valid_records)

    display_report(transformed_data)

if __name__ == "__main__":
    main()