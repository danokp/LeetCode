class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return Solution.isPowerOfTwo(self, n // 2)
        return False