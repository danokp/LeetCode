class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        from math import ceil
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = ceil((r + l) / 2)

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid - 1
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                l = mid + 1