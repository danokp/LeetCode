class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dct = Counter(s)
        flag = 0
        res = 0
        for amount in letter_dct.values():
            num, add = divmod(amount, 2)
            res += num
            if add == 1:
                flag = 1
        return res * 2 + flag
