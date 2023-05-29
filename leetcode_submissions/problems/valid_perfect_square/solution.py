class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        prev, cur = 1, num // 2
        while cur >= prev:
            mid = (cur + prev) // 2
            sq = mid ** 2
            if sq == num:
                return True
            if sq > num:
                cur = mid - 1
            else:
                prev = mid + 1
        return False
