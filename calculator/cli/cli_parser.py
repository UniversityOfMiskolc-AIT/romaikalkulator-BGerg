import argparse


def parse():
    parser = argparse.ArgumentParser(description='Read account numbers from file in seven digit format'
                                                 ', check correctness and write to a new file in normal digit format.',
                                     epilog='Enjoy the digital world! :)')

    parser.add_argument('input_file',
                        metavar='Input file name',
                        type=str,
                        help='Seven digit format account numbers read from this file')

    parser.add_argument('-s',
                        '--saveto',
                        action='store',
                        type=str,
                        default='report.txt',
                        metavar='',
                        help='Set output file name for account number')

    return parser.parse_args()
