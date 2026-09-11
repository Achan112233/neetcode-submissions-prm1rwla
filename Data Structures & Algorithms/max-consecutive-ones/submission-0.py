class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCount = 0
        maxCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currCount += 1
            else:
                maxCount = max(currCount, maxCount)
                currCount = 0

        return max(maxCount, currCount)