from src.google_foobar.P009_undercover_underground.solution_01 import answer
from math import factorial
import logging
import itertools


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    # logging.basicConfig(level=logging.DEBUG)

    N = 4
    K = 3
    expected = '16'
    print "N = %-2s K = %-3s expected = %-3s, answer = %s" % (N, K, expected, (answer(N, K)))

    # Generate Combinations
    # edges = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
    # K = 4
    # generate_combination(edges, K)

    # Generate testcases
    # print 80 * '-'
    # generate_testcases()


def generate_testcases():
    for N in range(2, 21):
        for K in range(N - 1, N * (N - 1) / 2 + 1):
            print "N = %-2s K = %-3s answer = %s" % (N, K, (answer(N, K)))


def generate_combination(edges, K):
    s = list(itertools.combinations(edges, K))
    print(len(s))
    print(s)


# Call Main
if __name__ == '__main__': main()
