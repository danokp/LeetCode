class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = [i for i in str(num)]
        num_list_sorted = sorted(num_list)
        # print(num_list_sorted)
        return (int(num_list_sorted[0] + num_list_sorted[2]) +
                int(num_list_sorted[1] + num_list_sorted[3]))