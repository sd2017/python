import unittest
import sys
import StringIO
import logging
from  stacmin import parser


class Stacker(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Stacker, self).__init__(*args, **kwargs)
        self.saved_stdout = sys.stdout

    def setUp(self):
        self.line = ""
        self.expected = []
        self.stack = parser()

    def tearDown(self):
        sys.stdout = self.saved_stdout


    def rollout(self):
        sys.stdout = self.saved_stdout

    def setSeriasBasic(self):
        self.line = "PUSH 10,PUSH 3,PUSH 1,POP,MIN,POP,MIN,PUSH 11,PUSH 7,PUSH 8,PUSH 9,MIN,POP,MIN,POP,MIN,POP,MIN"
        self.expecteds = [None, None, None, 1, 3, 3, 10, None, None, None, None, 7, 9, 7, 8, 7, 7, 100]

    def testSerias(self):
        self.stack = parser(logging.DEBUG)
        self.setSeriasBasic()
        for expected, command in zip(self.expecteds, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)

    def testSeriasNoPrint(self):
        self.out = StringIO.StringIO()
        try:
            pass #sys.stdout = self.out
        except:
            raise

        self.stack = parser(logging.DEBUG)
        self.setSeriasBasic()
        try:
            for expected, command in zip(self.expecteds, self.line.split(',')):
                actual = self.stack.parseLine(command)
                self.rollout();
                self.assertEqual(self.out.getvalue(), "")
                self.assertEqual(actual, expected)

        finally:
           print "output", self.out.getvalue()

if __name__ == "__main__":
    unittest.main()