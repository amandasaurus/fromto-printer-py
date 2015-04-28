Reads in input lines from stdin, and prints out a subset of them, based on lines that match the start and end.

Traditional unix utilities (like grep) can print lines that match a regex, or treat each line as separate, handling no state.

Usage:

    usage: fromto [-h] [-f REGEX] [-F REGEX] [-t REGEX] [-T REGEX]

    optional arguments:
      -h, --help            show this help message and exit

    From regex:
      Start printing lines 'from' this line. Must not use both together.

      -f REGEX, --from-incl REGEX
                            Start 'from' this line, and print this line
      -F REGEX, --from-excl REGEX
                            Start 'from' this line, and don't print this line

    To regex:
      Stop printing line when you get 'to' a line that matches this. Must not
      use both together

      -t REGEX, --to-incl REGEX
                            Continue printing 'to' this line, and do print this
                            line
      -T REGEX, --to-excl REGEX
                            Continue printing 'to' this line, and don't print this
                            line

