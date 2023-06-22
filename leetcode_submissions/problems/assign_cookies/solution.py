class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse=True)
        s.sort()
        for g_i in g:
            for index_s in range(len(s)):
                if s[index_s] >= g_i:
                    count += 1
                    s.pop(index_s)
                    break
        return count
