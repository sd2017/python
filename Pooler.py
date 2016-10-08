import threading


class RunnableInterface:
    def run(self):
        pass


class Threader(threading.Thread):
    def __init__(self):
        super(Threader,self).__init__(self.global_run)
        self.runnanle = RunnableInterface()
        self.run()
    def lock(self):
        pass

    def global_run(self):
       while (True):
        self.lock()
        if (self.runnanle != None):
           self.runnanle.run()
           self.runnanle=None



class Pooler:
    def __init__(self, size):
        self.free = []
        self.list=[]>?>?>?
            threader=Threader()