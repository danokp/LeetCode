class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        flowerbed_cp = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed_cp)-1):
            if not sum(flowerbed_cp[i-1:i+2]):
                count += 1
                flowerbed_cp[i] = 1
                # if count == n:
                #     return True
        return count >= n