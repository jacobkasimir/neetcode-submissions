class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        res = 0
        for num in h:
            if num-1 in h: 
                continue
            else: 
                streak=0
                while(num + streak in h):
                    streak += 1
                    res = max(streak, res)

        return res