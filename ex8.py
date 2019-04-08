import argparse

parser = argparse.ArgumentParser(description="Cut out sections from a line of text.")

parser.add_argument("text", help="Line of text to cut.")

parser.add_argument("-d", help="Delimiter for the input text.")

parser.add_argument("-f", help="Fields to cut.")

args = parser.parse_args()
