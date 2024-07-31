# 2. Add two numbers

## Notes
Remember to run the while loop till one of the linkedlist is non empty or there is a carry left

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        cur = l3
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sumval = a + b + carry
            carry = sumval // 10
            sumval %= 10
            cur.next = ListNode(sumval)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next
```

