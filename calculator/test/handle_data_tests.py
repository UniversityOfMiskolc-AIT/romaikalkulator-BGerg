import unittest
from calculator.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_exchange_to_arabic_single_digit(self):
        self.assertEqual(exchange_to_arabic("I"),1)
        self.assertEqual(exchange_to_arabic("II"), 2)
        self.assertEqual(exchange_to_arabic("III"), 3)
        self.assertEqual(exchange_to_arabic("IV"), 4)
        self.assertEqual(exchange_to_arabic("V"), 5)
        self.assertEqual(exchange_to_arabic("VI"), 6)
        self.assertEqual(exchange_to_arabic("VII"), 7)
        self.assertEqual(exchange_to_arabic("VIII"), 8)
        self.assertEqual(exchange_to_arabic("IX"), 9)
        self.assertEqual(exchange_to_arabic("XXX"), 30)
        self.assertEqual(exchange_to_arabic("LX"), 60)
        self.assertEqual(exchange_to_arabic("MDCCCLXXXVI"), 1886)
        self.assertEqual(exchange_to_arabic("MCXI"), 1111)
        self.assertEqual(exchange_to_arabic("MCMXCIX"), 1999)
        self.assertEqual(exchange_to_arabic("XIV"), 14)


