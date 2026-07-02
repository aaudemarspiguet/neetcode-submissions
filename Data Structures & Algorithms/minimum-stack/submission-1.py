class MinStack:

    # every time we push an element e to the stack, we keep track of the min at the time of pushing e
    # a ledger dedicated to tracking the min (ie another stack)

    def __init__(self):
        self.stack = []
        self.min_stack = []
          
    def push(self, val: int) -> None:
        self.stack.append(val)
        # first element in stack is the min at that point in time
        if not self.min_stack or val < self.min_stack[-1]: # empty or value is less than current min
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1]) # carry over min to current step

    def pop(self) -> None:
        self.stack.pop()        
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]    

    def getMin(self) -> int:
        return self.min_stack[-1]
