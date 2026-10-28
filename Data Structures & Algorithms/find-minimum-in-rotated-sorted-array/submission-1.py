class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        le = len(nums)
        r = le - 1 

        while l < r:
            begin = (l + r) // 2
            n = nums[begin]

            if n <= nums[r]:
                r = begin
            else:
                l = begin + 1

        return nums[l]