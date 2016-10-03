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
        #self.stack = parser(sys.stdout,logging.DEBUG)
        self.stack = parser( logging)

    def tearDown(self):
        pass #sys.stdout = self.saved_stdout


    def rollout(self):
        pass #sys.stdout = self.saved_stdout

    def setSeriasBasic(self):
        self.line = "PUSH 10,PUSH 3,PUSH 1,POP,MIN,POP,MIN,PUSH 11,PUSH 7,PUSH 8,PUSH 9,MIN,POP,MIN,POP,MIN,POP,MIN"
        self.expectency = [None, None, None, 1, 3, 3, 10, None, None, None, None, 7, 9, 7, 8, 7, 7, 10]

    def testSerias(self):
        logging.basicConfig( level=logging.ERROR)
        self.setSeriasBasic()
        for expected, command in zip(self.expectency, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)

    def t_estSeriasNoPrint(self):
        self.out = StringIO.StringIO()
        try:
             sys.stdout = self.out
             sys.stderr = self.out
        except:
             raise

        self.stack = parser(self.out,logging.DEBUG)
        self.setSeriasBasic()
        try:
            for expected, command in zip(self.expectency, self.line.split(',')):
                actual = self.stack.parseLine(command)
                self.assertEqual(actual, expected)

            expected_out = "a"
            expected_output_as_bytes = expected_out.encode(encoding='UTF-8')
            self.assertEqual(self.out.getvalue(), expected_output_as_bytes)
        finally:
           logging.debug( self.out.getvalue())
           print "outputfff", self.out.getvalue()


    def testSeriasLogger(self):
        self.stream = StringIO.StringIO()
        self.handler = logging.StreamHandler(self.stream)
        self.log = logging.getLogger('mylogger')
        self.log.setLevel(logging.ERROR)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)
        self.stack = parser(self.log)
        self.setSeriasBasic()
        for expected, command in zip(self.expectency, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)
            self.handler.flush()
            #print '[', self.stream.getvalue(), ']'
            self.assertEqual(self.stream.getvalue(), '')



if __name__ == "__main__":
    unittest.main()