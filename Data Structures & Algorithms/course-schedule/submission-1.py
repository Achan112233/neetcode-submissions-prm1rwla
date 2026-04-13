class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set) 
        in_deg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].add(a)
            in_deg[a] += 1

        q = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        res = 0
        while q:
            print(q)
            c = q.popleft()
            res += 1
            for course in graph[c]:
                in_deg[course] -= 1
                if in_deg[course] == 0:
                    q.append(course)
        
        return res == numCourses


            


