# 150. Reverse polish notation

## Notes
Easy question, no notes needed

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for x in tokens:
            if stk and x in ('+','-','*','/'):
                b = int(stk.pop())
                a = int(stk.pop())
                if x == '+':
                    stk.append(a + b)
                if x == '*':
                    stk.append(a * b)
                if x == '-':
                    stk.append(a - b)
                if x == '/':
                    stk.append(a / b)
            else:
                stk.append(int(x))
        return int(stk[-1])
```