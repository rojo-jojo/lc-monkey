# 543. Diameter of Binary Tree

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(cur):
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            self.res = max(self.res, left + right)
            # 1 is added below because your add the length the of left and right edge
            # and then add the length of the root edge also to get the height
            return 1 + max(left, right)
        dfs(root)
        return self.res
```