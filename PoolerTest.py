import unittest
import time
import Pooler
class Runnable(Pooler.RunnableInterface):
    def __init__(self,num,name):
        self.delay=num
        self.name=name
    def run(self):
        time.sleep(self.delay)
        print "finished {0} {1} ".format( self.name, time.ctime())


class PoolerTest(unittest.TestCase):
        def setUp(self):
            self.pooler=Pooler.Pooler(30)
        def testFive(self):
            times=[1,2,3,4,5,1,2,3,4,5]
            names=["11","12","13","14","15","21","22","23","24","25"]
            runnables=[];
            for  time,name in zip(names,times):
                runnables.append(Runnable(time,name))
            for runnable in runnables

