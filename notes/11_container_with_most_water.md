# 11. Container with most water

## Notes

## Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxarea = 0
        while l < r:
            if height[l] < height[r]:
                maxarea = max(height[l]*(r-l), maxarea)
                l += 1
            else:
                maxarea = max(height[r]*(r-l), maxarea)
                r -= 1
        return maxarea
                
            
```
