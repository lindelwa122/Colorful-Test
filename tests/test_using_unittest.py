import unittest

class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertSequenceEqual([1, 2, 3], (1, 2, 3))