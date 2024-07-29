class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charMap = {}
        for r in range(len(s)):
            c = s[r]
            charMap[c] = 1 + charMap.get(c, 0)
            if (r - l + 1) - max(charMap.values()) <= k:
                res = max(res, r - l + 1)
            else:
                charMap[s[l]] -= 1
                l += 1
        return res