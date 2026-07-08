class MinStack:

    def __init__(self):
        self.stack = [] # standard stack (use for push, pop, and top)
        self.localMins = [] # keeps track of local min at each level, where levels range from 0 to i, i = len(stack)
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.localMins[-1] if self.localMins else val)
        self.localMins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.localMins.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.localMins[-1]
