class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 
        sum_nums = numbers[l] + numbers[r]

        while sum_nums != target:
            if sum_nums > target:
                r -= 1
            else:
                l += 1
            sum_nums = numbers[l] + numbers[r]
        return [l+1, r+1]