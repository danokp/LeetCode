class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_dct = {
            1: 'I',
            5: 'V', 
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        res_lst = []
        div = 10
        while int(num) > 0:
            letter = ''
            num, ending = divmod(num, div)
            low_div = div/10
            inter, frac = divmod(ending, 5*low_div)
            if frac == 4*low_div:
                letter += int_to_roman_dct[low_div]
                new_frac = frac + (1 + inter * 5) * low_div
                letter += int_to_roman_dct[new_frac]
            else:
                if inter:
                    letter += int_to_roman_dct[inter*low_div*5]
                while frac > 0:
                    letter += int_to_roman_dct[low_div]
                    frac -= low_div
            num *= div
            div *= 10
            res_lst.append(letter)
        return ''.join(res_lst[::-1])