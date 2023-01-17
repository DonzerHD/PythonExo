import unittest
from a_tester import add

class TestAddWithUnittest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(3.2,4.5), 7.7)
        self.assertEqual(add("a","b"), "ab")