from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Speichert Indizes von nums in absteigender Wert-Reihenfolge
        
        for i in range(len(nums)):
            # 1. Entferne Indizes, die links aus dem Fenster gefallen sind
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Entferne Elemente von hinten, die kleiner/gleich dem neuen Element sind
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            # 3. Aktuellen Index zur Deque hinzufügen
            q.append(i)
            
            # 4. Ab dem ersten vollständigen Fenster (i >= k - 1) das Maximum speichern
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res