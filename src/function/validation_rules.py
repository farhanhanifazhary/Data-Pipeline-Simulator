from typing import Any, Tuple, Union

def is_required(val) -> bool:
    """Check if val is defined"""
    return val is not None and str(val).strip != ""

def is_integer(val) -> Tuple[bool, Union[int, Any]]:
    """Check if val is an int"""
    try:
        float(val)
        if val.is_integer():
            return True, int(val)
        return False, val
    except (ValueError, TypeError):
        return False, val

def is_float(val) -> Tuple[bool, Union[float, Any]]:
    """Check if val is a float"""
    try:
        converted = float(val)
        return True, converted
    except (ValueError, TypeError):
        return False, val

def is_positive(val) -> bool:
    """Check if val is positive"""
    try:
        return float(val) > 0
    except (ValueError, TypeError):
        return False

"""Buat fungsi validasi utnuk transaction_id, user_id, dan status (enum)"""
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