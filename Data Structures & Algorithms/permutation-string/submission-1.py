from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])
        
        if s1_counts == window_counts:
            return True
            
        # Slide the window across s2
        for i in range(n1, n2):
            # Add new character entering the window
            window_counts[s2[i]] += 1
            
            # Remove character leaving the window
            left_char = s2[i - n1]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char]
                
            # Check if current window matches s1's frequency
            if window_counts == s1_counts:
                return True
                
        return False