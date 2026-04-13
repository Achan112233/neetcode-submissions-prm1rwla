class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we can iterate through the list, make a tuple with distance as key and coord as snd

        distances = []

        for x, y in points:
            distances.append((math.sqrt(x * x + y * y), x, y))

        heapq.heapify(distances)

        ans = []
        for i in range(k):
            dist, x, y = heapq.heappop(distances)
            ans.append([x, y])
        return ans