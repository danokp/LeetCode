class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 ={}
        for i, n in enumerate(nums):
            m = target - n
            if m in dict_1:
                return [dict_1[m], i]
            else:
                dict_1[n] = i
