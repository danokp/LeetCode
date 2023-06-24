class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def inner(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            ret = float('inf')
            for coin in coins:
                ret = min(ret, inner(amount - coin) + 1)
            return ret
        ans = inner(amount)

        return ans if ans != float('inf') else -1