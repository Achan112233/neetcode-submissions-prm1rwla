class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given int array nums, return array where output at i is the product of all eelemnts of nums except nums[i]
        # ex: output [2] = 12 = 1 * 2 * 6

        # what can we do to sum everything.. pref, post fill in

        res = [1] * len(nums) #<- to store the multi answers

        prefix = 1

        for n in range(len(nums)):
            res[n] = prefix
            prefix *= nums[n]
        
        postfix = 1

        for n in range(len(nums) - 1, -1, -1):
            res[n] *= postfix
            postfix *= nums[n]

        return res