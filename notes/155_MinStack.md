# 155. MinStack

```python
class MinStack:

    def __init__(self):
        self.stk = [(-1, float('inf'))]

    def push(self, val: int) -> None:
        if val < self.stk[-1][-1]:
            self.stk.append((val, val))
        else:
            self.stk.append((val, self.stk[-1][-1]))

    def pop(self) -> None:
        val, _ = self.stk.pop()
        return val

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][-1]
```