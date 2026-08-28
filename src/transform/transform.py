from ..data.schema import SCHEMA

def validate_records(record_stream: list, schema: dict = SCHEMA):
    """Memvalidasi data yang transaksi"""

def process_validation(data: list):
    for record in data:
        errors = validate_records(data)
        if errors:
            record["errors"] = errors
            yield False, record
        else:
            yield True, record

def get_validation_result(data: list):
    valid_records = []
    invalid_records = []

    for status, record in process_validation(data):
        if status:
            valid_records.append(record)
        else:
            invalid_records.append(record)

    return valid_records, invalid_records