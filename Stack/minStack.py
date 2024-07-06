class MinStack(object):

    def __init__(self):
        self.min_nums = []
        self.stack = []


    def push(self, val):
        self.stack.append(val)

        if self.min_nums:
            if self.min_nums[-1] >= val:
                self.min_nums.append(val)
            else:
                self.min_nums.append(self.min_nums[-1])
        else:
            self.min_nums.append(val)


    def pop(self):
        self.stack.pop(-1)
        self.min_nums.pop(-1)

    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.min_nums[-1]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
