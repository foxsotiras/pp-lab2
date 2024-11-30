import unittest
from main import is_roman_numeral


class TestRomanNumeral(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(is_roman_numeral("XI"), True)
        self.assertEqual(is_roman_numeral("XXI"), True)
        self.assertEqual(is_roman_numeral("CML"), True)
        self.assertEqual(is_roman_numeral("MMII"), True)
        self.assertEqual(is_roman_numeral("XAAAI"), False)
        self.assertEqual(is_roman_numeral("DAS"), False)
