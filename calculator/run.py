from calculator.cli.cli_parser import parse
from calculator.core.handle_data import *

def run(args):
    arabic_expression = convert_expression_to_arabic(args.roman_expression)
    arabic_result_expression = eval(arabic_expression)
    validate_arabic_number(arabic_result_expression)
    roman_result_expression = convert_arabic_to_roman(str(arabic_result_expression))
    print(f"{args.roman_expression} = {roman_result_expression}")

if __name__ == "__main__":
    run(parse())