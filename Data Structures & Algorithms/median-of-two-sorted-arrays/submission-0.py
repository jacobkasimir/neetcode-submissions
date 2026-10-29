from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2

        # Always run binary search on the smaller array for O(log(min(m, n)))
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2      # Partition index for A
            j = half - i          # Partition index for B

            # Handle out-of-bound boundary conditions using infinity
            A_left  = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i]     if i < len(A) else float('inf')
            B_left  = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j]     if j < len(B) else float('inf')

            # Correct partition found
            if A_left <= B_right and B_left <= A_right:
                # Odd total length: max of left side is the median
                if total % 2 == 1:
                    return float(max(A_left, B_left))
                # Even total length: average of max(left) and min(right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            # Too many elements taken from A -> move left
            elif A_left > B_right:
                r = i - 1
            # Too few elements taken from A -> move right
            else:
                l = i + 1

        return 0.0




