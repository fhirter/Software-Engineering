import unittest

from ProgrammingBasicsAndAlgorithms.Examples.ErrorHandling import return_value, return_error


class TestErrorHandling(unittest.TestCase):
    def test_return_value(self):
        value, error = return_value()
        self.assertIsNotNone(value)
        self.assertIsNone(error)

    def test_return_error(self):
        value, error = return_error()
        self.assertIsNotNone(error)
        self.assertIsNone(value)


if __name__ == '__main__':
    unittest.main()
