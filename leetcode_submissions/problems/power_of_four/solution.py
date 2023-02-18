class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bin_n = bin(n).replace("0b", "")
        if bin_n[0] == '1' and bin_n.replace('00', '') == '1':
            return True
        return False