class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def inner(stng):
            stack = []
            for ch in stng:
                if stack and ch =='#':
                    stack.pop()
                elif ch != '#':
                    stack.append(ch)
            return stack
        return inner(s) == inner(t)