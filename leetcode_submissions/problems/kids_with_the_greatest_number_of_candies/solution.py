class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies) - extraCandies
        return [n >= max_cand for n in candies]