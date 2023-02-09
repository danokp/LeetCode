class Solution:
    def mySqrt(self, x: int) -> int:
        num_min, num_max = 0, x
        while num_min <= num_max:
            mid = num_min + (num_max - num_min) // 2
            if mid ** 2 <= x and (mid+1) ** 2 > x:
                return mid
            if mid ** 2 > x:
                num_max = mid - 1
            else:
                num_min = mid + 1