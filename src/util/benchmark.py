# CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
import time


def timed_call(function, *args):
    """Call function(*args).

       Return the tuple(time in seconds, result).
    """

    t0 = time.clock()
    result = function(*args)
    t1 = time.clock()

    return t1 - t0, result


def timed_calls(n, function, *args):
    """Call function(*args) repeatedly as follows,
        Case 1: Call function n times if n is an int.
        Case 2: Call function up to N seconds if n is a float.

        Returns the minimum, average, and maximum time
    """

    if isinstance(n, int):
        times = [timed_call(function, *args)[0] for _ in range(n)]
    else:
        times = []
        while (sum(times) < n):
            times.append(timed_call(function, *args)[0])

    return min(times), average(times), max(times)


def average(numbers):
    """Return the average (arithmetic mean) of a sequence of numbers."""

    return sum(numbers) / float(len(numbers))


def benchmark(n, function, *args):
    (minimumTime, averageTime, maximumTime) = timed_calls(n, function, *args)
    print (
        "Time for %d runs (In sec): Minimum: %s, Average: %s, Maximum: %s" % (n, minimumTime, averageTime, maximumTime))

# # Modify these before benchmarking
# RUN_N_TIMES = 2
# benchmark(RUN_N_TIMES, main)
