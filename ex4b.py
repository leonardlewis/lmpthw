import argparse
import sys

parser = argparse.ArgumentParser(description="This parser is a solution to ex4.")

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help="an integer for the accumulator")
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help="sum the integers (default: find the max)")

args = parser.parse_args()
print(args.accumulate(args.integers))
