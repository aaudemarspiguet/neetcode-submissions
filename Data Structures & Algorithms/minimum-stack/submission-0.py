class MinStack:

    def __init__(self):
        self.st: list = []
        self.min_st: list = []        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val < self.min_st[-1]:
            self.min_st.append(val)
        else:
            self.min_st.append(self.min_st[-1])



    def pop(self) -> None:
        del self.st[-1]
        del self.min_st[-1]
        
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]

