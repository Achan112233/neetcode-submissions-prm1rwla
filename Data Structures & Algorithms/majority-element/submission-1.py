class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # keep result as first seen
        # also keep occurences, if occurences ever hits zero, we swap result since that is not most seen

        res = nums[0]
        occ = 1 

        for i in range(1, len(nums)):
            if nums[i] == res:
                occ += 1
            else:
                occ = max(0, occ - 1)
            if occ == 0:
                res = nums[i]
        
        return res

        

        