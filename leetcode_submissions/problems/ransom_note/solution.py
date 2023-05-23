class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransomNote_d = Counter(ransomNote)
        magazine_d = Counter(magazine)
        for key, value in ransomNote_d.items():
            if value > magazine_d[key]:
                return False
        return True