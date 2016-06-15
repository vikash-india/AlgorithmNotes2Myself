from src.tools.function import decorator


@decorator
def trace(f):
    """
    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """

    indent = '   '

    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level * indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            print '%s<-- %s == %s' % ((trace.level - 1) * indent, signature, result)
        finally:
            trace.level -= 1
        return result

    trace.level = 0
    return _f


