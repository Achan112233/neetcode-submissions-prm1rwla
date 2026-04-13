class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given integer nums, and int target, return two indices such that they return target.

        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic.get(nums[i]), i]
            dic[target - nums[i]] = i
        return []