# 110. Balanced Binary Tree

## Notes
 - Base condition:  if the root is none return then return true and height 0
 - height at root = 1 + max(left_subtree_height, right_subtree_height)
 - Tree is balanced if this is true for every node
    - Left subtree is balanced
    - Right subtree is balanced
    - abs(left_subtree_height - right_subtree_height) <= 1

## Code
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (True, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return (balanced, 1 + max(left[1], right[1]))
        return dfs(root)[0]

```