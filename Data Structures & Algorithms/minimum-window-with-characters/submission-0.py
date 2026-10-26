from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map for characters in t
        target_counts = Counter(t)
        window_counts = {}
        
        # 'have' tracks unique chars meeting target frequency, 'need' is total unique chars in t
        have, need = 0, len(target_counts)
        
        res = [-1, -1]
        min_len = float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If current character count matches required count in t
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # Contract window from the left while it remains valid
            while have == need:
                # Update minimum window record
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = [l, r]

                # Remove left character from window
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                l += 1

        start, end = res
        return s[start : end + 1] if min_len != float('inf') else ""