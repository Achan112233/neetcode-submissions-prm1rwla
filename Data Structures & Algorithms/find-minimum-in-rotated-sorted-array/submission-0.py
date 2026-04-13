class Solution:
    def findMin(self, nums: List[int]) -> int:
        # notoce thjat as soon as we see the element next is less, this means we have the min
        # if we have an element and its next is larger, we go to the
        # we can check if m < r: if yes, r = m - 1
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]