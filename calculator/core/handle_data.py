def convert_expression_to_arabic(expression: str):
    roman_number = ""
    arabic_expression = ""
    for elem in expression:
        if elem == "+" or elem == "-" or elem == "*" or elem == " ":
            arabic_expression += exchange_to_arabic(roman_number)
            arabic_expression += elem
            roman_number = ""
        elif elem == "/":
            arabic_expression += exchange_to_arabic(roman_number)
            arabic_expression += "//"
            roman_number = ""
        else:
            roman_number += elem

    arabic_expression += exchange_to_arabic(roman_number)  # add last number to the expression
    return arabic_expression


def exchange_to_arabic(roman_number: str) -> str:
    arabic_number = 0
    index = 0

    number_repository = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    while index < len(roman_number):
        if (len(roman_number) - index) >= 2:
            try:
                arabic_number += number_repository[roman_number[index] + roman_number[index + 1]]
                index += 2
            except KeyError:
                arabic_number += number_repository[roman_number[index]]
                index += 1
        else:
            arabic_number += number_repository[roman_number[index]]
            index += 1

    return str(arabic_number)


def get_calculated_expression(arabic_expression: str, roman_expression: str):

    expression_result = str(eval(arabic_expression))
    return roman_expression + "=" + expression_result
