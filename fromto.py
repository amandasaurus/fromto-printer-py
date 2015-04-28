import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fromregex', required=True)
    parser.add_argument('-t', '--toregex', required=True)

    args = parser.parse_args()

    fromregex = re.compile(args.fromregex)
    toregex = re.compile(args.toregex)

    printing = False
    for line in sys.stdin:
        line = line.rstrip("\n")
        if printing and toregex.search(line):
            # stop printing
            printing = False
        elif not printing and fromregex.search(line):
            printing = True

        if printing:
            print line

if __name__ == '__main__':
    main()
