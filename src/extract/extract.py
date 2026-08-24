def extract_data(*sources: list):
    for source in sources:
        yield from source