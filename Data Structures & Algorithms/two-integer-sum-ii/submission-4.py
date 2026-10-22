class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            if current_sum == target:
                return [l + 1, r + 1]  # LeetCode 167 expects 1-based indices
            elif current_sum > target:
                r -= 1
            else:
                l += 1
                
        return []