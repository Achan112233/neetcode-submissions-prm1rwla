class Solution:
    def climbStairs(self, n: int) -> int:
        # given int n return how many times we can reach by adding 1 or 2.
        # distinct ways, order matters
        # only 1 or 2
        # starting from brute force, we add 2 and slowly, we get to 1
        # greedy...
        # any number is made up of a combination of 1 and 2
        # make an array of prev stored combos
        # each recursive call is a value
        # base case: for 1, there is only 1 way to make and that is [1]
        # for 2, we can do 1 + 1 or 2
        # for 4, we can do 1 + 1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 2 + 2
        cache = []
        # start with the n, figure out that it can be added together with other elements, which ones. ..
        # 

        # starting from zero, we fill 

        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp[i])
        return dp[n]
            
            
        
