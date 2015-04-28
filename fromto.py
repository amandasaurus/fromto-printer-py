import argparse
import re
import sys

def main(args=None, indata=None, outdata=None):
    args = args or sys.argv[1:]
    indata = indata or sys.stdin
    outdata = outdata or sys.stdout

    parser = argparse.ArgumentParser()
    from_grp = parser.add_argument_group("From regex", "Start printing lines 'from' this line.\nMust not use both together.")
    from_grp.add_argument('-f', '--from-incl', metavar="REGEX", help="Start 'from' this line, and print this line")
    from_grp.add_argument('-F', '--from-excl', metavar="REGEX", help="Start 'from' this line, and don't print this line")
    
    to_grp = parser.add_argument_group("To regex", "Stop printing line when you get 'to' a line that matches this.\nMust not use both together")
    to_grp.add_argument('-t', '--to-incl', metavar="REGEX", help="Continue printing 'to' this line, and do print this line")
    to_grp.add_argument('-T', '--to-excl', metavar="REGEX", help="Continue printing 'to' this line, and don't print this line")

    args = parser.parse_args(args)

    if args.from_excl is not None and args.from_incl is not None:
        sys.stderr.write("Overlapping -f & -F\n")
        return

    if args.to_excl is not None and args.to_incl is not None:
        sys.stderr.write("Overlapping -t & -T\n")
        return

    from_incl = False
    if args.from_excl:
        fromregex = re.compile(args.from_excl)
        from_incl = False
    elif args.from_incl:
        fromregex = re.compile(args.from_incl)
        from_incl = True
    else:
        fromregex = None


    to_incl = False
    if args.to_excl:
        toregex = re.compile(args.to_excl)
        to_incl = False
    elif args.to_incl:
        toregex = re.compile(args.to_incl)
        to_incl = True
    else:
        toregex = None


    printing = False

    for line in indata.readlines():

        if printing:
            if toregex and toregex.search(line):
                # stop printing
                printing = False
                if to_incl:
                    outdata.write(line)
            else:
                outdata.write(line)
        else:
            if fromregex and fromregex.search(line):
                printing = True
                if from_incl:
                    outdata.write(line)


if __name__ == '__main__':
    main()
