class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        mink = max(max(piles),h)
        r = mink
        while l <= r:
            k = (l + r) // 2
            s = 0
            for i in piles:
                s += math.ceil(i / k)
            if s > h:
                l = k + 1
            else:
                mink = min(mink, k)
                r = k - 1

        return mink
