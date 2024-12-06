from ProgrammingBasicsAndAlgorithms.Exercises.Basics.Solutions.sort import sort
import unittest

class TestSort(unittest.TestCase):
    def test_sort(self):
        a = [3, 0, 12, 8]
        b = sort(a)
        self.assertEqual( [0, 3, 8, 12], b)