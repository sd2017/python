import threading
import time
import Queue


class Pooler:
    def __init__(self, size,running_jobs_counter):
            print "start pooler constructor"
            self.running_jobs_counter=running_jobs_counter
            print "running_jobs_counter={0}".format(self.running_jobs_counter)
            self.list=[]
            self.jobs = Queue.Queue()
            self.mutex = threading.Lock()
            self.condition = threading.Condition(self.mutex)
            print "pooler constructor try acquire "
            self.condition.acquire()
            print "pooler constructor  acquired "
            for  index in range(0,size):
                threader=Pooler.Threader(index,self.condition,self.jobs,self.running_jobs_counter)
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
        self.jobs.put(runnabe)
        self.condition.notify()
        self.condition.release()



    def join(self):
        print "start pooler join "
        time.sleep(1.0)
        self.jobs.join()
        for threader in self.list:
            time.sleep(0.5)
            threader.join()


    class Threader(threading.Thread):
        def __init__(self,name,condition,jobs,running_jobs_counter):
            super(Pooler.Threader,self).__init__()
            self.running_jobs_counter=running_jobs_counter
            self.condition=condition
            self.jobs=jobs
            self.runnanle=None
            self.running=True
            self.name=name

            print "Threader before start"

        def run(self):
           while (self.running):
                self.runnanle = self.jobs.get(1)  #TODO blocking time
                self.condition.acquire()
                #print("run acquired {}".format(self.name))

                #if (not self.jobs.empty()):
                #   self.runnanle = self.jobs.get()
                   #self.running_jobs_counter = self.running_jobs_counter + 1
                #self.running_jobs_counter = self.running_jobs_counter + 1
                self.condition.notify()
                self.condition.release()

                if (self.runnanle != None):
                      #print "poped {0} {1}".format(self.runnanle.name, time.ctime())
                      self.runnanle.entry_time=time.ctime()
                      self.runnanle.run()
                      self.jobs.task_done()
                      self.condition.acquire()
                      self.running_jobs_counter[0] = self.running_jobs_counter[0] -1 # TODO rename running_jobs_counter to other name
                      #print "thread inside finished {0}:{1}".format(self.name,self.running_jobs_counter)
                      self.condition.notify()
                      self.condition.release()
                      self.runnanle = None
                if ( self.jobs.empty() and  self.running_jobs_counter[0]<5):
                    print "stop {0}:{1}".format(self.name,self.running_jobs_counter )
                    self.running=False



