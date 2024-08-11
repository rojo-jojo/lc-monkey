```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            small, big = q, p
        else:
            small, big = p, q
        # Condition where node splits p and q, so the node is the LCA
        if small.val <= root.val < big.val:
            return root
        # condition where both are on the left side of the node
        if big.val < root.val:
            self.lowestCommonAncestor(root.left, p, q)

        if small.val > root.val:
            self.lowestCommonAncestor(root.right, p, q)

```
