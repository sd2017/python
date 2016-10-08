import threading
import time



class Pooler:
    def __init__(self, size):
            print "start pooler constructor"
            self.running_jobs_counter=0
            self.list=[]
            self.jobs = []
            self.condition = threading.Condition()
            print "pooler constructor try acquire "
            self.condition.acquire()
            print "pooler constructor  acquired "
            for  index in range(0,size):
                threader=Pooler.Threader(self.condition,self.jobs,self.running_jobs_counter)
                self.list.append(threader)
            print "pooler constructor  created threads  "
            for threader in self.list:
                threader.start()
            print "pooler constructor  started threads  "
            self.condition.notify()
            print "pooler constructor  notified  "
            self.condition.release()
            print "finished pooler constructor"

    def run(self,runnabe):
        #print "entering global run"
        self.condition.acquire()
        #print " global run acuire lock"
        self.jobs.append(runnabe)
        self.condition.notify()
        self.condition.release()

    def join(self):
        print "start pooler join "
        time.sleep(1.0)
        while ( self.jobs):
            pass
        if (not self.jobs):
            print "iterating join "
            while (self.running_jobs_counter>0):
              print "join waiting {0}".format(self.running_jobs_counter)
            for threader in self.list:
                 threader.join()


    class Threader(threading.Thread):
        def __init__(self,condition,jobs,running_jobs_counter):
            super(Pooler.Threader,self).__init__()
            self.running_jobs_counter=running_jobs_counter
            self.condition=condition
            self.jobs=jobs
            self.runnanle=None
            self.running=True
            print "Threader before start"

        def run(self):
           while (self.running):
                self.condition.acquire()
                if (self.jobs):
                   self.runnanle = self.jobs.pop()
                   self.running_jobs_counter=self.running_jobs_counter+1
                self.condition.notify()
                self.condition.release()

                if (self.runnanle != None):
                      #print "poped {0} {1}".format(self.runnanle.name, time.ctime())
                      self.runnanle.entry_time=time.ctime()
                      self.runnanle.run()
                      self.condition.acquire()
                      self.running_jobs_counter = self.running_jobs_counter -1
                      self.condition.notify()
                      self.condition.release()
                      if ((not self.jobs) and self.running_jobs_counter ==0):
                          self.running=False
                      self.runnanle=None


