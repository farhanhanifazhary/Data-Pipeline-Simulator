import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from function.validation_rules import *

SCHEMA = {
    "transaction_id": [
        ("Missing transaction_id", is_required),
        ("Invalid transaction_id", is_valid_transaction_id)
    ],
    "user_id": [
        ("Missing user_id", is_required),
        ("Invalid user_id", is_valid_user_id)
    ],
    "product": [
        ("Missing product", is_required)
    ],
    "category": [
        ("Missing category", is_required)
    ],
    "price": [
        ("Missing price", is_required),
        ("Price must be positive", is_positive),
        ("Price can't be a decimal", is_integer)
    ],
    "quantity": [
        ("Missing quantity", is_required),
        ("quantity must be positive", is_positive)
    ],
    "status": [
        ("Missing status", is_required),
        ("Invalid status", is_valid_status)
    ]
}