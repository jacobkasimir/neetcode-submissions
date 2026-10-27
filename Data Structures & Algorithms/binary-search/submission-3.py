class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        m = r // 2
        for l in range(r+1):
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif m <= r and target < nums[m]:
                r = m
                m = (m+l)//2
            else:
                l = m
                m = (m + r)//2
        return -1