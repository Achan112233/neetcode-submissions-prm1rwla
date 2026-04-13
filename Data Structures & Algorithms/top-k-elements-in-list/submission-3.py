
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        scount = {}
        
        for num in nums: 
            scount[num] = 1 + scount.get(num, 0)
            
        arr = []
        for num, cnt in scount.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while (len(res) < k):
            res.append(arr.pop()[1])
        return res