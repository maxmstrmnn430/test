
import unittest

class TestBlub(unittest.TestCase):

    def test_blub(self):
        self.assertTrue(True)

    def test_crap(self):
        self.assertEquals(1, 2-1, "Da funktioniert was nicht")

