# 33. Search in a rotated sorted array

## Notes
- Check if we are in the left sorted array
- If in left sorted array and the target is towards the right then l = m + 1
- Else r = m - 1
- If in the right sorted array and the target is towards the left r = m - 1
- Else l = m + 1

## Code 

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m -1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
```