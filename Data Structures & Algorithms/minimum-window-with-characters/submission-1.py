class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Fixed 128-element ASCII arrays (faster than dict/Counter)
        target = [0] * 128
        window = [0] * 128
        
        need = 0
        for char in t:
            code = ord(char)
            if target[code] == 0:
                need += 1
            target[code] += 1

        # Filter s: keep only (original_index, char) for characters in t
        filtered_s = [(i, char) for i, char in enumerate(s) if target[ord(char)] > 0]

        have = 0
        l = 0
        min_len = float('inf')
        res = (-1, -1)

        for r, (s_idx, char) in enumerate(filtered_s):
            code = ord(char)
            window[code] += 1

            if window[code] == target[code]:
                have += 1

            # Contract window from the left while valid
            while have == need:
                start_idx, left_char = filtered_s[l]
                current_len = s_idx - start_idx + 1

                if current_len < min_len:
                    min_len = current_len
                    res = (start_idx, s_idx)

                left_code = ord(left_char)
                window[left_code] -= 1
                if window[left_code] < target[left_code]:
                    have -= 1
                l += 1

        start, end = res
        return s[start : end + 1] if min_len != float('inf') else ""