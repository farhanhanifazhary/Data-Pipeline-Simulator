from typing import Any, Tuple, Union

raw_transactions = [
    {
        "transaction_id": "TRX001",
        "user_id": "USR001",
        "product": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 850000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX002",
        "user_id": "USR002",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "price": 350000,
        "quantity": 2,
        "status": "completed",
    },
    {
        "transaction_id": "TRX003",
        "user_id": "USR003",
        "product": "Python Book",
        "category": "Books",
        "price": 175000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX004",
        "user_id": "USR004",
        "product": "Notebook",
        "category": "Stationery",
        "price": 45000,
        "quantity": 5,
        "status": "completed",
    },
    {
        "transaction_id": "TRX005",
        "user_id": "USR005",
        "product": "Running Shoes",
        "category": "Sports",
        "price": 950000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX006",
        "user_id": "USR006",
        "product": "Coffee Beans",
        "category": "Food",
        "price": 125000,
        "quantity": 3,
        "status": "completed",
    },
    {
        "transaction_id": "TRX007",
        "user_id": "USR007",
        "product": "USB-C Hub",
        "category": "Electronics",
        "price": 275000,
        "quantity": 1,
        "status": "pending",
    },
    {
        "transaction_id": "TRX008",
        "user_id": "USR008",
        "product": "Data Engineering Book",
        "category": "Books",
        "price": 225000,
        "quantity": 2,
        "status": "completed",
    },
    {
        "transaction_id": "TRX009",
        "user_id": "USR009",
        "product": "Pen Set",
        "category": "Stationery",
        "price": 30000,
        "quantity": 4,
        "status": "completed",
    },
    {
        "transaction_id": "TRX010",
        "user_id": "USR010",
        "product": "Yoga Mat",
        "category": "Sports",
        "price": 275000,
        "quantity": 1,
        "status": "cancelled",
    },
    {
        "transaction_id": "TRX011",
        "user_id": "USR001",
        "product": "Monitor 24 inch",
        "category": "Electronics",
        "price": 1850000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX012",
        "user_id": "USR002",
        "product": "Green Tea",
        "category": "Food",
        "price": 85000,
        "quantity": 2,
        "status": "completed",
    },
    {
        "transaction_id": "TRX013",
        "user_id": "USR003",
        "product": "Clean Code",
        "category": "Books",
        "price": 320000,
        "quantity": 1,
        "status": "pending",
    },
    {
        "transaction_id": "TRX014",
        "user_id": "USR004",
        "product": "Desk Organizer",
        "category": "Stationery",
        "price": 75000,
        "quantity": 2,
        "status": "completed",
    },
    {
        "transaction_id": "TRX015",
        "user_id": "USR005",
        "product": "Dumbbell Set",
        "category": "Sports",
        "price": 650000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX016",
        "user_id": "USR006",
        "product": "Chocolate",
        "category": "Food",
        "price": 55000,
        "quantity": 6,
        "status": "completed",
    },
    {
        "transaction_id": "TRX017",
        "user_id": "USR007",
        "product": "Laptop Stand",
        "category": "Electronics",
        "price": 425000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX018",
        "user_id": "USR008",
        "product": "Algorithms Book",
        "category": "Books",
        "price": 280000,
        "quantity": 1,
        "status": "cancelled",
    },
    {
        "transaction_id": "TRX019",
        "user_id": "USR009",
        "product": "Sticky Notes",
        "category": "Stationery",
        "price": 25000,
        "quantity": 8,
        "status": "completed",
    },
    {
        "transaction_id": "TRX020",
        "user_id": "USR010",
        "product": "Resistance Band",
        "category": "Sports",
        "price": 120000,
        "quantity": 2,
        "status": "pending",
    },
    {
        "transaction_id": "TRX021",
        "user_id": "USR001",
        "product": "Protein Bar",
        "category": "Food",
        "price": 35000,
        "quantity": 10,
        "status": "completed",
    },
    {
        "transaction_id": "TRX022",
        "user_id": "USR002",
        "product": "Webcam",
        "category": "Electronics",
        "price": 725000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX023",
        "user_id": "USR003",
        "product": "Python Cookbook",
        "category": "Books",
        "price": 375000,
        "quantity": 1,
        "status": "completed",
    },
    {
        "transaction_id": "TRX024",
        "user_id": "USR004",
        "product": "Planner",
        "category": "Stationery",
        "price": 95000,
        "quantity": 2,
        "status": "completed",
    },
    {
        "transaction_id": "TRX025",
        "user_id": "USR005",
        "product": "Tennis Racket",
        "category": "Sports",
        "price": 1250000,
        "quantity": 1,
        "status": "completed",
    },

    # Invalid: negative price
    {
        "transaction_id": "TRX026",
        "user_id": "USR006",
        "product": "Coffee Beans",
        "category": "Food",
        "price": -125000,
        "quantity": 2,
        "status": "completed",
    },

    # Invalid: zero quantity
    {
        "transaction_id": "TRX027",
        "user_id": "USR007",
        "product": "USB Cable",
        "category": "Electronics",
        "price": 100000,
        "quantity": 0,
        "status": "completed",
    },

    # Invalid: negative quantity
    {
        "transaction_id": "TRX028",
        "user_id": "USR008",
        "product": "Notebook",
        "category": "Stationery",
        "price": 50000,
        "quantity": -3,
        "status": "completed",
    },

    # Invalid: unknown status
    {
        "transaction_id": "TRX029",
        "user_id": "USR009",
        "product": "Basketball",
        "category": "Sports",
        "price": 450000,
        "quantity": 1,
        "status": "refunded",
    },

    # Invalid: wrong price type
    {
        "transaction_id": "TRX030",
        "user_id": "USR010",
        "product": "Keyboard",
        "category": "Electronics",
        "price": "750000",
        "quantity": 1,
        "status": "completed",
    },

    # Invalid: missing product
    {
        "transaction_id": "TRX031",
        "user_id": "USR001",
        "category": "Books",
        "price": 250000,
        "quantity": 1,
        "status": "completed",
    },

    # Invalid: wrong quantity type
    {
        "transaction_id": "TRX032",
        "user_id": "USR002",
        "product": "Mouse Pad",
        "category": "Electronics",
        "price": 85000,
        "quantity": "two",
        "status": "completed",
    },

    # Duplicate of TRX001
    {
        "transaction_id": "TRX001",
        "user_id": "USR001",
        "product": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 850000,
        "quantity": 1,
        "status": "completed",
    },

    # Duplicate of TRX010
    {
        "transaction_id": "TRX010",
        "user_id": "USR010",
        "product": "Yoga Mat",
        "category": "Sports",
        "price": 275000,
        "quantity": 1,
        "status": "cancelled",
    },

    # Valid
    {
        "transaction_id": "TRX033",
        "user_id": "USR003",
        "product": "Eraser",
        "category": "Stationery",
        "price": 10000,
        "quantity": 10,
        "status": "completed",
    },

    # Valid
    {
        "transaction_id": "TRX034",
        "user_id": "USR006",
        "product": "Headphones",
        "category": "Electronics",
        "price": 550000,
        "quantity": 1,
        "status": "pending",
    },

    # Valid
    {
        "transaction_id": "TRX035",
        "user_id": "USR010",
        "product": "Coffee Mug",
        "category": "Food",
        "price": 75000,
        "quantity": 2,
        "status": "completed",
    },
]

def is_required(val: Any) -> bool:
    """Check if val is defined"""
    return val is not None and str(val).strip != ""

def is_integer(val: Any) -> Tuple[bool, Union[int, Any]]:
    """Check if val is an int"""
    try:
        float(val)
        if val.is_integer():
            return True, int(val)
        return False, val
    except (ValueError, TypeError):
        return False, val

def is_float(val: Any) -> Tuple[bool, Union[float, Any]]:
    """Check if val is a float"""
    try:
        converted = float(val)
        return True, converted
    except (ValueError, TypeError):
        return False, val

def is_positive(val: Any) -> bool:
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

def drop_duplicates(data: list) -> list:
    seen = set()
    hasil = []

    for item in data:
        item_set = tuple(item.items())
        if item_set not in seen:
            seen.add(item_set)
            hasil.append(item)

def is_valid_status(val, list_status) -> bool:
    if val not in list_status:
        return False
    return True