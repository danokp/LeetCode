class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.find('LLL') == -1 and s.count('A') < 2
