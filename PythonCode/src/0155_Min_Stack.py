class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        if tmp == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = float("inf")
        return tmp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

