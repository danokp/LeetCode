class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for num in range(1, n+1):
            cur = 0
            while num:
                cur += num & 1
                num >>= 1
            res.append(cur)
        return res
