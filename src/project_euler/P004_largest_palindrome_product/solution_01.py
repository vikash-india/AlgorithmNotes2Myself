import logging

"""
Note
1. All possible combination will have to checked and not just the top end of the 3-digit numbers.
2. Optimisation(s)
    - Dont check for the number already checked in the loop.
3. Limitation(s)
    - None
"""


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


def answer(minimum=100, maximum=999):
    largest_palindrome_product = 0
    for i in range(minimum, maximum + 1):
        # Dont recompute previously computed values
        for j in range(i + 1, maximum + 1):
            product = i * j
            if product > largest_palindrome_product and is_palindrome(product):
                largest_palindrome_product = product
    return largest_palindrome_product
