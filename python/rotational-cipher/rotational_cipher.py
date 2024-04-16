alphabet = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    new_text: list[str] = list(text)

    for i, x in enumerate(new_text):
        if (x.islower()):
            new_text[i] = alphabet[(alphabet.index(x) + key) % len(alphabet)]
        elif (x.isupper()):
            new_text[i] = alphabet[(alphabet.index(x.lower()) + key) % len(alphabet)].upper()
    return "".join(new_text)
