class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_1 = {}
        for num in nums1:
            dict_1[num] = dict_1.get(num, 0) + 1

        res = []
        for num in nums2:
            if dict_1.get(num):
                res.append(num)
                dict_1[num] -= 1
        return res
