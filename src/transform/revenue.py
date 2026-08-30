def calculate_revenue(records: list) -> tuple:
    return tuple(
        {**record, "revenue": record["price"] * record["quantity"]}
        for record in records
    )