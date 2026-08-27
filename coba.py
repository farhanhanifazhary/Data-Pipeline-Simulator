from typing import Any, Callable, Dict, Iterator, List, Tuple

# 1. Definisi Rule Validasi Murni
def is_required(val: Any) -> bool:
    return val is not None and str(val).strip() != ""

def is_integer(val: Any) -> bool:
    try:
        int(val)
        return True
    except (ValueError, TypeError):
        return False

def is_email(val: Any) -> bool:
    s = str(val).strip()
    return "@" in s and "." in s.split("@")[-1] and not s.startswith("@")

def is_positive(val: Any) -> bool:
    try:
        return float(val) > 0
    except (ValueError, TypeError):
        return False


# 2. Skema Ekspektasi Data
SCHEMA: Dict[str, List[Tuple[str, Callable[[Any], bool]]]] = {
    "user_id": [
        ("Missing user_id", is_required),
        ("Invalid integer for user_id", is_integer)
    ],
    "email": [
        ("Missing email", is_required),
        ("Invalid email format", is_email)
    ],
    "amount": [
        ("Missing amount", is_required),
        ("Amount must be positive", is_positive)
    ]
}


# 3. Engine Validasi Stream / Generator
def validate_record(record: Dict[str, Any], schema: Dict) -> List[str]:
    """Memeriksa single record terhadap skema, mengembalikan list error."""
    errors = []
    for field, rules in schema.items():
        val = record.get(field)
        for error_msg, rule in rules:
            if not rule(val):
                errors.append(f"{field}: {error_msg}")
    return errors


def process_pipeline(stream: Iterator[Dict[str, Any]], schema: Dict):
    """Memisahkan data valid dan rejected tanpa load semua ke RAM."""
    valid_count = 0
    rejected_count = 0
    
    for row_idx, record in enumerate(stream, start=1):
        errors = validate_record(record, schema)
        if not errors:
            valid_count += 1
            # Kirim ke downstream sink / buffer target
            yield "VALID", record
        else:
            rejected_count += 1
            # Dead-letter queue payload
            yield "REJECTED", {"row": row_idx, "record": record, "errors": errors}


# --- Simulasi Eksekusi ---
raw_data = [
    {"user_id": "101", "email": "user@domain.com", "amount": "250.0"},
    {"user_id": "", "email": "anon@domain.com", "amount": "100"},
    {"user_id": "103", "email": "bad-email-format", "amount": "-50"},
    {"user_id": "104", "email": "test@corp.com", "amount": "invalid_num"},
]

for status, payload in process_pipeline(iter(raw_data), SCHEMA):
    print(f"[{status}] -> {payload}")