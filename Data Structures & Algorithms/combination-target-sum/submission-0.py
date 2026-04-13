class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        
        '''
        res = []

        subset = []

        def backtrack(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if sum(subset) > target:
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j)
                subset.pop()
        backtrack(0)
        return res
                


