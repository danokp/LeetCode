class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for br in s:
            if br in bracket_dict:
                stack.append(br)
            elif len(stack) == 0 or bracket_dict[stack.pop()] != br:
                return False
        return len(stack) == 0