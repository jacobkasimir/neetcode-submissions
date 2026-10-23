class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # 1. Populate initial window frequencies
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # 2. Count how many of the 26 alphabet characters match initially
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        l = 0
        # 3. Slide window across s2
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Character entering on right
            r_idx = ord(s2[r]) - ord('a')
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1
            elif s1_count[r_idx] + 1 == s2_count[r_idx]:  # Was equal before increment
                matches -= 1
            
            # Character leaving on left
            l_idx = ord(s2[l]) - ord('a')
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1
            elif s1_count[l_idx] - 1 == s2_count[l_idx]:  # Was equal before decrement
                matches -= 1
                
            l += 1
            
        return matches == 26