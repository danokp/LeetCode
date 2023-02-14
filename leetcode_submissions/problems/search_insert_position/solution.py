class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index_start, index_end = 0, len(nums) - 1
        while index_start <= index_end:
            index_mid = (index_end + index_start) // 2
            mid_num = nums[index_mid]
            if mid_num < target:
                index_start = index_mid + 1
            elif mid_num == target and nums[index_mid-1] != target:
                return index_mid
            else:
                index_end = index_mid - 1
        return index_start