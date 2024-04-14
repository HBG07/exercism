from re import split


def is_isogram(string: str) -> bool:
    new_str: str = ''.join(split(r"[\s-]", string)).lower()
    return len(new_str) == len(set(new_str))
