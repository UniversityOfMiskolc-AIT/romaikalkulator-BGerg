arabic_numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

special_roman_numbers = {
    "IV": 4,
    "IX": 9,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


def exchange_to_arabic(roman_number: str) -> int:
    a = 0
    i = 0
    while i < len(roman_number):
        if (len(roman_number) - i) >= 2:
            try:
                a += special_roman_numbers[roman_number[i]+roman_number[i+1]]
                i += 2
            except KeyError:
                a += arabic_numbers[roman_number[i]]
                i += 1
        else:
            a += arabic_numbers[roman_number[i]]
            i += 1

    return a


