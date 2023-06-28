class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        pointer_1 = m - 1
        pointer_2 = n - 1
        poiner_res = m + n - 1
        while pointer_2 >= 0:
            if pointer_1 < 0 or nums2[pointer_2] >= nums1[pointer_1]:
                nums1[poiner_res] = nums2[pointer_2]
                pointer_2 -= 1
            else:
                nums1[poiner_res] = nums1[pointer_1]
                pointer_1 -= 1
            poiner_res -= 1        
