import unittest
from PermutePure import *



class  PermuteTest(unittest.TestCase):
    counter=0

    def setUp(self):
        self.actual = set()
        self.counter = 0

    def tearDown(self):
        self.counter=0

    def PermuteTest(self):
        self.counter = 0

    def testPermute(self):
        perme=permutf("abc")
        for i in range(1,6):
            res=perme.next()
            #if __debug__:
            #    print "testPermute:%s",res
            self.actual.add(res)
            self.counter=self.counter+1

        expected={('a', 'b', 'c'),('a', 'c', 'b'),('b', 'a', 'c'),('b', 'c', 'a'),('c', 'a', 'b'),('c', 'b', 'a')}
        self.assertEqual(self.actual, expected,"actual:{0}".format(self.actual))
        self.assertEqual(self.counter, 6,"actual:{0}".format(self.actual))

    def testABC(self):
        perm = Permuter()
        expected = {('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'),
                    ('c', 'b', 'a')}
        while self.counter<4 :
            if __debug__:
              self.actual.add(perm.next("abc"))
              self.counter=self.counter+1
        self.assertEqual(self.actual,expected,"actual:{0}".format(self.actual))

if __name__ == "__main__":
    unittest.main()