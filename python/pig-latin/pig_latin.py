def translate(text: str) -> str:
    words: list[str] = text.split()
    words_transform = list(map(transform_words, words))
    return " ".join(words_transform)


def transform_words(text: str) -> str:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    start_vowels: bool = text[0] in vowels or text.startswith(
        "xr") or text.startswith("yt")
    str_add = "ay"

    if not start_vowels:
        if(text[0] == "y"):
            text = text[1:] + text[0:1]
        while not start_vowels and text[0] != "y":
            if (text[0:2] == "qu"):
                text = text[2:] + text[0:2]
            elif text[0] not in vowels:
                text = text[1:] + text[0:1]
            else:
                break

    return text+str_add
