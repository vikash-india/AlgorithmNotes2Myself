import logging

"""
Note
1. A simple and intuitive technique which is fast as well.
2. Optimisation(s)
    - None
3. Limitation(s)
    - None
"""

def answer(upper_bound):
    a, b = 1, 1
    result = 0
    while b < upper_bound:
        a, b = b, b + a
        if b % 2 == 0:
            result += b
    return result
