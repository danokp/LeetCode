class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] < float('inf') else -1