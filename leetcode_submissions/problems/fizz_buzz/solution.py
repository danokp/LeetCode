class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for num in range(1, n+1):
            s_i = ''
            if num % 3 == 0:
                s_i += "Fizz"
            if num % 5 == 0:
                s_i += "Buzz"
            if s_i == '':
                s_i = str(num)
            result.append(s_i)
        return result