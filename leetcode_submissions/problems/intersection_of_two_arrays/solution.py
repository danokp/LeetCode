class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_1 = {}
        for num in nums1:
            dict_1[num] = True

        res = []
        for num in nums2:
            # print(dict_1[num])
            if dict_1.get(num):
                res.append(num)
                dict_1[num] = False
        return res