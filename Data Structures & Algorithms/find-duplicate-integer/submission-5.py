class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        s = 0

        while slow != s:
            s = nums[s]
            slow = nums[slow]

        return s