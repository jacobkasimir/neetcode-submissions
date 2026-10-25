class MinStack:

    def __init__(self):
        self.stack =[]
        self.mini = float('inf')
        self.m2 = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.m2 = self.mini
        self.mini = min(self.mini, val)

    def pop(self) -> None:
        if self.top() == self.mini:
            self.mini = self.m2
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack)
        
