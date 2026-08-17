class MinStack:

    def __init__(self):
        self.container = []
        self.minContainer = []



    def push(self, val: int) -> None:
        self.container.append(val)
        val = min(self.minContainer[-1] if self.minContainer else val, val)
        self.minContainer.append(val)

    def pop(self) -> None:
        self.container.pop()
        self.minContainer.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.minContainer[-1]
