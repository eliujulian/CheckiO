from unittest import TestCase


def checkio(first, second):
    return ",".join(sorted(list(set(first.split(",")) & set(second.split(",")))))


class Test(TestCase):
    def test(self):
        self.assertEqual("hello", checkio("hello,world", "hello,earth"))
        self.assertEqual("", checkio("one,two,three", "four,five,six"))
        self.assertEqual("one,three,two", checkio("one,two,three", "four,five,one,two,six,three"))
