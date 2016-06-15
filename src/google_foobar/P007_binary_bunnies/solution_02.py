from math import factorial
from src.tools.debug import trace, disabled

"""
Note
1. This solution combines the divide, conquer and combine function into a single function to reduce the number
   of function calls. This reduces the stack size and improves the performance. This is what I submitted to Google.
2. Optimisation(s)
    - Use memoization to speed up the computation of factorial.
    - Use less number of functions in a recursive calls.
3. Limitation(s)
    - None
"""


def memoize(f):
    """
    A decorator that caches the return value for each call to f(args).
    Then when called again with some arguments, we can just look it up.
    """
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            """Some elements of args cannot be a dict key"""
            return f(args)

    return _f


# Memoize factorial
factorial = memoize(factorial)


def answer(seq):
    # Divide
    left_tree = []
    right_tree = []
    root = seq[0]
    for i in range(1, len(seq)):
        if seq[i] < root:
            right_tree.append(seq[i])
        else:
            left_tree.append(seq[i])

    # Conquer left
    left_result = 1
    if len(left_tree) > 2:
        left_result = int(answer(left_tree))

    # Conquer right
    right_result = 1
    if len(right_tree) > 2:
        right_result = int(answer(right_tree))

    # Combine Result
    level_result = factorial(len(left_tree) + len(right_tree)) / (factorial(len(left_tree)) *
                                                                  factorial(len(right_tree)))
    result = level_result * right_result * left_result

    return str(result)
