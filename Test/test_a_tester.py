import unittest
from a_tester import add, fois

class TestAddWithUnittest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(3.2,4.5), 7.7)
        self.assertEqual(add("a","b"), "ab")
        
    def test_fois(self):
        self.assertEqual(fois(2,4), 8)
        self.assertEqual(fois('a',2), 'aa')
        with self.assertRaises(TypeError):
            fois('a' * 'a')
        self.assertEqual(fois('a',-2), ' ')