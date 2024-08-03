# 84. Largest rectangle in histogram

## Notes
![Image 1](./images/lc_84_1.png)
![Image 2](./images/lc_84_2.png)

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] # stores (index, height)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stk and h < stk[-1][1]:
                index, height = stk.pop()
                maxArea = max(maxArea, (i - index)*height)
                start = index
            stk.append((start, h))

        for i,h in stk:
            maxArea = max(maxArea, (len(heights)- i)*h)
        return maxArea
```