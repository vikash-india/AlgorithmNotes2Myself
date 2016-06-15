from functools import update_wrapper


def decorator(d):
    """
    Make function d a decorator: d wraps a function fn.

    This will also make sure that documentation returns the appropriate function instead of the decorator.

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """

    def _d(fn):
        return update_wrapper(d(fn), fn)

    update_wrapper(_d, d)
    return _d


def disabled(f):
    """
    Usage: trace=disabled at the beginning to disable trace or any function.

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """
    return f
