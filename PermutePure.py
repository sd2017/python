import itertools

def PermuteTry(string):
    #print "premutations enumerate:{0}".format(enumerate(itertools.permutations(string)))
    #print "premutations:{0}".format(itertools.permutations(string))
    #for item in  itertools.permutations(string):
    #    print "item:{0}".format(item)
    lista=list(itertools.permutations(string))
    print "lista",lista
    #for index,item in enumerate(lista):
    #    print "enumerate{0}:{1}:".format(index,item)
    return lista

class Permuter():
    def __iter__(self):
       return self
    def next(self,string):
        if string not in self.cache:
            self.cache[string]=list(itertools.permutations(string))   #expert python programming p318
        if (string !=self.prev_string):
            self.prev_string= string
            self.iter=iter(self.cache[string])
        self.res=self.iter.next()
        return self.res

    def __init__(self):
        self.cache = {}
        self.prev_string = ""
        self.iter = None
        self.cache["abc"] = list(itertools.permutations("abc"))
        self.lista = self.cache["abc"]
        #print "Permuter {0}".format(self.cache)
        #print "lista {0}".format(self.lista)
        self.res = None
        self.iter = iter(self.lista)

def permutf(string ):
    lista=list(itertools.permutations(string))
    print "lista {0}".format(lista)
    #a,b=0,1
    itera = iter(lista)
    item = "".join(itera.next())
    while True:
        #yield b
        yield item
        #a,b=b,a+b
        item = "".join(itera.next())

if __name__=="__main__":

    permf=permutf("abc")
    for ind in xrange(1, 7):
        print "loop ff#{0}:{1}".format(ind, permf.next())

    perme = permutf("abcde")
    for ind in xrange(1, 7):
        print "loop ff#{0}:{1}".format(ind, perme.next())

    perm = Permuter()
    for ind in xrange(1,7):
        print "loop permuter#{0}:{1}".format(ind,perm.next("abc"))
