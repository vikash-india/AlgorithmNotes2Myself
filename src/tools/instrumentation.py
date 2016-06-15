import time


def timed_call(function, *args):
    """
    Calls function(*args)

    Return the tuple(time in seconds, result).

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """

    t0 = time.clock()
    result = function(*args)
    t1 = time.clock()

    return t1 - t0, result


def timed_calls(n, function, *args):
    """
    Call function(*args) repeatedly as follows,
        Case 1: Call function n times if n is an int.
        Case 2: Call function up to N seconds if n is a float.

    Returns the minimum, average and maximum time

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """
    if isinstance(n, int):
        times = [timed_call(function, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timed_call(function, *args)[0])

    return min(times), average(times), max(times)


def average(numbers):
    """
    Return the average (arithmetic mean) of a sequence of numbers.

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """
    return sum(numbers) / float(len(numbers))


def benchmark(n, function, *args):
    """
    Usage Examples
        benchmark(100, answer)                  - Run answer() 100 times.
        benchmark(100, answer, 'a=1, b=2')      - Run answer(a=2, b=3) 100 times.
        print benchmark(100, answer, '1, 2')    - Run answer(a, b) 100 times.
        print benchmark(100, answer, 1, 2)      - Run answer(a, b) 100 times.

        benchmark(2.0, answer)                  - Run answer() for upto 2 seconds.
        benchmark(2.0, answer, 'a=1, b=2')      - Run answer(a=2, b=3) for upto 2 seconds.

    CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
    """
    (minimum_time, average_time, maximum_time) = timed_calls(n, function, *args)
    print ('Time (In seconds) for %d runs: Minimum: %s, Average: %s, Maximum: %s for function call %s with args %s' %
           (n, minimum_time, average_time, maximum_time, function.__name__, args))
