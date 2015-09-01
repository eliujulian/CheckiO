"""
Not my solution. See here: http://www.checkio.org/mission/golden-pyramid/publications/zero_loss/python-3/first/?ordering=most_voted
"""

def count_gold(pyramid):
    py = [list(i) for i in pyramid]
    print(py)
    for i in reversed(range(len(py)-1)): # pyramid level from bottom
        for j in range(i+1): #path in level
            py[i][j] +=(max(py[i+1][j], py[i+1][j+1]))
            print(py[i][j])
    return py[0][0]



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
