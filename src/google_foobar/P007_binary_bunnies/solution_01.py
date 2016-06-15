from math import factorial
from src.tools.debug import trace, disabled

"""
Note
1. Optimisation(s)
    - Use memoization to speed up the computation of factorial.
2. Limitation(s)
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


# Disable trace
trace = disabled

# Memoize factorial
factorial = memoize(factorial)
factorial = trace(factorial)


@trace
def divide(seq):
    left_tree = []
    right_tree = []
    root = seq[0]
    for i in range(1, len(seq)):
        if seq[i] < root:
            right_tree.append(seq[i])
        else:
            left_tree.append(seq[i])

    return left_tree, right_tree


@trace
def conquer(sub_sequence):
    result = 1
    if len(sub_sequence) > 2:
        result = int(answer(sub_sequence))

    return result


@trace
def combine(left_tree, right_tree, left_result, right_result):
    level_result = factorial(len(left_tree) + len(right_tree)) / (factorial(len(left_tree)) *
                                                                  factorial(len(right_tree)))
    result = level_result * right_result * left_result

    # print 'Data: left_tree=%s, right_tree=%s, len(left_tree)=%s, len(right_tree)=%s, left_result=%s, right_result=%s, level_result=%s, result=%s' % (
    #     left_tree, right_tree, len(left_tree), len(right_tree), left_result, right_result, level_result, result)

    return result


@trace
def answer(seq):
    left_tree, right_tree = divide(seq)

    left_result = conquer(left_tree)
    right_result = conquer(right_tree)

    result = combine(left_tree, right_tree, left_result, right_result)

    return str(result)
