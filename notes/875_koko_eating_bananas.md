# 875. Koko eating bananas

## Notes
- Run a binary search for K = [1...max(piles)] 


```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            val = sum([ceil(x / m) for x in piles])
            if val <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
```