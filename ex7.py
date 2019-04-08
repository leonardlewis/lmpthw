import argparse
import re

parser = argparse.ArgumentParser(description="Search a file for a regex pattern.")

parser.add_argument("pattern", nargs="*", help="Provide the pattern you want to search on")

parser.add_argument("file", help="Provide the file you want to search on")

args = parser.parse_args()

# import the contents of a file
file = open(args.file, "r")

# search the file for a pattern that matches the input
for line in file:
    for x in args.pattern:
        if re.search(x, line):
            print(line)
