class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_max = ''
        substr = []
        for i, chr in enumerate(s):
            if i > 0 and chr == s[i-1]:
                substr.append(chr)
                count = 2

                for chr_sub in s[i+1:]:
                    # print(f'{chr_sub=}')
                    if i >= count and chr_sub == s[i-count]:
                        count += 1
                        substr.append(chr_sub)
                    else:
                        break
                sub = ''.join(substr[::-1] + substr)
                sub_max = max([sub_max, sub], key=len)
                substr = []
            if chr == s[i]:
                substr.append(chr)
                count = 1
                print(f'{i=}')
                for chr_sub in s[i+1:]:
                    # print(f'{chr_sub=}')
                    if i >= count and chr_sub == s[i-count]:
                        count += 1
                        substr.append(chr_sub)
                    else:
                        break
                sub = ''.join(substr[:-len(substr):-1] + substr)
                sub_max = max([sub_max, sub], key=len)
                substr = []
            print(f'{sub=}') 

        return sub_max
