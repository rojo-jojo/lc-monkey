# 138. Copy of list with random pointer

## Explanation
Create a hashmap where key is the curr node and value is a copy of that node
1. In the first pass add all the current to copy nodes pairs to hashmap
2. in the second pass update the next and random pointers of the copy hashmap

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]s
```