class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        sorted_cost = sorted(cost, reverse=True)
        while len(sorted_cost) > 2:
            total += sorted_cost.pop(0)
            total += sorted_cost.pop(0)
            sorted_cost.pop(0)
        return total + sum(sorted_cost)