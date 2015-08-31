def count_gold(pyramid):
    possible_path = 2 ** (len(pyramid) - 1)

    result = [[0 for n in range(len(pyramid))]]
    last = [0 for n in range(len(pyramid))]

    for path in range(possible_path - 1):
        index_identifier = 0

        for n in range(len(pyramid)):
            new = last.copy()

            index_identifier += 1

            new[int(len(pyramid)) - index_identifier] += 1

            if index_identifier > 2:
                for i in range(index_identifier - 2):
                    i += 1
                    new[int(len(pyramid)) - index_identifier + i + 1] -= i

            if set([n for n in range(max(set(new)) +1)]) == set(new):
                last = new
                result.append(new)
                break

    max_gold = [(sum([pyramid[l][p[l]] for l in range(len(pyramid))])) for p in result]

    return max(max_gold)


import unittest

class TestGold(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(3, count_gold(((1,), (2, 2))))

    def test_1(self):
        self.assertEqual(23, count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3))))

    def test_1a(self):
        self.assertEqual(12, count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        )))

    def test_1b(self):
        self.assertEqual(13, count_gold((
        (0,),
        (0, 1),
        (5, 1, 2),
        (0, 1, 2, 3),
        (8, 1, 2, 3, 4),
        )))

    def test_2(self):
        self.assertEqual(7, count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        )))

    def test_web_2(self):
        self.assertEqual(15, count_gold(((1,),(2,1),(1,2,1),(1,2,1,1),(1,2,1,1,1),(1,2,1,1,1,1),(1,2,1,1,1,1,9))))

    def test_web_12(self):
        self.assertEqual(139, count_gold(((4,),(1,7),(9,9,7),(4,9,9,3),(3,5,3,7,5),(1,7,5,3,5,6),(6,5,5,8,3,3,3),(6,8,6,8,7,3,7,5),(7,9,9,1,6,8,7,5,9),(2,8,2,5,5,5,2,5,7,8),(1,3,5,2,4,5,3,5,1,1,6),(8,6,1,1,3,4,7,5,3,6,1,9),(5,8,6,6,2,6,9,3,7,4,6,9,9),(3,3,5,4,4,6,9,2,5,7,7,1,6,7),(8,1,4,4,6,8,4,9,7,6,1,8,4,2,9),(6,5,8,6,8,3,2,4,8,8,1,5,6,8,8,7),(6,3,9,1,5,6,7,7,2,2,6,2,2,1,8,8,6),(4,7,8,7,5,2,8,8,2,2,7,1,3,8,1,9,4,7),(1,7,8,1,4,3,8,6,6,9,6,3,5,4,7,6,4,5,6),(1,1,4,9,9,8,3,3,8,1,8,1,7,6,6,3,2,1,1,6))))