class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        lucky = [num for num, f in freq.items() if num == f]
        
        return max(lucky) if lucky else -1