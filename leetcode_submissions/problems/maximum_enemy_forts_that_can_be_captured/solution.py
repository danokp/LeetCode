class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """

        def get_index(list, value):
            try:
                index = list.index(value)
            except ValueError:
                index = len(list)-1
            return index

        max_forts_captured = 0
        count = 0
        start_fort_index = min(get_index(forts, -1), get_index(forts, 1))
        start_fort = forts[start_fort_index]
        for fort in forts[start_fort_index+1:]:
            if fort == 0 and start_fort != 0:
                count += 1
            if start_fort * fort == -1:
                max_forts_captured = max(max_forts_captured, count)
                count = 0
                start_fort = fort
            if start_fort == fort:
                count = 0
                start_fort = fort
            # print(f'{start_fort=}, {fort=}, {count=}')
        # print(max_forts_captured)
        return max_forts_captured
