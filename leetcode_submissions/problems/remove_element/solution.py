class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len_num = len(nums)
        for i, num in enumerate(nums[::-1]):
            # print(f'{i=}, {num=}')
            if num == val:
                nums.pop(len_num - i - 1)
        # print(f'{nums=}')
        return len(nums)