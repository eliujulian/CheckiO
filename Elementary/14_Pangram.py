from unittest import TestCase
import logging
import string

logging.basicConfig(level=logging.INFO)


def check_pangram(text):
    logging.debug("input of function: {0}".format(text))
    result = set(string.ascii_lowercase) <= set(text.lower())
    logging.debug("result: {0}".format(result))
    return set(string.ascii_lowercase) <= set(text.lower())


class Test(TestCase):
    def test_1(self):
        self.assertTrue(check_pangram("The quick brown fox jumps over the lazy dog."))
        self.assertFalse(check_pangram("ABCDEF"))
        self.assertTrue(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"))
