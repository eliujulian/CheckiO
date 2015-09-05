"""
While Stephen is running cargo, Nicola and Sophia invented a game using the boxes.
To start the game, they put several black and white pearls in one of the boxes. Each robots have Nth moves, then initial
set are restored for a next player. For each move, the robot take a pearl out of the box and put one of the opposite
color back.

The winner is the one who pulls the white pearl on the Nth step (or +1 point if they play many parties).

Our robots don't like indeterminacy and want to know the probability of a white pearl on the Nth step. The probability
is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen). The result is a float from 0 to
1 with two digits precision (0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the step
(N). The order of the pearls does not matter.

Input: The start sequence of the pearls as a string and the step number as an integer.
Output: The probability for a white pearl as a float.
Precondition: 0 < N ? 20
0 < |pearls| ? 20
"""

import unittest


def checkio(marbles, step):
    result = [[marbles.count("w"), marbles.count("b"), 1]]

    for s in range(step - 1):
        new_list = result
        result = []

        for box in new_list:
            if box[0] == 0:
                box[0] += 1
                box[1] -= 1
                result.append([box[0], box[1], box[2]])

            elif box[1] == 0:
                box[0] -= 1
                box[1] += 1
                result.append([box[0], box[1], box[2]])

            else:
                box_1 = box.copy()
                box_1[0] += 1
                box_1[1] -= 1
                box_1[2] = box[2] * (box[1] / len(marbles))
                result.append(box_1)

                box_2 = box.copy()
                box_2[0] -= 1
                box_2[1] += 1
                box_2[2] = box[2] * (box[0] / len(marbles))
                result.append(box_2)

    return round(sum([n[0] / len(marbles) * n[2] for n in result]), 2)


class TestChekcio(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0.48, checkio('bbw', 3))


if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    assert checkio("bbbbbbbbbbbb", 5) == 0.26
    assert checkio("wwwwwwwwwwww", 4) == 0.79
    assert checkio("b", 2) == 1
    assert checkio("w", 2) == 0
    assert checkio("b", 1) == 0
    assert checkio("w", 1) == 1
    assert checkio("wbwwwwwb", 3) == 0.64
    assert checkio("bbbbw", 5) == 0.46
    assert checkio("bwb", 2) == 0.44
    assert checkio("bbwbwbbwbwwbw", 11) == 0.49
    assert checkio("wwbwwwbbwbbwww", 10) == 0.54
    assert checkio("wwwwwbwbwbbwbbwwbw", 11) == 0.53
    assert checkio("wwwwwwwwwwwwwwwwwwww", 20) == 0.57
