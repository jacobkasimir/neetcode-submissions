class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        counts = {}
        max_len = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_freq = max(max_freq, counts[s[r]])

            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len
