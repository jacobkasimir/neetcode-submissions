class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        seen = set()

        while i < len(nums):
            if nums and nums[i] in seen:
                return nums[i]
            seen.add(nums[i])
            i+=1
