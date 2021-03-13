import unittest
from calculator.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_convert_roman_to_arabic(self):
        self.assertEqual("1", convert_roman_to_arabic("I"))
        self.assertEqual("2", convert_roman_to_arabic("II"))
        self.assertEqual("3", convert_roman_to_arabic("III"))
        self.assertEqual("4", convert_roman_to_arabic("IV"))
        self.assertEqual("5", convert_roman_to_arabic("V"))
        self.assertEqual("6", convert_roman_to_arabic("VI"))
        self.assertEqual("7", convert_roman_to_arabic("VII"))
        self.assertEqual("8", convert_roman_to_arabic("VIII"))
        self.assertEqual("9", convert_roman_to_arabic("IX"))
        self.assertEqual("10", convert_roman_to_arabic("X"))
        self.assertEqual("30", convert_roman_to_arabic("XXX"))
        self.assertEqual("60", convert_roman_to_arabic("LX"))
        self.assertEqual("90", convert_roman_to_arabic("XC"))
        self.assertEqual("400", convert_roman_to_arabic("CD"))
        self.assertEqual("900", convert_roman_to_arabic("CM"))
        self.assertEqual("1886", convert_roman_to_arabic("MDCCCLXXXVI"))
        self.assertEqual("1111", convert_roman_to_arabic("MCXI"))
        self.assertEqual("1999", convert_roman_to_arabic("MCMXCIX"))
        self.assertEqual("14", convert_roman_to_arabic("XIV"))

    def test_convert_expression_to_arabic(self):
        self.assertEqual("1+1", convert_expression_to_arabic("I+I"))
        self.assertEqual("1+2", convert_expression_to_arabic("I+II"))
        self.assertEqual("1+4", convert_expression_to_arabic("I+IV"))
        self.assertEqual("1+4+1", convert_expression_to_arabic("I+IV+I"))
        self.assertEqual("1+1000+1+100", convert_expression_to_arabic("I+M+I+C"))
        self.assertEqual("1-4", convert_expression_to_arabic("I-IV"))
        self.assertEqual("1+4-10", convert_expression_to_arabic("I+IV-X"))
        self.assertEqual("1+1000-1+100", convert_expression_to_arabic("I+M-I+C"))
        self.assertEqual("1*4", convert_expression_to_arabic("I*IV"))
        self.assertEqual("1*4//9-2+1", convert_expression_to_arabic("I*IV/IX-II+I"))
        self.assertEqual("1*6", convert_expression_to_arabic("I*VI"))
        self.assertEqual("1*600", convert_expression_to_arabic("I*DC"))

    def test_get_calculated_expression(self):
        self.assertEqual(2, eval(convert_expression_to_arabic("I+I")))
        self.assertEqual(3, eval(convert_expression_to_arabic("I+II")))
        self.assertEqual(5, eval(convert_expression_to_arabic("I+IV")))

    def test_convert_arabic_to_roman(self):
        self.assertEqual("DCXI", convert_arabic_to_roman("611"))
        self.assertEqual("MMMCMXCIX", convert_arabic_to_roman("3999"))
        self.assertEqual("VI", convert_arabic_to_roman("6"))
        self.assertEqual("DCCLXVIII", convert_arabic_to_roman("768"))
        self.assertEqual("CMLXVIII", convert_arabic_to_roman("968"))
