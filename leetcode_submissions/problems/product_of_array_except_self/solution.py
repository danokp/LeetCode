class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_begining = [1]
        from_end = [1]
        for i in range(1, len(nums)):
            from_begining.append(from_begining[i-1] * nums[i-1])
        # # for i in range(-2, -len(nums)-1, -1):
        #     print(f'{nums[-i]=}, {from_end[-i]=}')
            from_end.append(from_end[i-1] * nums[-i])
        # print(from_begining)
        # print(from_end)
        return list(map(
            lambda a, b: a * b,
            from_begining,
            from_end[::-1]
        ))        


