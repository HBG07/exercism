from curses.ascii import isupper


def response(hey_bob: str) -> str:
    question: bool = hey_bob.strip().endswith("?")
    yell: bool = hey_bob.isupper()
    white_space: bool = hey_bob.isspace() or hey_bob == ""

    if question and yell:
        return "Calm down, I know what I'm doing!"
    elif yell:
        return "Whoa, chill out!"
    elif question:
        return "Sure."
    elif white_space:
        return "Fine. Be that way!"
    else:
        return "Whatever."
