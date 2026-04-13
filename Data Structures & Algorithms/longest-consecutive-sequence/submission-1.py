class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        we can add it to a set
        '''
        numbers = set(nums)

        longest = 0

        for num in numbers:
            #instead of checking for longest streak every time.
            # we check for when the streak starts
            if (num - 1) not in numbers:
                length = 1
                while num + length in numbers:
                    length += 1
                longest = max(length, longest)
        return longest
            
