import logging

from src.google_foobar.P007_binary_bunnies.solution_01 import answer


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    seq = [5, 9, 8, 2, 1]
    expected = '6'
    # print answer(seq)

    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = '1'
    # print answer(seq)

    seq = [10, 8, 15, 6, 9, 4, 5]
    expected = '24'
    # print answer(seq)

    seq = [12, 6, 19, 15, 5]
    expected = '6'
    # print answer(seq)

    seq = [44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
    expected = '1'
    # print answer(seq)

    seq = [5, 9, 8, 2, 1, 10, 3]
    expected = '1'
    print(answer(seq))


# Call Main
if __name__ == '__main__': main()
