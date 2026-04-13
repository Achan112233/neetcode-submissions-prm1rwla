class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        given an integer of nums, return the longest consecutive seuqnece of elemetns that can be formed

        consecutive sequence is a sequence of each elemeent where there is 1 greater than the prev element

        elements dop not have to be consecutive in original array

        [2,20,4,10,3,4,5]

        longest is 

        if we sort

        2, 3, 4, 4, 5, 10, 20
        longest -> 2, 3, 4, 5

        only one four matters
        we can make it a set

        for each number, we check if the i + 1 is in the numberset.
        we increase for each..
        this makes n^2
        can we do beter

        we can make a conditional to check..

        so what defines a start of sequence. if there is no number before it
        we can then start counting
        '''

        numbers = set(nums)
        range, maxrange = 0, 0
        for num in numbers:
            if num - 1 not in numbers:
                #marks start of sequence
                while num + range in numbers:
                    range += 1
                maxrange = max(maxrange, range)
                range = 0
        return maxrange