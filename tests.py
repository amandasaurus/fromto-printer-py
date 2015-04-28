import unittest
import six
import shlex

import fromto

def output(args, input_lines):
    indata = six.StringIO("\n".join(input_lines))
    output = six.StringIO()
    fromto.main(shlex.split(args), indata, output)

    # trailing newline means there's an empty '' at the end
    return output.getvalue().split("\n")[:-1]


def _test(args, indata, expected_output):
    def test(self):
        self.assertEqual(output(args, indata), expected_output)

    return test

class FromToTestCase(unittest.TestCase):
    testSimple1 = _test('-f 2 -t 4', ['1', '2', '3', '4', '5'], ['2', '3', '4'])
    testSimple2 = _test('-F 2 -t 4', ['1', '2', '3', '4', '5'], ['3', '4'])
    testSimple3 = _test('-f 2 -T 4', ['1', '2', '3', '4', '5'], ['2', '3'])
    testSimple4 = _test('-F 2 -T 4', ['1', '2', '3', '4', '5'], ['3'])

    testOverlap1 = _test('-f 2 -t 4', ['1', '2', '3', '4', '5', '1', '2', '3', '3', '4', '5'], ['2', '3', '4', '2', '3', '3', '4'])


        

