class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        num_ref = nums[k]
        for index in range(1, len(nums)):
            if nums[index] != num_ref:
                k += 1
                nums[k] = nums[index]
                num_ref = nums[index]
            # if k != index:
            #     nums[index] = '_'
        return k + 1