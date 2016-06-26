import logging

from src.google_foobar.P008_carrotland.solution_01 import answer


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    vertices = [[-1, -1], [1, 0], [0, 1]]
    expected = 1
    print answer(vertices)

    vertices = [[2, 3], [6, 9], [10, 160]]
    expected = 289
    print answer(vertices)

    vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
    expected = 1730960165
    print answer(vertices)

    vertices = [[0, 0], [0, 1], [1, 0]]
    expected = 0
    print answer(vertices)


# Call Main
if __name__ == '__main__': main()
