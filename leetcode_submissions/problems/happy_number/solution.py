class Solution:
    def isHappy(self, n: int) -> bool:
        save_list = []
        while n != 1:
            n = sum(int(num) ** 2 for num in str(n))
            if n in save_list:
                return False
            save_list.append(n)
        return True