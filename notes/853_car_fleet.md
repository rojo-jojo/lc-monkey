# 853. Car fleet

# Notes
- Sort the cars in reverse order based on position and speed
- Put time taken by each car to reach the end in a stack
- If the time taken by the current car is less than the previous car then pop from the stack
- return len of the stack

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        fleeter = [(p,s) for p,s in zip(position, speed)]
        for p,s in sorted(fleeter, reverse=True):
            stk.append((target - p)/s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)

```