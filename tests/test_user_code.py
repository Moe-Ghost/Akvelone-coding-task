import unittest

from app import NumberFormatter


class UserTestCase(unittest.TestCase):

    def test_correct_type(self):
        str1 = '123-45'
        str2 = NumberFormatter.parse_int(str1)
        for i in str2:
            self.assertIs(type(i), type(1))

    def test_correct_str(self):
        result = []
        str1 = '123-45'
        str2 = NumberFormatter.parse_int(str1)
        for i in str2:
            result.append(i)
        self.assertEqual(result, [1, 2, 3, -4, 5])

    def test_incorrect_str_length(self):
        str1 = '1'
        str2 = NumberFormatter.validating(str1)
        self.assertEqual(str2, 'incorrect string length')

    def test_incorrect_math_operator(self):
        str1 = '12-'
        str2 = NumberFormatter.validating(str1)
        self.assertEqual(str2, 'incorrect last symbol')

    def test_wrong_values(self):
        str1 = 'abc'
        str2 = NumberFormatter.validating(str1)
        self.assertEqual(str2, "incorrect symbol")
