from typing import Literal


def classify(number) -> None | Literal['perfect', 'deficient', 'abundant']:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if (number < 1):
        raise ValueError(
            "Classification is only possible for positive integers.")

    sum_number: int = sum_perfect_number(number)

    if number == sum_number:
        return "perfect"
    elif number > sum_number or sum_number == 1:
        return "deficient"
    elif number < sum_number:
        return "abundant"


def sum_perfect_number(number) -> int:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: bool
    """
    return sum(divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0)
