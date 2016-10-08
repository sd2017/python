import unittest
import time
import Pooler
class Runnable():
    def __init__(self,num,name):
        self.delay=num
        self.name=name
        self.entry_time=0
    def run(self):
        time.sleep(self.delay)
        print "finished {0}:{1} {2} -  {3} ".format( self.name,self.delay,self.entry_time, time.ctime())


class PoolerTest(unittest.TestCase):
        def setUp(self):
            print "start test setup"
            self.pooler=None
            print "pooler initialized"
        def testFive(self):
            print "start testFive"
            times=[1.00,2.00,8.00,4.00,1.10,8.00,4.00,5.00,7.00,1.00,1.20,9.00,1.30,1.20,3.00,1.00,1.00,1.00,1.00,1.00]
            names=["11","12","13","14","15","21","22","23","24","25","31","32","33","34","35","41","42","43","44","45"]
            self.pooler = Pooler.Pooler(5, [len(times)])

            runnables=[];
            for  time,name in zip(times,names):
                runnables.append(Runnable(time,name))
            for runnable in runnables:
                self.pooler.run(runnable)
            print "main before join"
            self.pooler.join()
            self.assertEqual(2,1)

if __name__=="__main__":
    unittest.main()