def is_required(val) -> bool:
    """Check if val is defined"""
    return val is not None and str(val).strip != ""

def is_integer(val) -> bool:
    try:
        int(val)
        return True
    except (ValueError, TypeError):
        return False

def is_float(val) -> bool:
    """Check if val is a float"""
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False

def is_positive(val) -> bool:
    """Check if val is positive"""
    try:
        return float(val) > 0
    except (ValueError, TypeError):
        return False

def is_valid_transaction_id(val: str) -> bool:
    """Check a valid transaction_id"""
    if not val.startswith("TRX"):
        return False
    if not val[3:].isdigit():
        return False
    return True

def is_valid_user_id(val: str) -> bool:
    """Check a valid user_id"""
    if not val.startswith("USR"):
        return False
    if not val[3:].isdigit():
        return False
    return True

def drop_duplicates(data: list) -> list:
    """drop duplicates data"""
    seen = set()
    hasil = []

    for item in data:
        item_set = tuple(item.items())
        if item_set not in seen:
            seen.add(item_set)
            hasil.append(item)

def is_valid_status(val) -> bool:
    """check if status valid"""
    list_status = ["completed", "pending", "cancelled"]
    if val not in list_status:
        return False
    return True