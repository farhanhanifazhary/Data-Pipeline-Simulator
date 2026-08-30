import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.schema import SCHEMA

def validate_records(record_stream: dict, schema: dict = SCHEMA) -> list:
    """Memvalidasi data yang transaksi"""
    return [
        error_msg
        for field, rules in schema.items()
        for error_msg, rule in rules
        if not rule(record_stream.get(field))
    ]

def process_validation(data: list):
    """Memproses validasi"""
    for record in data:
        errors = validate_records(record)
        if errors:
            record["errors"] = errors
            yield False, record
        else:
            yield True, record

def get_validation_result(data: list) -> list:
    """Mengambil hasil validasi"""
    valid_records = []
    invalid_records = []

    for status, record in process_validation(data):
        if status:
            valid_records.append(record)
        else:
            invalid_records.append(record)

    return valid_records, invalid_records