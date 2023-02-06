class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        str_max, str_min = max(strs), min(strs)
        result = ''
        i = 0
        while i < len(str_min):
            if str_min[i] != str_max[i]:
                return result
            result += str_min[i]
            i += 1
        return result