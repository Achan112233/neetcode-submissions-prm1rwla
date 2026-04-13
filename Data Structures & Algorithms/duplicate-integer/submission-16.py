class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set()
        for num in nums:
            if num in curr:
                return True
            else:
                curr.add(num)
        return False