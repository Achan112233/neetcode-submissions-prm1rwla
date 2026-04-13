class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        currMax = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > currMax:
                currMax = arr[i]
            ans.append(currMax)
        ans.reverse()
        ans.append(-1)
        return ans