class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setS = set()
        for i in range(len(nums)):
            if nums[i] in setS:
                return True
            setS.add(nums[i])

        return False