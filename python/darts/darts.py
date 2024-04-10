import math
from typing import Literal


def score(x, y) -> Literal[10, 5, 1, 0]:
    r: float = math.sqrt(x ** 2 + y ** 2)
    if r <= 1:
        return 10
    elif r <= 5:
        return 5
    elif r <= 10:
        return 1
    else:
        return 0
