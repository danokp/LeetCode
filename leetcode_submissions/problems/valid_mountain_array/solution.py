class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        while arr[i-1] < arr[i] and i < len(arr)-1:
            i += 1
        j = len(arr)-1
        while arr[j-1] > arr[j] and j > 0:
            j -= 1
        return i-1 == j and i-1 > 0
