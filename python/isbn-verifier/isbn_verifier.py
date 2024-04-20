def is_valid(isbn: str) -> bool:
    new_isbn: str = isbn.replace("-", "")
    if (len(new_isbn) != 10):
        return False
    result = 0
    for index, value in enumerate(new_isbn):
        if (not value.isnumeric() and value != "X") or (value == "X" and index != 9):
            return False
        result += (len(new_isbn)-index) * (int(value) if value.isnumeric() else 10)
    return result % 11 == 0
