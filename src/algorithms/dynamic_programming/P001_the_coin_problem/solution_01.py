import logging
import math

"""
Note
1. Optimisation(s)
    - None
2. Limitation(s)
    - None
"""


def answer(coin_values, coin_sum):
    minimum_sum = [10000] * (coin_sum + 1)
    minimum_sum[0] = 0

    for i in range(1, coin_sum + 1):
        for j in range(0, len(coin_values)):
            if coin_values[j] <= i and minimum_sum[i - coin_values[j]] + 1 < minimum_sum[i]:
                minimum_sum[i] = minimum_sum[i - coin_values[j]] + 1

    return minimum_sum[coin_sum]
