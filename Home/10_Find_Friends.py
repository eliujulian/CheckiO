from unittest import TestCase

def check_connection(network, first, second):
    max_depth = len(network)

    if not any(map(lambda x: x.startswith(first), network)):
        for connection in network:
            if first in connection:
                first = connection[:connection.find("-")]

    counter = 0
    network = list(network)
    while counter < max_depth * max_depth:
        for connection in network:
            if first in connection and second in connection:
                return True

        for connection in network:
            if connection.startswith(first):
                first = connection[connection.find("-") + 1:]
                network.remove(connection)
                break
            elif connection.endswith(first):
                first = connection[:connection.find("-")]
                network.remove(connection)
                break
            counter += 1

    return False



class Test_CheckConnection(TestCase):
    def test_simple(self):
        self.assertTrue(check_connection(("sehr-einfach", ), "sehr", "einfach"))

    def test_one_connection(self):
        self.assertTrue(check_connection(("sehr-einfach", "einfach-toll"), "sehr", "toll"))

    def test_one_connection_reverse(self):
        self.assertTrue(check_connection(("toll-some", "some-einfach", "einfach-sehr"), "sehr", "toll"))

    def test_1(self):
        self.assertTrue(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3"))

    def test_2(self):
        self.assertTrue(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2"))

    def test_3(self):
        self.assertFalse(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout"))

    def test_4(self):
        self.assertTrue(check_connection(("cat-robin","cat-base","out00-scout4","robin-scout4","cat-batman","batman-plane2","plane2-scout3","plane2-base","robin-batman","mr99-scout3",),"base","robin"))
