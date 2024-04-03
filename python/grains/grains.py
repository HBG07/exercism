def square(number):
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    if (number == 1):
        return 1
    return square(number-1)*2


def total() -> int:
    total = 0
    for i in range(1, 65):
        total += square(i)
    return total
