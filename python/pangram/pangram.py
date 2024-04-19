def is_pangram(sentence: str) -> bool:
    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())
