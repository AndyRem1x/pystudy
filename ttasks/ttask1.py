import unittest

from testing_task import make_operation


class TestMakeOperationFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(make_operation('+', 1, 23, 4, 5), 33)
        self.assertEqual(make_operation('+', 7, 7, 2), 16)

    def test_subtraction(self):
        self.assertEqual(make_operation('-', 5, 5, -10, -20), 30)

    def test_multiplication(self):
        self.assertEqual(make_operation('*', 7, 6), 42)

    def test_unsupported_operator(self):
        self.assertEqual(make_operation('/', 1, 2, 3), "This operator is unsupported")

    def test_empty_args(self):
        self.assertEqual(make_operation('+'), "No arguments provided")


if __name__ == '__main__':
    unittest.main()
