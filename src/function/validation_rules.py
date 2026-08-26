def is_required(val) -> bool:
    """Check if val is defined"""
    return val is not None and str(val).strip != ""

def is_integer(val) -> bool:
    """Check if val is an int"""
    try:
        if val.is_integer():
            int(val)
            return True
        return False
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

"""Buat fungsi validasi utnuk transaction_id, user_id, dan status (enum)"""
def is_valid_transaction_id(val: str) -> bool:
    """Check a valid transaction_id"""
    if not val.startswith("TRX"):
        raise "A valid transaction_id must start with TRX"
    if not val[3:].isdigit():
        raise "A valid transaction_id must end with digit"
    return True

def is_valid_user_id(val: str) -> bool:
    """Check a valid user_id"""
    if not val.startswith("USR"):
        raise "A valid user_id must start with USR"
    if not val[3:].isdigit():
        raise "A valid user_id must end with digit"
"""Membuat parse untuk integer dan float seperti di bawah"""

"""from typing import Any, Tuple, Union

def parse_integer(val: Any) -> Tuple[bool, Union[int, Any]]:
    try:
        # Menangani tipe float terlebih dahulu
        if isinstance(val, float):
            if val.is_integer():
                return True, int(val)
            return False, val
        
        # Menangani string atau int langsung
        parsed = float(val)
        if parsed.is_integer():
            return True, int(parsed)
        return False, val
    except (ValueError, TypeError):
        return False, val


def parse_float(val: Any) -> Tuple[bool, Union[float, Any]]:
    try:
        # Konversi int, float, atau string angka ke float
        converted = float(val)
        return True, converted
    except (ValueError, TypeError):
        return False, val"""