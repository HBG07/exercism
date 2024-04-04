def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not is_triangle(sides)):
        return False
    return a == b and b == c


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not is_triangle(sides)):
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not is_triangle(sides)):
        return False
    return a != b and b != c and a != c


def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a+b > c and a+c > b and b+c > a
