import unittest
import sys
import StringIO
import logging
from  stacmin import parser

class stackFactory():
    logger_global=1
    logger_local=2
    factory=None

    @staticmethod
    def Getfactory():
       if (stackFactory.factory==None):
           stackFactory.factory=stackFactory()
       return stackFactory.factory

    def __init__(self):
        self.loggerPolicy=None
        self.log=None
        self.pars=None

    def tearDown(self): #TODO
        pass

    def flush(self):
        self.handler.flush()

    def getlog(self):
        return self.stream.getvalue()

    def newStack( self, logger_policy=logger_global,loglevel=logging.WARN ):
        self.loggerPolicy=logger_policy
        if logger_policy == stackFactory.logger_global:
            self.log=logging
            logging.basicConfig(level=loglevel)
            self.pars = parser(self.log)
        elif logger_policy == stackFactory.logger_local:
            self.stream = StringIO.StringIO()
            self.handler = logging.StreamHandler(self.stream)
            self.log = logging.getLogger('mylogger')
            self.log.setLevel(loglevel)
            for handler in self.log.handlers:
                self.log.removeHandler(handler)
            self.log.addHandler(self.handler)
            self.pars=parser(self.log)
        else:
            pass
        return self.pars

class Stacker(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Stacker, self).__init__(*args, **kwargs)
        self.saved_stdout = sys.stdout

    def setUp(self):
        self.line = ""
        self.expected = []
        self.stack= stackFactory.Getfactory().newStack()
    def tearDown(self):
        pass #sys.stdout = self.saved_stdout

    def setSeriasBasic(self):
        self.line = "PUSH 10,PUSH 3,PUSH 1,POP,MIN,POP,MIN,PUSH 11,PUSH 7,PUSH 8,PUSH 9,MIN,POP,MIN,POP,MIN,POP,MIN"
        self.expectency = [None, None, None, 1, 3, 3, 10, None, None, None, None, 7, 9, 7, 8, 7, 7, 10]

    def testSerias(self):
        self.setSeriasBasic()
        for expected, command in zip(self.expectency, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)

    def testSeriasNoLog(self):
        self.stack = stackFactory.Getfactory().newStack(stackFactory.logger_local)
        self.setSeriasBasic()
        for expected, command in zip(self.expectency, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)
            stackFactory.Getfactory().flush()
            self.assertEqual(stackFactory.Getfactory().getlog(), '')


    def testSeriasLogDebug(self):
        self.stack = stackFactory.Getfactory().newStack(stackFactory.logger_local,logging.DEBUG)
        self.setSeriasBasic()
        for expected, command in zip(self.expectency, self.line.split(',')):
            actual = self.stack.parseLine(command)
            self.assertEqual(actual, expected)
            stackFactory.Getfactory().flush()
            self.assertEqual(stackFactory.Getfactory().getlog(), '')

if __name__ == "__main__":
    unittest.main()