class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_avg = total
        for i, num in enumerate(nums[k:]):
            total += num
            total -= nums[i]
            max_avg = max(total, max_avg)
        return max_avg / k