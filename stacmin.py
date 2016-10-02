import sys
import traceback
import cgitb
from enum import Enum

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


# class push
# class pop
# class min
# class commander
class CommandType():
    PUSH = 0
    POP = 1
    MIN = 2

    def __init__(self):
        pass

    def tostring(self, val):
        #members = [attr for attr in dir(self) if not callable(getattr(self,attr)) and not attr.startswith("__")]
        #print members
        members = {0: "PUSH", 1: "POP", 2: "MIN"}
        return members[val]
        #for k, v in vars(CommandType()).iteritems():
        #    if v == val:
        #        return k

    def fromstring(self, str):
        # type: (object, object) -> object
        return getattr(self, str.upper(), None)


class commander:
    stack_min = StakMin()



    def execute(self, Value):
        return

    def executenv(self):
        Value = self.stack_min.min()
        return Value


class push(commander):
    def execute(self, Value):
        self.stack_min.push(Value)


class pop(commander):
    def executenv(self):
        res = self.stack_min.pop()
        return res


class min(commander):
    def executenv(self):
        res = self.stack_min.min()
        return res


class tester:
    def __init__(self):
        self.StackMin = min()
        self.StackPush = push()
        self.StackPop = pop()
        self.CommandEnum = CommandType()
        self.Command =pop()
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
        command_enum = self.CommandEnum.fromstring(parameters[0])
        # if command_enum is CommandType:
        #     pass
        # else:
        #     command_enum=None

        num = StakMin.MAXNUMBER
        command_size = 1
        res = StakMin.MAXNUMBER
        if command_enum == CommandType.MIN:
            self.Command = self.StackMin

        elif command_enum == CommandType.POP:
            self.Command = self.StackPop

        elif command_enum == CommandType.PUSH:
            self.Command = self.StackPush
            num = self.parseSecond(parameters)
            res = num
            command_size = 2

        else:
            pass
        tmp = self.CommandEnum.tostring(command_enum)
        #print("command %d %s " % (command_enum,self.CommandEnum.tostring(command_enum)))
        print("command  %s " % ( self.CommandEnum.tostring(command_enum)))
        if command_size == 1:
            res = self.Command.executenv()

        elif command_size == 2:
            self.Command.execute(num)

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
