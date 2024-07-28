from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res_max = 0
        for n in nums:
            if (n - 1) not in setnums:
                length = 0
                while (n + length) in setnums:
                    length += 1
                res_max = max(res_max, length)
        return res_max