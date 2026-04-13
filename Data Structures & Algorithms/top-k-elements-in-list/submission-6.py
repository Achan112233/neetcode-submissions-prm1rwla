class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an array of nums, return the k most frequent elements within array
        
        dic = {}

        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for num, cnt in dic.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
