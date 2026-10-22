class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = -1
        while l < r:
            maxi = max(maxi,(r - l) * min(heights[l], heights[r]))
            if (heights[r] > heights[l]):
                l += 1
            else:
                r -= 1
        return maxi