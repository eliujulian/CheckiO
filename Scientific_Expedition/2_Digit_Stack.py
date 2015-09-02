def digit_stack(commands):
    stack = []
    result = 0

    for c in commands:
        if c == "PEEK" and stack:
            result += stack[-1]
        elif c == "POP" and stack:
            result += stack.pop()
        elif c.startswith("PUSH"):
            stack.append(int(c[-1]))

    return result


import unittest


class TestDigitStack(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                         "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    def test_2(self):
        self.assertEqual(0, digit_stack(["POP", "POP"]))

    def test_3(self):
        self.assertEqual(9, digit_stack(["PUSH 9", "PUSH 9", "POP"]))

    def test_4(self):
        self.assertEqual(0, digit_stack([]))

    def test_5(self):
        self.assertEqual(8, digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK",
                                          "POP", "PUSH 1", "PEEK"]))
