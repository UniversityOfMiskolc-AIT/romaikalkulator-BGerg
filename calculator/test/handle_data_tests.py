import unittest
from calculator.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_exchange_to_arabic_single_digit(self):
        self.assertEqual(exchange_to_arabic("I"), "1")
        self.assertEqual(exchange_to_arabic("II"), "2")
        self.assertEqual(exchange_to_arabic("III"), "3")
        self.assertEqual(exchange_to_arabic("IV"), "4")
        self.assertEqual(exchange_to_arabic("V"), "5")
        self.assertEqual(exchange_to_arabic("VI"), "6")
        self.assertEqual(exchange_to_arabic("VII"), "7")
        self.assertEqual(exchange_to_arabic("VIII"), "8")
        self.assertEqual(exchange_to_arabic("IX"), "9")
        self.assertEqual(exchange_to_arabic("X"), "10")
        self.assertEqual(exchange_to_arabic("XXX"), "30")
        self.assertEqual(exchange_to_arabic("LX"), "60")
        self.assertEqual(exchange_to_arabic("XC"), "90")
        self.assertEqual(exchange_to_arabic("CD"), "400")
        self.assertEqual(exchange_to_arabic("CM"), "900")
        self.assertEqual(exchange_to_arabic("MDCCCLXXXVI"), "1886")
        self.assertEqual(exchange_to_arabic("MCXI"), "1111")
        self.assertEqual(exchange_to_arabic("MCMXCIX"), "1999")
        self.assertEqual(exchange_to_arabic("XIV"), "14")

    def test_convert_expression_to_arabic(self):
        self.assertEqual(convert_expression_to_arabic("I+I"), "1+1")
        self.assertEqual(convert_expression_to_arabic("I+II"), "1+2")
        self.assertEqual(convert_expression_to_arabic("I+IV"), "1+4")
        self.assertEqual(convert_expression_to_arabic("I+IV+I"), "1+4+1")
        self.assertEqual(convert_expression_to_arabic("I+M+I+C"), "1+1000+1+100")
        self.assertEqual(convert_expression_to_arabic("I-IV"), "1-4")
        self.assertEqual(convert_expression_to_arabic("I+IV-X"), "1+4-10")
        self.assertEqual(convert_expression_to_arabic("I+M-I+C"), "1+1000-1+100")
        self.assertEqual(convert_expression_to_arabic("I*IV"), "1*4")
        self.assertEqual(convert_expression_to_arabic("I*IV/IX-II+I"), "1*4//9-2+1")

    def test_get_calculated_expression(self):
        self.assertEqual(get_calculated_expression("1+1", "I+I"), "I+I=2")
        self.assertEqual(get_calculated_expression("1886+1", "MDCCCLXXXVI+I"), "MDCCCLXXXVI+I=1887")
        self.assertEqual(get_calculated_expression("1-2", "MDCCCLXXXVI+I"), "MDCCCLXXXVI+I=-1")
        self.assertEqual(get_calculated_expression("1*4//9-2+1", "I*IV/IX-II+I"), "I*IV/IX-II+I=-1")
