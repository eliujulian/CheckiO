import re, math, unittest

def checkio(anything):
    class SomeClass(object):
        def __cmp__(self, other):
            return True
        def __eq__(self, other):
            return True
        def __ne__(self, other):
            return True
        def __lt__(self, other):
            return True
        def __gt__(self, other):
            return True
        def __le__(self, other):
            return True
        def __ge__(self, other):
            return True

    return SomeClass()

class Test_chkio(unittest.TestCase):
    def test_dict_to_list(self):
        self.assertTrue(checkio({}) != [])

    def test_str(self):
        self.assertTrue(checkio("Hello") < "World")

    def test_int(self):
        self.assertTrue(checkio(80) > 81)

    def test_module(self):
        self.assertTrue(checkio(re) >= re)

    def test_module_2(self):
        self.assertTrue(checkio(re) <= math)

    def test_ord(self):
        self.assertTrue(checkio(5) == ord)

