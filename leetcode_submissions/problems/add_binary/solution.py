class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        add = 0
        for a_i, b_i in zip(a[::-1], b[::-1]):
            sum = add + int(a_i) + int(b_i)
            if sum == 0:
                result.append('0')
                add = 0
            elif sum == 1:
                result.append('1')
                add = 0
            elif sum == 2:
                result.append('0')
                add = 1
            else:
                result.append('1')
                add = 1
        if len(a) != len(b):
            max_num = a if len(a) > len(b) else b
            for num in max_num[abs(len(a)-len(b))-1::-1]:
                sum = add + int(num)
                if sum == 1:
                    result.append('1')
                    add = 0
                elif sum == 2:
                    result.append('0')
                    add = 1
                else:
                    result.append('0')
                    add = 0
        return ('1' if add == 1 else '') + ''.join(result[::-1])