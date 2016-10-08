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
            self.pooler=Pooler.Pooler(5)
            print "pooler initialized"
        def testFive(self):
            print "start testFive"
            times=[2.00,3.00,9.00,5.00,1.10,9.00,5.00,6.00,8.00,1.00,1.20,10.0,1.30,1.20,4.00,1.00,1.00,1.00,1.00,1.00]
            names=["11","12","13","14","15","21","22","23","24","25","31","32","33","34","35","41","42","43","44","45"]
            runnables=[];
            for  time,name in zip(times,names):
                runnables.append(Runnable(time,name))
            for runnable in runnables:
                self.pooler.run(runnable)

            self.pooler.join()
            self.assertEqual(2,1)

if __name__=="__main__":
    unittest.main()