import sys
import traceback
import cgitb
import logging

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
    def execute(self):
        return



class push(commander):
    def __init__(self):
       self.num_parameters=1
       self.value = 0
       self.has_res = False

    def execute(self ):
        self.stack_min.push(self.value)
        return None

class pop(commander):
    def execute(self):
        res = self.stack_min.pop()
        return res


class min(commander):
    def execute(self):
        res = self.stack_min.min()
        return res


class parser:
    def __init__(self, logger):
        self.logger=logger
        commander.set_stack(StakMin())
        self.StackMin = min()
        self.StackPush = push()
        self.StackPop = pop()
        self.res=None
        self.Command =None
        self.commands={"PUSH":self.StackPush,"POP":self.StackPop,"MIN":self.StackMin}

    def parseLine(self, line):
        Delimeters = ','
        commands = line.split(Delimeters)
        res=None
        for command in commands:
            spacers = ' '
            parameters = command.split(spacers)
            res=self.parse(parameters)
        return res

    def parse(self, parameters):
            self.Command = self.commands[parameters[0]]
            if (self.Command.num_parameters==1):
               self.Command.value = int(parameters[1])
            self.logger.info( parameters)
            self.res=self.Command.execute()
            if (self.Command.has_res):
               self.logger.info("res %s " % (self.res))
            return self.res


if __name__ == "__main__":
    # try:
    test1 = parser()
    test1.parseLine("PUSH 10,PUSH 3,PUSH 1,POP,MIN,POP,MIN,PUSH 11,PUSH 7,PUSH 8,PUSH 9,MIN,POP,MIN,POP,MIN,POP,MIN")
    # except:
    #    traceback.print_tb(10)
