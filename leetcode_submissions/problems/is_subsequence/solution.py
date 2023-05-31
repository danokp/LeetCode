class Solution:
    def isSubsequence(self, sub: str, target: str) -> bool:
        stack = list(sub)

        for chr in target[::-1]:
            if stack and stack[-1] == chr:
                stack.pop(-1)
        return len(stack) == 0
