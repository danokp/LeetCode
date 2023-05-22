class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums) + 1
        target_sum = len_nums * (len_nums - 1) / 2
        return int(target_sum - sum(nums))
