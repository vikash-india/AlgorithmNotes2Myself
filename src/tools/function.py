# CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.

from functools import update_wrapper

# This is used to make sure that documentation returns the appropriate tools
def decorator(d):
    "Make function d a decorator: d wraps a function fn."

    def _d(fn):
        return update_wrapper(d(fn), fn)

    update_wrapper(_d, d)
    return _d

