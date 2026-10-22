class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums is []:
            return []
        res = set()
        a = set()
        for i in range(len(nums)):
            r = len(nums) - 1
            l = i + 1
            if i in a:
                continue
            a.add(i)
            while l < r:
                if i == r:
                    r -= 1
                elif i == l:
                    l += 1
                if (nums[l] + nums[r] == - nums[i]):
                    res.add((nums[l], nums[r], nums[i]))
                    l += 1
                elif (nums[l] + nums[r] > - nums[i]):
                    r -= 1
                else:
                    l += 1
        return [i for i in res]
            
                