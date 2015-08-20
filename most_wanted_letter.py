from unittest import TestCase


def checkio(text):
    different_letters = set(text.lower())
    only_letters = set("abcdefghijklmnopqrstuvwxyz")
    different_letters.intersection_update(only_letters)
    result = []
    for n in different_letters:
        result.append((text.lower().count(n), n))
    result.sort(reverse=True)
    print(result)
    new = []
    for n in result:
        if n[0] == result[0][0]:
            new.append(n)
    if len(new) > 1:
        new.sort(key=str)
    print(new)
    return new[0][1]


class Test_chekio(TestCase):
    def test_hello_world(self):
        self.assertEqual(checkio("Hello World!"), "l")

    def test_how_do_you_do(self):
        self.assertEqual(checkio("How do you do?"), "o")

    def test_one(self):
        self.assertEqual(checkio("One"), "e")

    def test_only_lower(self):
        self.assertEqual(checkio("Oops!"), "o")

    def test_only_letters(self):
        self.assertEqual(checkio("AAaooo!!!!"), "a")

    def test_the_first(self):
        self.assertEqual(checkio("abe"), "a")

    def test__loong(self):
        self.assertEqual(checkio("a" * 9000 + "b" * 1000), "a")

    def test_Z(self):
        self.assertEqual(checkio("Z"), "z")

"""
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
"""