class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        memoization
        or top down
        we can choose between 1, 5, 10
        [1, 5, 10]
        amount = 5
        can take 6 small coins or 2 large coin
        '''
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1