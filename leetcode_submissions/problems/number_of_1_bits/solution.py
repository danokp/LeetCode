class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        d = Counter(bin(n)[2:])
        return d['1']
