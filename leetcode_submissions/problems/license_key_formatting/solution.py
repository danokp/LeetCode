class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        count = 0
        for chr in s[::-1]:
            if count == k:
                ans.append('-')
                count = 0
            if chr == '-':
                continue
            count += 1
            ans.append(chr.upper())
        return ''.join(ans[::-1]).strip('-')


        