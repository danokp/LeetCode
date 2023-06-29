class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        first_ltter = ''
        prev_index = -1
        s_lst = list(s)

        l, r = 0, len(s_lst) - 1

        while l <= r:
            if s_lst[l].lower() not in vowels:
                l += 1
            if s_lst[r].lower() not in vowels:
                r -= 1
            else:
                if s_lst[l].lower() in vowels:
                    s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
                    r -= 1
                    l += 1

        return ''.join(s_lst)



