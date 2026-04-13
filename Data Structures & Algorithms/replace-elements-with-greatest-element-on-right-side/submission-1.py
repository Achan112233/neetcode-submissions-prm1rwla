class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        currMax = -1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = currMax
            if arr[i] > currMax:
                currMax = arr[i]
        return ans