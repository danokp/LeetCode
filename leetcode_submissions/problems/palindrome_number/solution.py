class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        for i in range(len(x_str) // 2):
            if x_str[i] != x_str[-i-1]:
                return False
        return True
