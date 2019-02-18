#     -type t
#             True if the file is of the specified type.  Possible file types
#             are as follows:

#             b       block special
#             c       character special
#             d       directory
#             f       regular file
#             l       symbolic link
#             p       FIFO
#             s       socket

# Why import the whole module and not pieces of it?
import argparse
from os import listdir

parser = argparse.ArgumentParser(description="Find a file and do things.")

# Argument: the directory to start searching in
# add_argument defines how the argument should be parsed.
parser.add_argument("directory", help="Provide the directory you want to search.")

# Argument: --name to filter on the files you want to find
parser.add_argument("--name", help="Provide a name to filter on when you search.")

# Argument: -print or other actions you want to take on the file
parser.add_argument("-print", action="store_true")

args = parser.parse_args()
directory = args.directory

files = listdir(directory)
target = args.name

if target in files:
    print(f"{target} is in this directory!")

if args.print:
    print(directory)
    for file in files:
        print(directory + "/" + file)
else:
    print(args)
