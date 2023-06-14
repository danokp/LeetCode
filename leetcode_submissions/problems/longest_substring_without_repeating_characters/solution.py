class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        stack = []

        for chr in s:
            if stack and chr in stack:
                max_len = max(len(stack), max_len)
                stack = stack[stack.index(chr)+1:]
            stack.append(chr)
        return max(len(stack), max_len)