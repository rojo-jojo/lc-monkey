class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2] , [3,4]
        # if A[-1]  <= B[0] = normally calculate median value
        # if case like this [1,3,7], [2,4,5]
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1
        
        while True:
            i = (l + r) // 2
            j = half - (i + 1) - 1
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1