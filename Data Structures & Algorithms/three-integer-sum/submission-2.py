class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            # 1. Skip duplicate starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 2. Search strictly to the right of i
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1  # 3. Move pointers to find other potential pairs for 'i'
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        # 4. Convert tuples back to lists
        return [list(t) for t in res]