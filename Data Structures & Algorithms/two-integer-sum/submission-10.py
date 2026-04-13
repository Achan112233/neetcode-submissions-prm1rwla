class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            idx = target - num
            if num in dic:
                return [dic.get(num), i]
            dic[idx] = i
