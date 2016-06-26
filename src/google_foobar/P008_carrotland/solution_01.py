import logging
from fractions import gcd

"""
Note
1. Optimisation(s)
    - None
2. Limitation(s)
    - None
"""


def answer(vertices):
    x1, y1 = vertices[0][0], vertices[0][1]
    x2, y2 = vertices[1][0], vertices[1][1]
    x3, y3 = vertices[2][0], vertices[2][1]

    # Area of triangle using Heron's formula
    area = .5 * abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1))

    # Number of integer points on the boundaries
    boundary = gcd(abs(x1 - x2), abs(y1 - y2)) + gcd(abs(x2 - x3), abs(y2 - y3)) + gcd(abs(x3 - x1), abs(y3 - y1))

    # Number of integer points inside the triangle using Pick's theorem
    interior_points = area - boundary / 2 + 1

    return int(interior_points)
