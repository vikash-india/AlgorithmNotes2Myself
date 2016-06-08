import logging

"""
Note
1. Implemention of a bubble sort algorithm with an optimization.
2. Optimisation(s)
    - The n-th pass finds the n-th largest element and puts it into its final place. So, the inner loop can avoid
      looking at the last n-1 items when running for the n-th time.
3. Limitation(s)
    - Can be optimized further.
"""
def bubble_sort(numbers):
    """Implement Bubble Sort Algorithm"""

    # For Instrumentation
    iterations_count = 0
    passes_count = 0
    swaps_count = 0

    # Main Algorithm
    swapped = True
    n = len(numbers)
    while swapped:
        swapped = False
        passes_count = passes_count + 1
        for index in range(1, n):
            iterations_count = iterations_count + 1

            # Swap if this pair is out of order
            if numbers[index - 1] > numbers[index]:
                swaps_count = swaps_count + 1

                # Swap and remember
                numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]
                swapped = True

                # Debug Info
                logging.debug('Swapped {0} and {1}'.format(numbers[index - 1], numbers[index]))

            logging.debug('Pass {0}, Iteration {1}, Swap Count {2}, Index {3} Data: {4}'.format(passes_count, \
                                                                        iterations_count, swaps_count, index, numbers))

        # Optimisation: The n-th pass finds the n-th largest element and puts it into its final place. So, the inner
        # loop can avoid looking at the last n-1 items when running for the n-th time.
        n = n - 1

    logging.info('Total Passes {0}, Iterations {1}, Swaps {2}'.format(passes_count, iterations_count, swaps_count))
    return numbers

