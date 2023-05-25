class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)
        for key, value_t in t_dict.items():
            if value_t != s_dict[key] or s_dict.get(key) is None:
                return key