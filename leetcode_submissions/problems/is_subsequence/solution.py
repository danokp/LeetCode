class Solution:
    def isSubsequence(self, sub: str, target: str) -> bool:
        if sub == "":
            return True
        count = 0
        for ch in target:
            if len(sub) == count:
                break
            if ch == sub[count]:
                count += 1
            
        return count == len(sub)