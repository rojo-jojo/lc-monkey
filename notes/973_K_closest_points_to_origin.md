# 973. K closest points to origin

## Notes
- heapify based on the distances from the origin
- distance = (x1-x2)^2 + (y1-y2)^2 => We are not taking root of full distance because we dont care.

## Codes
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[x**2 + y**2, x, y] for x,y in points]
        heapq.heapify(points)
        res = []
        while k > 0:
            res.append(heapq.heappop(points)[1:])
            k -= 1
        return res
```
