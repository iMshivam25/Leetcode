class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.limit = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.limit:
            pass
        else:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        for idx in range(0,min(k,len(self.stack))):
            self.stack[idx]+=val 
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)