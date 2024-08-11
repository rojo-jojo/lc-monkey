# 235. Lowest common ancestor in a binary search trei

## Notes
If p and q are to the left and right of the root then root is the lca

else we move to the left or the right of the tree based on where both p and q are located

do this iteratively in a while loop

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNode') -> 'TreeNode':
        cur = root
        while True:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

```
