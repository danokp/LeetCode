class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        cur = 0
        for h in gain:
            cur += h
            max_alt = max(max_alt, cur)
        return max_alt
