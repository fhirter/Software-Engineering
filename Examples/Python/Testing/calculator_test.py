import unittest

from Examples.Python.Testing import calculator


class TestSum(unittest.TestCase):

    def test_sum(self):
        # Arrange
        operand1 = 2
        operand2 = 3
        expected_result = 5

        # Act
        actual_result = calculator.add(operand1, operand2)

        # Assert
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
