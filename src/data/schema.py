from typing import Any, Callable, Dict, List, Tuple
from ..function.validation_rules import *

SCHEMA: Dict[str, List[Tuple[str, Callable[[Any], bool]]]] = {
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