class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, s = 0, 0
        fast = 0

        while fast < len(nums) and slow < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                while True:
                    s = nums[s]
                    slow = nums[slow]
                    if s == slow:
                        return s