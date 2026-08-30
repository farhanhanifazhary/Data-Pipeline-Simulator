from data.dataset import raw_transactions
from extract.extract import extract_data
from transform.validation import get_validation_result
from transform.revenue import calculate_revenue

def main():
    if not isinstance(raw_transactions, list):
        raise TypeError("Tipe data bukan list")

    result = list(extract_data(raw_transactions))
    valid_records, invalid_records = get_validation_result(result)

    print(calculate_revenue(valid_records))

if __name__ == "__main__":
    main()