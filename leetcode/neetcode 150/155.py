class MinStack:

    def __init__(self):
        self.mn = [] 
        self.stack = [] 
    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = min(val, self.mn[-1] if self.mn else val) 
        self.mn.append(temp) 

    def pop(self) -> None: 
        self.stack.pop() 
        self.mn.pop() 

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.mn[-1] 
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()