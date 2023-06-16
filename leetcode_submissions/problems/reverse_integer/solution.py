class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:
            x_new = int(str(x)[::-1])
        else:
            x_new = -int(str(x)[:0:-1])
        if abs(x_new) > 2_147_483_647:
            return 0
        return x_new