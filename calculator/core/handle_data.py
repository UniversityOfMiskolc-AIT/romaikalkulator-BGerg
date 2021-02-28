import calculator.core.numbers as numbers



def convert_expression_to_arabic(expression: str):
    roman_number = ""
    arabic_expression = ""
    for elem in expression:
        if elem == "+" or elem == "-" or elem == "*" or elem == " ":
            arabic_expression += convert_roman_to_arabic(roman_number)
            arabic_expression += elem
            roman_number = ""
        elif elem == "/":
            arabic_expression += convert_roman_to_arabic(roman_number)
            arabic_expression += "//"
            roman_number = ""
        else:
            roman_number += elem

    arabic_expression += convert_roman_to_arabic(roman_number)  # add last number to the expression
    return arabic_expression


def convert_roman_to_arabic(roman_number: str) -> str:
    arabic_number = 0
    index = 0

    while index < len(roman_number):
        if (len(roman_number) - index) >= 2:
            try:
                arabic_number += numbers.number_repository[roman_number[index] + roman_number[index + 1]]
                index += 2
            except KeyError:
                arabic_number += numbers.number_repository[roman_number[index]]
                index += 1
        else:
            arabic_number += numbers.number_repository[roman_number[index]]
            index += 1

    return str(arabic_number)


def get_calculated_expression(arabic_expression: str, roman_expression: str):
    expression_result = convert_arabic_to_roman(str(eval(arabic_expression)))
    return roman_expression + "=" + expression_result

def convert_arabic_to_roman(arabic_number: str):
    roman_number = ""

    key_list = list(numbers.number_repository.keys())
    val_list = list(numbers.number_repository.values())

    for place_value in range(len(arabic_number)):

        value = arabic_number[place_value]
        number_pattern = value+ (len(arabic_number) - place_value - 1) * "0"
        try:
            position = val_list.index(int(number_pattern))
            roman_number += key_list[position]
        except ValueError:
            if int(value) < 5:
                number_pattern = "1" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += key_list[position] * int(value)
            else:
                number_pattern = "5" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += key_list[position]
                number_pattern = "1" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += (key_list[position] * (int(value) - 5))

    return roman_number
