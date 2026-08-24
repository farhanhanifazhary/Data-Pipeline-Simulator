from data.dataset import raw_transactions
from extract.extract import extract_data

def main():
    if not isinstance(raw_transactions, list):
        raise TypeError("Tipe data bukan list")

    result = list(extract_data(raw_transactions))

if __name__ == "__main__":
    main()