# 3. Longest subtring with repeating characters

## Notes
- Use a set to store values
- Go through each character in the string
- while a character in string is already present in the set =>
  - keep removing elements from the left of the set
  - increment the left
- result is the max size of window after a new non existing element is added to the set

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```
