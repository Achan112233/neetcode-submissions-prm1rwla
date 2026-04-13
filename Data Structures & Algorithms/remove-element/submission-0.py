class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        main idea is to remove instance of val in place,

        '''
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums.remove(nums[idx])
            else:
                idx += 1
        return len(nums)