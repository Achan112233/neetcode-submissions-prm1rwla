class Solution:

    def tribonacci(self, n: int) -> int:
        '''
        t0 = 0
        t1 = 1
        t2 = 1
        tn+3 = tn + tn+1 + tn+2 for any pos n
        given n, return tn

        

        ''' 
        memo = [-1] * (n + 1)

        def recurse(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if memo[i] != -1:
                return memo[i]

            memo[i] = recurse(i - 1) + recurse(i - 2) + recurse(i - 3)
            return memo[i]
        
        return recurse(n)
