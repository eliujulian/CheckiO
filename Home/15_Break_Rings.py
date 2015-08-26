from unittest import TestCase

def break_rings(rings):
    connections = list(rings)

    for n in range(len(connections)):
        flatten = [x for inst in connections for x in inst]
        all_rings = [(ring, flatten.count(ring)) for ring in set(flatten)]

        for i in sorted(all_rings, key=lambda x: x[1]):
            if i[1] == min(all_rings, key= lambda x: x[1])[1]:
                anchor = i[0]
                break

        for c in connections:
            if anchor in c:
                removing = list(c)
                removing.remove(anchor)
                removing = removing[0]
                break

        connections = [item for item in connections if removing not in item]

        if not connections:
            return n + 1



class TestBreakRings(TestCase):
    def test_three_rings_chain(self):
        self.assertEqual(1, break_rings(({1, 2}, {2, 3})))

    def test_three_rings_circle(self):
        self.assertEqual(2, break_rings(({1, 2}, {2, 3}, {1, 3})))

    def test_four_rings_circle(self):
        self.assertEqual(2, break_rings(({1, 2}, {2, 3}, {3, 4}, {1, 4})))

    def test_four_rings_star(self):
        self.assertEqual(1, break_rings(({1, 2}, {2, 3}, {2, 4})))

    def test_example(self):
        self.assertEqual(3, break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})))

    def test_all_to_all(self):
        self.assertEqual(3, break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})))

    def test_chain(self):
        self.assertEqual(3, break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})))

    def test_long_chain(self):
        self.assertEqual(5, break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})))

    def test_8(self):
        self.assertEqual(5, break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)))

    def test_1(self):
        self.assertEqual(3, break_rings(({8,7},{1,9},{2,7},{3,6},{1,7},{5,7},{3,4},{9,5},{9,6},{3,5},)))

    def test_13(self):
        self.assertEqual(8, break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},)))