# Two things to practice: writing English descripts when I get stuck and
# using a 45-minute block to focus.

import argparse

parser = argparse.ArgumentParser(description='''This script concatenates and
                                                prints the contents of some files.''')

# Take a file or set of files input on the command line and print their contents.
# If there is more than one file, print all the contents of the file in one block.

parser.add_argument("files", nargs="+", help="input file(s) to concatenate and print", metavar="File")

args = parser.parse_args()
files = args.files

for x in files:
    with open(x) as f:
        for line in f:
            print(line)

print(args)
