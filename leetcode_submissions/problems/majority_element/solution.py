class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        num_dict = Counter(nums)
        for num, count in num_dict.items():
            if count > len(nums)/2:
                return num