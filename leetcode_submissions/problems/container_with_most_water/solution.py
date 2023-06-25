class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(height)-1

        while l < r:
            max_vol = max(max_vol, min(height[r], height[l]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return max_vol