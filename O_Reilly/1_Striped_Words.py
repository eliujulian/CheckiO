from unittest import TestCase

VOWELS = set("AEIOUY")
CONSONANTS = set("BCDFGHJKLMNPQRSTVWXZ")


def checkio(text):
    new_text = ""
    for n in text:
        if n.isalpha() or n.isdigit():
            new_text += n
        else:
            new_text += " "
    words = new_text.split()
    result = 0
    print(words)

    for word in words:
        if len(word) == 1:
            pass
        else:
            batch_one = [n.upper() for ind, n in enumerate(word) if ind % 2 == 0]
            batch_two = [n.upper() for ind, n in enumerate(word) if ind % 2 != 0]

            if set(batch_one) <= VOWELS and set(batch_two) <= CONSONANTS:
                result += 1
            elif set(batch_one) <= CONSONANTS and set(batch_two) <= VOWELS:
                result += 1
            else:
                pass

    return result

class TestCheckiO(TestCase):
    def test_2(self):
        self.assertEqual(8, checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?"))

    def test_extra(self):
        self.assertEqual(1, checkio("1st 2a ab3er root rate"))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
