# 74. Search a 2-d matrix

## Notes
- Run binary search on the columns if target > matrix[row][-1] then next row
- if target < matrix[row][0] then previous row
- make sure l <= r after the loop iteration completes else return false
- then take the row as fixed and run the binary search on the column

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while l <= r:
            row = (l + r) // 2
            if matrix[row][0] > target:
                r = row - 1
            elif matrix[row][-1] < target:
                l = row + 1
            else:
                break
        if not (l <= r):
            return False
        row = (l + r) // 2
        l, r = 0, COLS - 1
        while l <= r:
            col = (l + r) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = col - 1
            elif matrix[row][col] < target:
                l = col + 1
        return False

```