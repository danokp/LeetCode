class Solution:
    def tribonacci(self, n: int) -> int:
        num_1, num_2, num_3 = 0, 1, 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(n-2):
            new_num = num_1 + num_2 + num_3
            num_1, num_2, num_3 = num_2, num_3, new_num
        return new_num