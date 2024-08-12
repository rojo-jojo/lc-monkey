# 1448. Count good nodes in a tree

## Notes
- DFS question
- Keep track of the max value in the path previous to current node
- add 1 to the return if current node >= previous max

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if not node:
                return 0
            res = 1 if node.val >= cur_max else 0
            cur_max = max(cur_max, node.val)
            res += dfs(node.left, cur_max)
            res += dfs(node.right, cur_max)
            return res
        return dfs(root, root.val)
```
