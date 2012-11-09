class Calculator(object):
    def __init__(self):
        self._stack = []

    def push(self, num):
        self._stack.append(num)

    def add(self):
        op1 = self._stack.pop()
        op2 = self._stack.pop()
        return op1 + op2
