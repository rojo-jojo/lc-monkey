# 153. Find minimum in rotated sorted array

## Notes
- Determine if you are in the left sorted array or the right sorted array
- If in the left sorted then move to the right sorted
- check if the current minimum value is less than nums[mid]
- If you are in a sorted part of the array, i.e. nums[l] < nums[r] then nums[l] is the minimum value and we break

## Code
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res
            
```