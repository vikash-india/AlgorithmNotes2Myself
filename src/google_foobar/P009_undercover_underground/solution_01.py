from math import factorial
from src.tools.function import disabled
from src.tools.debug import trace
import logging

"""
Note
1. Write Here
2. Optimisation(s)
    - None
3. Limitation(s)
    - None
"""
trace=disabled

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
# factorial = trace(factorial)

@memoize
#@trace
def C(n, r):
    if n < 0 or r > n:
        """
        The C(3, 5) means choosing 5 objects from 3 given objects. Logically there should be 0 ways to do
        that.
        """
        return 0
    else:
        # print 'n=%s, r=%s, n-r=%s' % (n, r, n - r)
        return int(factorial(n) / (factorial(r) * factorial(n - r)))


@memoize
@trace
def answer(N, K):
    # Number of edges required to connect every node to each other.
    maximum_edges = C(N, 2)

    # Number of ways to choose K edges out of maximum edges.
    connectivity = C(maximum_edges, K)

    logging.info('One: N=%s, K=%s, maximum_edges=%s, connectivity=%s' % (N, K, maximum_edges, connectivity))
    # Find the number of those combinations which have one or more isolated nodes.
    # Isolated nodes are found in cases like N=4, K=3
    if K < C(N - 1, 2) + 1:
        for i in range(1, N):
            ith_maximum_edges = C(i, 2)
            ith_connectivity = C(N - 1, i - 1)
            logging.info('Two: i=%s, ith_connectivity=%s, ith_maximum_edges=%s' % (i, ith_connectivity, ith_maximum_edges))

            for j in range(i - 1, min(ith_maximum_edges, K) + 1):
                jth_maximum_edges = C(N - i, 2)
                jth_connectivity = C(jth_maximum_edges, K - j)

                connectivity -= ith_connectivity * jth_connectivity * int(answer(i, j))
                logging.info('Three: j=%s, connectivity=%s' % (j, connectivity))

    return str(connectivity)
