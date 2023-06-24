class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for chr1, chr2 in zip_longest(word1, word2, fillvalue=''):
            ans += (chr1+chr2)

        return ans


