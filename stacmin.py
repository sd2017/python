import sys
import traceback
import cgitb


cgitb.enable(format='text')


class StakMin:
    MAXNUMBER = sys.maxint - 1

    def __init__(self):
        self.stack = []
        self.istack = []
        self.minValue = self.MAXNUMBER

    def push(self, Value):
        self.stack.append(Value)
        if (Value < self.minValue):
            self.istack.append(Value)
            self.minValue = Value

    def pop(self):
        if (self.stack.__len__() == 0):
            return self.minValue

        Value = self.stack[-1]
        self.stack.pop()
        if (Value == self.minValue):
            self.istack.pop()
            if (self.istack.__len__() == 0):
                self.minValue = StakMin.MAXNUMBER
            else:
                self.minValue = self.istack[-1]

        return Value

    def min(self):
        return self.minValue




class commander:
    stack_min = None;

    def __init__(self):
       self.num_parameters=0
       self.value = 0
       self.has_res = True
    @staticmethod
    def set_stack(inn):
        commander.stack_min=inn
    def execute(self, value):
        return



class push(commander):
    def __init__(self):
       self.num_parameters=1
       self.value = 0
       self.has_res = False

    def execute(self, value ):
        self.stack_min.push(value)
        return self.value

class pop(commander):
    def execute(self,value):
        res = self.stack_min.pop()
        return res


class min(commander):
    def execute(self,value):
        res = self.stack_min.min()
        return res


class tester:
    def __init__(self):
        commander.set_stack(StakMin())
        self.StackMin = min()
        self.StackPush = push()
        self.StackPop = pop()

        self.Command =None
        self.commands={"PUSH":self.StackPush,"POP":self.StackPop,"MIN":self.StackMin}
    def parseSecond(self, parameters):

        num = int(parameters[1])
        return num

    def parsecom(self, line):
        Delimeters = ','
        commands = line.split(Delimeters)
        for command in commands:
            spacers = ' '
            parameters = command.split(spacers)
            self.parseSingle(parameters)

    def parseSingle(self, parameters):
            num = 0
            self.Command = self.commands[parameters[0]]
            if (self.Command.num_parameters==1):
               num = self.parseSecond(parameters)
            print parameters
            res=self.Command.execute(num)
            if (self.Command.has_res):
               print("res %s " % (res))
            #print("stack %s " % (self.Command.stack_min.stack))


def test():
    test1 = tester()

    test1.parsecom("PUSH 10,PUSH 3,PUSH 1,POP,MIN,POP,MIN,PUSH 11,PUSH 7,PUSH 8,PUSH 9,MIN,POP,MIN,POP,MIN,POP,MIN")


if __name__ == "__main__":
    # try:
    test()
    # except:
    #    traceback.print_tb(10)
