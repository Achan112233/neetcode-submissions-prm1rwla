class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        numbers sorted increasing order return two indices such that they add up to given number

        '''

        l, r = 0, len(numbers) - 1

        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                return([l + 1, r + 1])

            if add > target:
                r -= 1
            
            if add < target:
                l += 1
        
