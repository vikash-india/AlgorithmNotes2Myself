import logging

"""
Note
1. Optimisation(s)
    - None
2. Limitation(s)
    - None
"""


def answer(numbers):
    # Keep a track of the pirates that have been already been explored.
    pirates_explored = []

    # First pirate position
    i = 0

    # Infinite loop is fine since challenge guarantees a loop.
    while True:

        # Pirate is already explored implies a loop.
        if i in pirates_explored:
            # Remove the index of the pirate that was just found.
            return len(pirates_explored) - pirates_explored.index(i)

        # Add the pirates to explored list
        pirates_explored.append(i)

        i = numbers[i]
