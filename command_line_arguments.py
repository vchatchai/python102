import sys

print(sys.argv)

import argparse

parser = argparse.ArgumentParser(prog='top', description='Show top line from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--line', type=int, default=10)
args = parser.parse_args()
print(args)


sys.stderr.write("Warning, log file not found starting a new one\n")