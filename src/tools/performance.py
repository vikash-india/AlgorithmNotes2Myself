from src.tools.function import decorator


@decorator
def memoize(f):
    """
    A decorator that caches the return value for each call to f(args).
    Then when called again with some arguments, we can just look it up.

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            """Some elements of args (mutable sequence like list) cannot be a dict key."""
            return f(args)
        return _f
