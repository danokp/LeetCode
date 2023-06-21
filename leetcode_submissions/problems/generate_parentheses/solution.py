class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base_comb = ['(' if i % 2 == 0 else ')' for i in range(n*2)]
        # ans = [''.join(base_comb)]
        # for 
        ans = []

        def inner(l, r, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            
            if l < n:
                inner(l+1, r, s +'(')
            if r < l:
                inner(l, r+1, s + ')')
        inner(0, 0, '')
        return ans