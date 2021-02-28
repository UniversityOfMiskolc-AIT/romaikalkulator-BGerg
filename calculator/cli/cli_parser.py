import argparse


def parse():
    parser = argparse.ArgumentParser(description='Read account numbers from file in seven digit format'
                                                 ', check correctness and write to a new file in normal digit format.',
                                     epilog='Enjoy the digital world! :)')

    parser.add_argument('roman_expression',
                        metavar='Roman expression',
                        type=str,
                        help='Needs a math expression with roman numbers e.g. I+IV*2 ')



    return parser.parse_args()
