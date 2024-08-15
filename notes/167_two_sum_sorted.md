# 167 Two sum II - sorted array

## Notes
- Start left pointer from beginning and right from end

## Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sumnum = numbers[l] + numbers[r]
            if sumnum == target:
                return [l+1, r+1]
            elif sumnum > target:
                r -= 1
            elif sumnum < target:
                l += 1
```
