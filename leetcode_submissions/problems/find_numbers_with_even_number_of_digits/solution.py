class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        filtered = list(filter(lambda num: len(str(num)) % 2 == 0, nums))
        return len(filtered)
