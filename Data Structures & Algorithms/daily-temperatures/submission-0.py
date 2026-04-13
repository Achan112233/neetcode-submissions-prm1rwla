class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day

        return result array where ith of result is the number of days after the ith day before a warmer temp appears on a future day
        if there is no day, set it to zero

        keep an array of count. iterate those until we reach an amount that is higher
        
        stops as soon as we encounter the first most.
        STOP THINKING ABOUT OPTIMZIED

        '''
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res