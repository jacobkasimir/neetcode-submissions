class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = {}  # Format: {Zeichen: Index}

        for r, c in enumerate(s):
            # Wenn das Zeichen bereits im aktuellen Fenster liegt:
            if c in seen:
                l = max(l, seen[c] + 1)
            
            # Index des Zeichens immer auf den neuesten Stand bringen
            seen[c] = r
            
            # Maximale Fensterlänge festhalten
            max_len = max(max_len, r - l + 1)

        return max_len