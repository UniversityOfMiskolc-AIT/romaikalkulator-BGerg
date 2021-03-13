import argparse


def parse():
    parser = argparse.ArgumentParser(description='Calculate mathematical expression in roman number format.'
                                                 'The application works with maximum value 3999.'
                                                 'Input format e.g. I+IV*II --> output I+IV*II=IX',
                                     epilog='All way lead to roma :)')

    parser.add_argument('roman_expression',
                        metavar='Roman expression',
                        type=str,
                        help='Needs a math expression with roman numbers e.g. I+IV*II ')



    return parser.parse_args()
