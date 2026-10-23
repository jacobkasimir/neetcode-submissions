class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        # 1. Track required character counts for s1
        count = [0] * 26
        for c in s1:
            count[ord(c) - 97] += 1
        
        l = 0
        for r in range(n2):
            r_idx = ord(s2[r]) - 97
            count[r_idx] -= 1
            
            # 2. If we took too many of s2[r] (or an invalid character),
            # shrink 'l' until s2[r] count is no longer negative
            while count[r_idx] < 0:
                count[ord(s2[l]) - 97] += 1
                l += 1
            
            # 3. Valid window condition: window size matches len(s1)
            if r - l + 1 == n1:
                return True
                
        return False