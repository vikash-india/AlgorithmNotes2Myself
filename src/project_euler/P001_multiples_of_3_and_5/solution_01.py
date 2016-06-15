import logging

"""
Note
1. Brute force technique: Loop through all the numbers, test if divisible by 3 or 5 and sum it up.
2. The first and the most intuitive solution that comes to my mind.
3. One of the slowest/worst solution possible.
4. Optimisation(s)
    - None
5. Limitation(s)
    - None
"""


def answer(n):
    """Sum of the all natural numbers less than n that are multiples of 3 or 5"""

    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result = result + i

    return result
