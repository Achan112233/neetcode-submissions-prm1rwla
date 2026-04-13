class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        we can add it to a set
        '''

        numbers = set(nums)
        ans = 0
        for num in numbers:
            # we have a starting value
            if (num - 1) not in numbers:
                length = 1
                while (num + length) in nums:
                    length += 1
                ans = max(length, ans)
        return ans
            
